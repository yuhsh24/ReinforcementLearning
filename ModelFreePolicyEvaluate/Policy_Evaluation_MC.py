# -*- coding:utf-8 -*-

from Mdp import *

def policy_evaluation_mc(state_sample, action_sample, reward_sample, mdp):
    V = dict()
    N = dict()
    for state in mdp.state:
        V[state] = 0
        N[state] = 0

    for iter1 in xrange(len(state_sample)):
        g = 0
        for iter2 in xrange(len(state_sample[iter1])-1, -1, -1):
            g *= mdp.gamma
            g += reward_sample[iter1][iter2]

        for iter2 in xrange(len(state_sample[iter1])):
            s = state_sample[iter1][iter2]
            V[s] += g
            N[s] += 1
            g = g - reward_sample[iter1][iter2]
            g = g / mdp.gamma

    for state in V:
        if N[state] > 0.001:
            V[state] = V[state] / N[s]

    return V

if "__main__" == __name__:
    mdp = Mdp()
    state_sample, action_sample, reward_sample = mdp.generate_randompi_sample(1000000)
    v = policy_evaluation_mc(state_sample, action_sample, reward_sample, mdp)
    print "policy_evaluation_mc:"
    for state in xrange(1, 6):
        print "%d: %f"%(state, v[state])



