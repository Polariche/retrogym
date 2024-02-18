#from collections.abc import abstractclass

class BaseReward:
    def __init__(self, targets, reward):
        self.targets = targets
        self.reward = reward

    #@abstractclass
    def get_reward(self, past_obs, action, obs):
        raise NotImplementedError
    
class NewReward(BaseReward):
    def __init__(self, targets, reward):
        super().__init__(targets, reward)
        self.q = set()

    def get_reward(self, past_obs, action, obs):
        past_obs = tuple([past_obs[t] for t in self.targets])
        obs = tuple([obs[t] for t in self.targets])

        if obs == past_obs:
            return 0
        elif obs in self.q:
            return 0
        
        self.q.add(obs)
        return self.reward

class DuplicateReward(BaseReward):
    def __init__(self, targets, reward):
        super().__init__(targets, reward)
        self.q = set()

    def get_reward(self, past_obs, action, obs):
        past_obs = tuple([past_obs[t] for t in self.targets])
        obs = tuple([obs[t] for t in self.targets])

        if obs == past_obs:
            return self.reward
        elif obs in self.q:
            return self.reward
        
        self.q.add(obs)
        return 0
    
class UnchangedReward(BaseReward):
    def get_reward(self, past_obs, action, obs):
        past_obs = tuple([past_obs[t] for t in self.targets])
        obs = tuple([obs[t] for t in self.targets])

        if obs == past_obs:
            return self.reward
        
        return 0
    
class ChangedReward(BaseReward):
    def get_reward(self, past_obs, action, obs):
        past_obs = tuple([past_obs[t] for t in self.targets])
        obs = tuple([obs[t] for t in self.targets])

        if obs == past_obs:
            return 0
        
        return self.reward
    
class DefaultReward(BaseReward):
    def get_reward(self, past_obs, action, obs):
        return self.reward
    

reward_objects = {
                    "new": NewReward, 
                    "duplicate": DuplicateReward,
                    "changed": ChangedReward, 
                    "unchanged": UnchangedReward, 
                    "default": DefaultReward
                 }

def create_reward(reward_model):
    try:
        return reward_objects[reward_model.type](reward_model.targets, reward_model.reward)

    except IndexError:
        raise Exception(f"'{reward_model.type}' does not have a Reward class")