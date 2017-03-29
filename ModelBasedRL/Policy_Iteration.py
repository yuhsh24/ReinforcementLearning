# -*- coding:utf-8 -*-

from Mdp import Mdp

class Policy_Iteration:

    # 初始化
    def __init__(self, mdp):
        # 保存状态价值
        self.v = [0.0 for state in xrange(len(mdp.state)+1)]
        # 策略保存
        self.pi = dict()
        for state in mdp.state:
            if state in mdp.terminalstate:
                continue
            self.pi[state] = mdp.action[0] # 随机初始化策略

    def __policy_evaluate(self, mdp):
        max_iteration_num = 1000
        for i in xrange(max_iteration_num):
            delta = 0.0

            for state in mdp.state:
                if state in mdp.terminalstate:
                    continue
                action = self.pi[state]
                is_terminal, next_state, reward = mdp.transform(state, action)
                value = reward + mdp.gamma * self.v[next_state]
                delta += abs(value - self.v[state])
                self.v[state] = value

            if delta < 1e-6:
                break


    def __policy_imporve(self, mdp):
        for state in mdp.state:
            if state in mdp.terminalstate:
                continue

            a = mdp.action[0]
            is_terminal, next_state, reward = mdp.transform(state, a)
            value = reward + mdp.gamma * self.v[next_state]
            for action in mdp.action:
                is_terminal, next_state, reward = mdp.transform(state, action)
                if value < reward + mdp.gamma * self.v[next_state]:
                    value = reward + mdp.gamma * self.v[next_state]
                    a = action

            self.pi[state] = a


    # 策略迭代方法
    def policy_iteration(self, mdp):
        max_iteration_num = 100
        for i in xrange(max_iteration_num):
            self.__policy_evaluate(mdp)
            self.__policy_imporve(mdp)

if "__main__" == __name__:
    mdp = Mdp()
    policy_value = Policy_Iteration(mdp)
    policy_value.policy_iteration(mdp)
    print "value:"
    for state in xrange(1, 6):
        print "state:%d value:%f"%(state, policy_value.v[state])

    print "policy:"
    for state in xrange(1, 6):
        print "state:%d policy:%s"%(state, policy_value.pi[state])

