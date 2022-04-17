#create a board structure
import cellStructure
import transitionModel

class Board:
    
    def __init__(self,reward,discount):
        self.reward = reward
        self.discount = discount
        self.utilityList = []
        for i in range(11):
            self.utilityList.append(cellStructure.Cell(0,"T",False))
            if i==6:
                self.utilityList[i].isTerminalState = True
                self.utilityList[i].action = "T"
                self.utilityList[i].reward = -1
                self.utilityList[i].prevReward = -1
            elif i==10:
                self.utilityList[i].isTerminalState = True
                self.utilityList[i].action = "T"
                self.utilityList[i].reward = 1
                self.utilityList[i].prevReward = 1
                
                
    # Transition sum
    def getTransitionSum(self,cellIndex,actionIndex):
        transition_model = []
        sum = 0
        #print(cellIndex,actionIndex)
        transition_model = transitionModel.P[actionIndex][cellIndex]
        for i in range(len(transition_model)):
            sum += transition_model[i]*self.utilityList[i].prevReward
        return sum
                
    def solve(self):
        diff = 1
        while diff > 0:
            for i in range(11):
                if(self.utilityList[i].isTerminalState == True):
                    continue
                Action = 'UP'
                maxval = self.getTransitionSum(i,0)
                move_right = self.getTransitionSum(i,1)
                move_down = self.getTransitionSum(i,2)
                move_left = self.getTransitionSum(i,3)
                if(move_right>maxval):
                    maxval = move_right
                    Action = 'RIGHT'
                if(move_down>maxval):
                    maxval = move_down
                    Action = 'DOWN'
                if(move_left>maxval):
                    maxval = move_left
                    Action = 'LEFT'
                    
                newValue = self.reward + (self.discount*maxval)
                var = abs(newValue - self.utilityList[i].prevReward)
                #if(var > diff):
                diff = var
                self.utilityList[i].prevReward = self.utilityList[i].reward
                self.utilityList[i].reward = newValue
                self.utilityList[i].action = Action
    
    def output(self):
        print("Discount : {}".format(self.discount)+" Reward : {} ".format(self.reward))
        print("============================")
        print("[")
        for i in range(11):
            print("{0:.4f}".format(self.utilityList[i].reward), end="\t")
        print("]")
        print(str(self.utilityList[7].action), end="\t")
        print(str(self.utilityList[8].action), end="\t")
        print(str(self.utilityList[9].action), end="\t")
        print(str(self.utilityList[10].action), end="\t\n")
        print(str(self.utilityList[4].action), end="\t")
        print("0", end="\t")
        print(str(self.utilityList[5].action), end="\t")
        print(str(self.utilityList[6].action), end="\t\n")
        print(str(self.utilityList[0].action), end="\t")
        print(str(self.utilityList[1].action), end="\t")
        print(str(self.utilityList[2].action), end="\t")
        print(str(self.utilityList[3].action), end="\t\n")
        print("============================")