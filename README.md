# Value Iteration algorithm to solve Markov Decision Process(MDP)

## Problem Statement 
A Markov decision process (MDP) is a sequential choice problem with a Markovian transition model and additive rewards in a fully observable, stochastic environment. A set of states, a set of actions, a transition model, and a reward function make up the system. There is a simple 4 x 3 environment, and each block represents a state. The agent can move left, right, up, or down from a state. The "intended" outcome occurs with probability 0.8, but with probability 0.2 the agent moves at right angles to the intended direction. A collision with the wall or boundary results in no movement. The two terminal states have reward +1 and -1, respectively, and all other states have a constant reward (e.g., of -0.01).
Also, a MDP usually has a discount factor γ, a number between 0 and 1, that describes the preference of an agent for current rewards over future rewards.


## Instructions to execute the code:
### Prerequisites:
* Make sure you have python installed.
* Make sure you have numpy installed.
* When you import the code in an IDE make sure there are no errors on the imports.


### Steps to run the program:
* Clone the repository.
* Go to the folder containing the code(four different files).
* Execute the main file.
* Open the terminal and and run command- py main.py
* Change the input values(discount and reward) in the main function.
