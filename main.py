# Import necessary modules
import numpy as np
import math
import boardStructure


#solve MDP for input 1
obj1 = boardStructure.Board(-0.04, 0.99)
obj1.solve()
obj1.output()

#solve MDP for input 2
obj1 = boardStructure.Board(-0.04, 0.5)
obj1.solve()
obj1.output()

#solve MDP for input 3
obj1 = boardStructure.Board(-0.25, 0.5)
obj1.solve()
obj1.output()