# -*- coding:utf-8 -*-

import random
random.seed(0)
from Mdp import *

def random_pi():
    action_set = ["n", "e", "s", "w"]
    index = int(random.random() * 4)
    return action_set[index]

def compute_random_pi_state_value():
    value = [0.0 for i in xrange(9)]
    max_iterator_num = 1000000

    for k in xrange(1, max_iterator_num):
        for state in xrange(1, 6):
            mdp = Mdp()
            s = state
            gamma = 1.0
            v = 0.0
            is_terminal = False

            while is_terminal is False:
                action = random_pi()
                is_terminal, s, reward = mdp.transform(s, action)
                v += gamma * reward
                gamma *= mdp.gamma

            value[state] = (value[state] * (k - 1) + v) / k

        if k % 100000 == 0:
            print "state value: ", value[1:6]

    print "state value: ", value[1:6]

if "__main__" == __name__:
    compute_random_pi_state_value()