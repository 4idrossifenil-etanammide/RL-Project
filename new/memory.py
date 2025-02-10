class Memory():
    
    def __init__(self):
    #initialize the memories for the training
        self.actions = []
        self.rewards = []
        self.old_log_probs = []
        self.values = []
        self.agent_states = []
        self.returns =[]
        self.advantages = []

    def add_episode(self, num_agents):
    #add an array for collecting data of current episode
        self.actions.append([ [] for _ in range(num_agents) ])
        self.rewards.append([ [] for _ in range(num_agents) ])
        self.old_log_probs.append([ [] for _ in range(num_agents) ])
        self.values.append([ [] for _ in range(num_agents) ])
        self.agent_states.append( {"physical": [],
                                     "utterances": [],
                                     "memories": [],
                                     "tasks": []} )
        self.returns.append([ [] for _ in range(num_agents) ])
        self.advantages.append([ [] for _ in range(num_agents) ])
        return

    def add_step(self, agent_index, action, reward, old_log_prob, value):
    #add data coming from step execution for a single agent
        self.actions[-1][agent_index].append(action)
        self.rewards[-1][agent_index].append(reward)
        self.old_log_probs[-1][agent_index].append(old_log_prob)
        self.values[-1][agent_index].append(value)
        return
    
    def add_step_state(self, state, agent):
    #add the state data for the current step
        self.agent_states[-1]["physical"].append(state["physical"].to(agent.device))
        self.agent_states[-1]["utterances"].append(state["utterances"].to(agent.device))
        self.agent_states[-1]["memories"].append(state["memories"].to(agent.device))
        self.agent_states[-1]["tasks"].append(state["tasks"].to(agent.device))
        return
    
    def add_objective_functions(self, agent_index, ret, advantage):
    #add the objective functions for the current episode
        self.returns[-1][agent_index] = ret
        self.advantages[-1][agent_index] = advantage
        return
    
    def get_reward(self, episode, agent_index):
    #return the rewards for a single agent
        return self.rewards[episode][agent_index]
    
    def get_values(self, episode, agent_index):
    #return the values for a single agent
        return self.values[episode][agent_index]
    
    def get_states(self, episode):
    #return the states for the current episode
        return self.agent_states[episode]
    
    def get_returns(self, episode, agent_index):
    #return the returns for the current episode
        return self.returns[episode][agent_index]
    

    