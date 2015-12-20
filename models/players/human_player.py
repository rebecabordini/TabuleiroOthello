# -*- coding:utf-8 -*-

from models.move import Move

class HumanPlayer:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        row_input = int(raw_input("Linha: "))
        column_input = int(raw_input("Coluna: "))
        move = Move(row_input, column_input)
        while move not in board.valid_moves(self.color):
            print("Movimento invalido.Insira um valido")
            print(board)
            row_input = int(raw_input("Linha: "))
            column_input = int(raw_input("Coluna: "))
            move = Move(row_input, column_input)
        return move
