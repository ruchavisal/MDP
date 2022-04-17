#create cell structure
class Cell:
    
    def __init__(self,reward,action,isTerminalState):
        self.reward = reward
        self.prevReward = reward
        self.action = action
        self.isTerminalState = isTerminalState