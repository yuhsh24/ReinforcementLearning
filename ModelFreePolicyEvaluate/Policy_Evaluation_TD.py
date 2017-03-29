# -*- coding:utf-8 -*-

from Mdp import *

def policy_evaluation_td(state_sample, action_sample, reward_sample, mdp, alpha):
    V = dict()
    for state in mdp.state:
        V[state] = 0

    for iter1 in xrange(len(state_sample)):
        for iter2 in xrange(len(state_sample[iter1])):
            state = state_sample[iter1][iter2]
            if iter2 < (len(state_sample[iter1]) - 1):
                next_v = V[state_sample[iter1][iter2+1]]
            else:
                next_v = 0
            V[state] += alpha * (reward_sample[iter1][iter2] + mdp.gamma * next_v - V[state])

    return V

if "__main__" == __name__:
    mdp = Mdp()
    state_sample, action_sample, reward_sample = mdp.generate_randompi_sample(1000000)
    v = policy_evaluation_td(state_sample, action_sample, reward_sample, mdp, 0.2)
    print "policy_evaluation_td:"
    for state in xrange(1, 6):
        print "%d: %f"%(state, v[state])
