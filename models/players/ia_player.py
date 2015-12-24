# -*- coding:utf-8 -*-

class IAPlayer:
    MIN_VALUE = -1000
    MAX_VALUE = 1000

    def __init__(self, color):
        self.color = color

    def play(self, board):
        print('minMax_player')
        return self.get_best_move(board, board.valid_moves(self.color), self.color, 3)

    def get_best_move(self, board, moves, player_color, max_depth):
        return self.min_max(board, moves, player_color, max_depth, 0)[1]

    def min_max(self, board, moves, player_color, max_depth, actual_depth):

        if len(moves) == 0:
            return [IAPlayer.MAX_VALUE, None] if actual_depth % 2 == 0 else [IAPlayer.MIN_VALUE, None]
        elif len(moves) == 1:
            return [self.board_score_by_heuristic_function(board, player_color), moves[0]]
        elif actual_depth == max_depth:
            return [self.board_score_by_heuristic_function(board, player_color), None]
        else:
            init = 0
            move_candidate = [IAPlayer.MIN_VALUE, None] if actual_depth % 2 == 0 else [IAPlayer.MAX_VALUE, None]

            for move in moves:
                clone_board = board.get_clone()
                clone_board.play(move, player_color)
                score = self.board_score_by_heuristic_function(clone_board, player_color)
                if init == 0:
                    move_candidate = [score, move]
                    init += 1

                valid_moves = clone_board.valid_moves(board.opponent(player_color))
                recursive_move = self.min_max(clone_board, valid_moves, board.opponent(player_color), max_depth,
                                              actual_depth + 1)

                move_candidate = [recursive_move[0], move] if (actual_depth % 2 == 0 and recursive_move[0] >
                                                               move_candidate[0]) or (
                    actual_depth % 2 == 1 and recursive_move[
                        0] < move_candidate) else move_candidate
        return move_candidate

    def board_score_by_heuristic_function(self, board, player_color):
        white = 0
        black = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if board.board[i][j] == board.WHITE:
                    white += self.heuristic([i, j])
                elif board.board[i][j] == board.BLACK:
                    black += self.heuristic([i, j])
        return black if player_color == board.BLACK else white

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
                [0, 100, 2, 8, 3, 3, 8, 2, 100]][move[0]][
            ove[1]]
