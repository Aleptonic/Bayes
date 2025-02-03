"""
PROBLEM:
        Street Blocks are labelled from 1 to n
        Walking from any state (s) to state (s+1) takes 1 min
        Magic train from any state (s) to state (2s) takes 2 min
        How to travel from 1 to n in least time?

        Tram fails with a probability of 0.5
"""
import sys
import os
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
            failProb=0.7
            result.append(((2*state),1-failProb,-2.))
            result.append(((state),failProb,-2.))
        return result
    def discount(self):
        return 1.
    def states(self):
        return range(1,self.N+1)
# Algorithms
def valueIterations(mdp):
    #Initialization
    V={} # state-> Vopt[state]
    for state in mdp.states():
        V[state]=0
    def Q(state,action):
            return sum(prob * (reward + mdp.discount() * V[newState]) for newState, prob, reward in mdp.succProbReward(state, action))
    for i in range(1000):
        # Compute new values given old values
        newV ={}
        for state in mdp.states():
            if mdp.isEnd(state)==True:
                newV[state]=0
            else:
                newV[state]=max(Q(state,action)for action in mdp.actions(state)) 
        # check for convergence
        if max(abs(V[state]-newV[state])for state in mdp.states())<1e-10:
            break
        V=newV
        #read the policy
        pi={}
        for state in mdp.states():
            if mdp.isEnd(state):
                pi[state]='None'
            else:
                pi[state]=max((Q(state,action),action)for action in mdp.actions(state))[1]

        # print stuff
        #os.system('clear')
        print('{:15}{:15}{:15}'.format('s','V(s)','pi(s)'))
        for state in mdp.states():
            print('{:15}{:15}{:15}'.format(state,V[state],pi[state]))

mdp=TransportationMDP(N=10)
# print(mdp.actions(3))
# print(mdp.succProbReward(3,'wlk'))
# print(mdp.succProbReward(3,'tram'))
valueIterations(mdp)