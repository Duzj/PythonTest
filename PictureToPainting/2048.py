# -*- coding = utf-8 -*-
import curses
from random import randrange, choice
from collections import defaultdict


# 有效输入
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# 有效输入键
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# 输入与行为进行关联
actions_dict = dict(zip(letter_codes, actions*2))

class GameField(object):
    # 初始化棋盘的参数
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

     # 随机生成一个2或4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    # 重置棋盘
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)]for j in range(self.height)]
        self.spawn()
        self.spawn()


if __name__ == '__main__':
    print([[0 for i in range(4)]for j in range(4)])
