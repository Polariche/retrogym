#from collections.abc import abstractclass

class BaseEnding:
    def __init__(self, targets, values):
        self.targets = targets
        self.values = values

    #@abstractclass
    def done(self, past_obs, action, obs):
        raise NotImplementedError

class MatchEnding(BaseEnding):
    def done(self, past_obs, action, obs):
        for target, value in zip(self.targets, self.values):
            if obs[target] != value:
                return False 
        return True

class TimeoutEnding(BaseEnding):
    def __init__(self, targets, values):
        super().__init__(targets, values)
        self.time = 0

    def done(self, past_obs, action, obs):
        if self.time > self.values[0]:
            return True
        
        self.time = self.time+1
        return False
    
ending_objects = {
                    "match": MatchEnding, 
                    "timeout": TimeoutEnding,
                 }

def create_ending(ending_model):
    try:
        return ending_objects[ending_model.type](ending_model.targets, ending_model.values)

    except IndexError:
        raise Exception(f"'{ending_model.type}' does not have an Ending class")