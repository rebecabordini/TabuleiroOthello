# -*- coding:utf-8 -*-

class MinMaxPlayer:
    BLACK, WHITE = '@', 'o'

    def __init__(self, color):
        self.color = color

    def play(self, board):
        print('minMax_player')
        return self.get_best_move(board, board.valid_moves(self.color), self.color, 3)

    def get_best_move(self, board, moves, player_color, max_depth):
        return self.min_max(board, moves, player_color, max_depth, 0)[1]

    def min_max(self, board, moves, player_color, max_depth, actual_depth):

        if len(moves) == 0:
            if actual_depth % 2 == 0:
                return [10000, None]
            else:
                return [-10000, None]
        elif len(moves) == 1:
            return [self.board_score(board, player_color), moves[0]]

        elif actual_depth == max_depth:
            return [self.board_score(board, player_color), None]

        else:
            init = 0

            if actual_depth % 2 == 0:
                ret_move = [-10000, None]
            else:
                ret_move = [10000, None]

            for move in moves:

                clone_board = board.get_clone()
                clone_board.play(move, player_color)
                next_moves = clone_board.valid_moves(self._opponent(player_color))

                score = self.board_score(clone_board, player_color)
                if init == 0:
                    ret_move = [score, move]
                    init += 1

                recursive_move = self.min_max(clone_board, next_moves, self._opponent(player_color), max_depth,
                                              actual_depth + 1)

                if actual_depth % 2 == 0:
                    if recursive_move[0] > ret_move[0]:
                        ret_move[0] = recursive_move[0]
                        ret_move[1] = move
                else:
                    if recursive_move[0] < ret_move:
                        ret_move[0] = recursive_move[0]
                        ret_move[1] = move

        return ret_move

    @staticmethod
    def _opponent(color):
        return MinMaxPlayer.WHITE if color == MinMaxPlayer.BLACK else MinMaxPlayer.BLACK

    def board_score(self, board, player_color):
        white = 0
        black = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if board.board[i][j] == MinMaxPlayer.WHITE:
                    white += self.heuristic([i, j])
                elif board.board[i][j] == MinMaxPlayer.BLACK:
                    black += self.heuristic([i, j])
        if player_color == MinMaxPlayer.BLACK:
            score = black
        else:
            score = white

        return score

    @staticmethod
    def heuristic(move):
        return [[0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                [0, 100, 2, 8, 3, 3, 8, 2, 100],
                [0, 2, 1, 7, 4, 4, 7, 1, 2],
                [0, 8, 7, 9, 5, 5, 9, 7, 8],
                [0, 3, 4, 5, 0, 0, 5, 4, 3],
                [0, 3, 4, 5, 0, 0, 5, 4, 3],
                [0, 8, 7, 9, 5, 5, 9, 7, 8],
                [0, 2, 1, 7, 4, 4, 7, 1, 2],
                [0, 100, 2, 8, 3, 3, 8, 2, 100]][move[0]][move[1]]
