# -*- coding: utf-8 -*-

class Mdp:

    def __init__(self):
        # 状态 state
        self.state = [1, 2, 3, 4, 5, 6, 7, 8]
        # 终止状态 terminalstate
        self.terminalstate = dict()
        self.terminalstate[6] = True
        self.terminalstate[7] = True
        self.terminalstate[8] = True
        # 动作 action
        self.action = ["n", "e", "s", "w"]  # 北东南西
        # 奖励 reward
        self.reward = dict()
        self.reward["2_s"] = -1.0
        self.reward["3_s"] = -1.0
        self.reward["4_s"] = 1.0
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

        is_terminalstate = False
        if next_state in self.terminalstate:
            is_terminalstate = True

        reward = 0
        if key in self.reward:
            reward = self.reward[key]

        return is_terminalstate, next_state, reward
