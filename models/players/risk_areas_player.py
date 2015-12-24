# -*- coding:utf-8 -*-

class BoardValuePlayer:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.best_value(board.valid_moves(self.color))

    def best_value(self, moves):
        ret_move_value = -50

        for move in moves:
            if self.heuristic(move) > ret_move_value:
                ret_move_value = move_candidate
                move_candidate = move
        return move_candidate

    @staticmethod
    def heuristic(move):
        value_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, ]
                        [0, 200, -20, 20, 5, 5, 20, -20, 200],
                        [0, -20, -40, -5, -5, -5, -5, -40, -20],
                        [0, 20, -5, 15, 3, 3, 15, -5, 20],
                        [0, 5, -5, 3, 3, 3, 3, -5, 5],
                        [0, 5, -5, 3, 3, 3, 3, -5, 5],
                        [0, 20, -5, 15, 3, 3, 15, -5, 20],
                        [0, -20, -40, -5, -5, -5, -5, -40, -20],
                        [0, 200, -20, 20, 5, 5, 20, -20, 200]]

        return value_matrix[move.x][move.y]
