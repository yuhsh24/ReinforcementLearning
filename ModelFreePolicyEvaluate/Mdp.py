# -*- coding:utf-8 -*-

import random

class Mdp:

    def __init__(self):
        # 状态　state
        self.state = [1, 2, 3, 4, 5, 6, 7, 8]
        # 终止状态 terminalstate
        self.terminalstate = dict()
        self.terminalstate[6] = True
        self.terminalstate[7] = True
        self.terminalstate[8] = True
        # 动作 actions
        self.action = ["n", "e", "s", "w"]  # 北东南西
        # 奖励 reward
        self.reward = dict()
        self.reward["2_s"] = -1
        self.reward["3_s"] = -1
        self.reward["4_s"] = 1
        # 状态转义 t
        self.t = dict()
        self.t["1_e"] = 2
        self.t["2_w"] = 1
        self.t["2_e"] = 3
        self.t["2_s"] = 6
        self.t["3_w"] = 2
        self.t["3_e"] = 4
        self.t["3_s"] = 7
        self.t["4_w"] = 3
        self.t["4_e"] = 5
        self.t["4_s"] = 8
        self.t["5_w"] = 4
        # 衰减系数 gamma
        self.gamma = 0.8

    def transform(self, state, action):

        if state in self.terminalstate:
            return True, state, 0

        key = "%d_%s"%(state, action)
        if key in self.t:
            next_state = self.t[key]
        else:
            next_state = state

        is_terminal = False
        if next_state in self.terminalstate:
            is_terminal = True

        reward = 0.0
        if key in self.reward:
            reward = self.reward[key]

        return is_terminal, next_state, reward

    def generate_randompi_sample(self, num):
        state_sample = []
        action_sample = []
        reward_sample = []
        for i in xrange(num):
            tmp_state = []
            tmp_action =[]
            tmp_reward = []

            s = self.state[int(random.random() * len(self.state))]
            is_terminal = False
            while False == is_terminal:
                a = self.action[int(random.random() * len(self.action))]
                is_terminal, s1, reward = self.transform(s, a)
                tmp_state.append(s)
                tmp_action.append(a)
                tmp_reward.append(reward)
                s = s1

            state_sample.append(tmp_state)
            action_sample.append(tmp_action)
            reward_sample.append(tmp_reward)

        return state_sample, action_sample, reward_sample

