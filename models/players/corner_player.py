# -*- coding:utf-8 -*-

class CornerPlayer:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.get_nearest_corner(board.valid_moves(self.color))

    @staticmethod
    def get_nearest_corner(moves):
        import math

        corners = [[1, 1], [1, 8], [8, 1], [8, 8]]
        min_distance = 10
        next_move = None
        for move in moves:
            for corner in corners:
                distance_in_x_axis = abs(corner[0] - move.x)
                distance_in_y_axis = abs(corner[1] - move.y)
                dist = math.sqrt(distance_in_x_axis * distance_in_x_axis + distance_in_y_axis * distance_in_y_axis)
                if dist < min_distance:
                    min_distance = dist
                    next_move = move

        return next_move
