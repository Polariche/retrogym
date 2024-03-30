/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

#include <iostream>
#include <memory>
#include <string>

// #include "absl/flags/flag.h"
// #include "absl/flags/parse.h"
// #include "absl/strings/str_format.h"

// #include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

#include "grpc_emulator.grpc.pb.h"

#include "emulator.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using retrogym::GRPCEmulator;
using retrogym::BoolValue;
using retrogym::Int32Value;
using retrogym::PathRequest;
using retrogym::Void;
using retrogym::Key;
using retrogym::KeysResponse;
using retrogym::SetKeyRequest;
using retrogym::MemorySizeRequest;
using retrogym::MemoryDataRequest;
using retrogym::MemorySizeResponse;
using retrogym::MemoryDataResponse;

// ABSL_FLAG(uint16_t, port, 50051, "Server port for the service");

// Logic and data behind the server's behavior.
class GRPCEmulatorServiceImpl final : public GRPCEmulator::Service {
  Emulator emu;

  Status Init(ServerContext* context, const PathRequest* request,
                  BoolValue* response) override {
    response->set_bool_(emu.init(request->path().c_str()));

    return Status::OK;
  }

  Status Deinit(ServerContext* context, const Void* request,
                  BoolValue* response) override {
    response->set_bool_(emu.deinit());

    return Status::OK;
  }

  Status LoadGame(ServerContext* context, const PathRequest* request,
                  BoolValue* response) override {
    response->set_bool_(emu.load_game(request->path().c_str()));
    return Status::OK;
  }

  Status UnloadGame(ServerContext* context, const Void* request,
                  BoolValue* response) override {
    response->set_bool_(emu.unload_game());
    return Status::OK;
  }

  Status LoadState(ServerContext* context, const PathRequest* request,
                  BoolValue* response) override {
    response->set_bool_(emu.load_state(request->path().c_str()));
    return Status::OK;
  }

  Status SaveState(ServerContext* context, const PathRequest* request,
                  BoolValue* response) override {
    response->set_bool_(emu.save_state(request->path().c_str()));
    return Status::OK;
  }

  Status Run(ServerContext* context, const Void* request,
                  BoolValue* response) override {
    response->set_bool_(emu.run());
    return Status::OK;
  }

  Status Reset(ServerContext* context, const Void* request,
                  BoolValue* response) override {
    response->set_bool_(emu.reset());
    return Status::OK;
  }

  Status Width(ServerContext* context, const Void* request,
                  Int32Value* response) override {
    response->set_int32(emu.get_width());
    return Status::OK;
  }

  Status Height(ServerContext* context, const Void* request,
                  Int32Value* response) override {
    response->set_int32(emu.get_height());
    return Status::OK;
  }

  Status GetKeys(ServerContext* context, const Void* request,
                  KeysResponse* response) override {

    std::vector<std::pair<int, std::string>> emu_keys = emu.get_keys();

    for(auto & k : emu_keys) {
      Key* key = response->add_keys();
      key->set_id(k.first);
      key->set_description(k.second);
    }

    return Status::OK;
  }

  Status SetKey(ServerContext* context, const SetKeyRequest* request,
                  Void* response) override {
    emu.set_key(request->id(), request->value());
    return Status::OK;
  }

  Status GetMemorySize(ServerContext* context, const MemorySizeRequest* request,
                  MemorySizeResponse* response) override {
    unsigned id = request->id();
    response->set_size(emu.get_memory_size(id));
    return Status::OK;
  }

  Status GetMemoryData(ServerContext* context, const MemoryDataRequest* request,
                  MemoryDataResponse* response) override {
    unsigned id = request->id();
    unsigned addr = request->addr();
    response->set_data(emu.get_memory_data(id, addr));
    return Status::OK;
  }

};

void RunServer(uint16_t port) {
  std::string server_address = absl::StrFormat("0.0.0.0:%d", port);

  GRPCEmulatorServiceImpl service;

  grpc::EnableDefaultHealthCheckService(true);
  // grpc::reflection::InitProtoReflectionServerBuilderPlugin();

  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  // Finally assemble the server.
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;

  server->Wait();
}

int main(int argc, char** argv) {
  //absl::ParseCommandLine(argc, argv);
  RunServer(50001); //absl::GetFlag(FLAGS_port));
  return 0;
}
