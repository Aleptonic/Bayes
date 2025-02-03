"""
PROBLEM:
        Street Blocks are labelled from 1 to n
        Walking from any state (s) to state (s+1) takes 1 min
        Magic train from any state (s) to state (2s) takes 2 min
        How to travel from 1 to n in least time?

        Tram fails with a probability of 0.5
"""
import sys

sys.setrecursionlimit(1000)

class TransportationMDP:
    def __init__(self,N):
        # N is the number of blocks
        self.N=N
    def startState(self):
        return 1
    def isEnd(self,state):
        return state==self.N
    def actions(self,state):
        # reutrns a list of valid actions
        result=[]
        if state+1<=self.N:
            result.append('wlk')
        if state*2<=self.N:
            result.append('tram')
        return result
    def succProbReward(self,state,action):
        # return a list of (neState,prob,reward) as triplet
        # s= state, a=action, s'=new state
        # prob= T(s,a,s')
        # reward = R(s,a,s')
        result=[]
        if action=='wlk':
            result.append(((state+1),1.,-1.))
        elif action=='tram':
            result.append(((2*state),0.5,-2.))
            result.append(((state),0.5,-2.))
        return result
    def discount(self):
        return 1.
    def states(self):
        return range(1,self.N+1)
mdp=TransportationMDP(N=10)
print(mdp.actions(3))
print(mdp.succProbReward(3,'wlk'))
print(mdp.succProbReward(3,'tram'))