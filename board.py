from const import *
from square import Square
from piece import *


class Board:
    def __init__(self):
        self.squares = [[0 for _ in range(COLS)] for _ in range(COLS)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def _create(self):
        for row in range(ROWS):
            for column in range(COLS):
                self.squares[row][column] = Square(row, column)

    def _add_pieces(self, colour):
        pawns, others = (6, 7) if colour == "white" else (1, 0)

        # Adding the pawns
        for column in range(COLS):
            self.squares[pawns][column] = Square(pawns, column, Pawn(colour))

        # Adding the knights
        self.squares[others][1] = Square(others, 1, Knight(colour))
        self.squares[others][6] = Square(others, 1, Knight(colour))

        # Adding the bishops
        self.squares[others][2] = Square(others, 1, Bishop(colour))
        self.squares[others][5] = Square(others, 1, Bishop(colour))

        # Adding the rooks
        self.squares[others][0] = Square(others, 1, Rook(colour))
        self.squares[others][7] = Square(others, 1, Rook(colour))

        # Adding the queen
        self.squares[others][3] = Square(others, 1, Queen(colour))

        # Adding the king
        self.squares[others][4] = Square(others, 1, King(colour))
