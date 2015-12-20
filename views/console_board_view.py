# -*- coding:utf-8 -*-

class ConsoleBoardView:
    def __init__(self, board):
        self.board = board

    def update_view(self):
        print(self.board)
        return self.board
