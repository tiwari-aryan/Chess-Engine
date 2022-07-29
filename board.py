from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self):
        self.squares = [[0 for _ in range(COLS)] for _ in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def move(self, piece, move):
        initial_position = move.initial
        final_position = move.final

        self.squares[initial_position.row][initial_position.column].piece = None
        self.squares[final_position.row][final_position.column].piece = piece

        if isinstance(piece, Pawn):
            self.check_promotion(piece, final_position)

        if isinstance(piece, King):
            if self.castling(initial_position, final_position):
                diff = final_position.column - initial_position.column
                rook = piece.left_rook if diff < 0 else piece.right_rook
                self.move(rook, rook.moves[-1])

        piece.moved = True

        piece.clear_moves()

        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.moves

    def check_promotion(self, piece, final_position):
        if final_position.row == 0 or final_position.row == 7:
            self.squares[final_position.row][final_position.column].piece = Queen(
                piece.colour
            )

    def castling(self, initial_position, final_position):
        return abs(initial_position.column - final_position.column) == 2

    def calc_moves(self, piece, row, column):
        def pawn_moves():
            steps = 1 if piece.moved else 2

            start = row + piece.dir
            end = row + (piece.dir * (steps + 1))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    possible_move_square = self.squares[possible_move_row][column]
                    if possible_move_square.is_empty():
                        initial_position = Square(row, column)
                        final_position = Square(possible_move_row, column)
                        move = Move(initial_position, final_position)
                        piece.add_moves(move)
                    else:
                        break
                else:
                    break

            possible_move_row = row + piece.dir
            possible_move_columns = [column - 1, column + 1]
            for possible_move_column in possible_move_columns:
                if Square.in_range(possible_move_row, possible_move_column):
                    possible_move_square = self.squares[possible_move_row][
                        possible_move_column
                    ]
                    if possible_move_square.has_rival_piece(piece.colour):
                        initial_position = Square(row, column)
                        final_position = Square(possible_move_row, possible_move_column)
                        move = Move(initial_position, final_position)
                        piece.add_moves(move)

        def knight_moves():
            possible_moves = [
                (row - 2, column + 1),
                (row - 2, column - 1),
                (row + 2, column + 1),
                (row + 2, column - 1),
                (row - 1, column + 2),
                (row - 1, column - 2),
                (row + 1, column + 2),
                (row + 1, column - 2),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_column = possible_move
                if Square.in_range(possible_move_row, possible_move_column):
                    possible_move_square = self.squares[possible_move_row][
                        possible_move_column
                    ]
                    if possible_move_square.is_empty_or_rival(piece.colour):
                        initial_position = Square(row, column)
                        final_position = Square(possible_move_row, possible_move_column)
                        move = Move(initial_position, final_position)
                        piece.add_moves(move)

        def straightline_moves(increments):
            possible_moves = []
            for increment in increments:
                row_increment, column_increment = increment
                possible_move_row = row + row_increment
                possible_move_column = column + column_increment
                while True:
                    if Square.in_range(possible_move_row, possible_move_column):
                        possible_move_square = self.squares[possible_move_row][
                            possible_move_column
                        ]
                        initial_position = Square(row, column)
                        final_position = Square(possible_move_row, possible_move_column)
                        move = Move(initial_position, final_position)
                        if possible_move_square.is_empty():
                            piece.add_moves(move)

                        if possible_move_square.has_rival_piece(piece.colour):
                            piece.add_moves(move)
                            break
                        if possible_move_square.has_team_piece(piece.colour):
                            break
                    else:
                        break
                    possible_move_row += row_increment
                    possible_move_column += column_increment

        def king_moves():
            possible_moves = [
                (row + 1, column),
                (row - 1, column),
                (row, column - 1),
                (row, column + 1),
                (row + 1, column + 1),
                (row + 1, column - 1),
                (row - 1, column - 1),
                (row - 1, column + 1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_column = possible_move
                if Square.in_range(possible_move_row, possible_move_column):
                    move_square = self.squares[possible_move_row][possible_move_column]
                    if move_square.is_empty_or_rival(piece.colour):
                        initial_position = Square(row, column)
                        final_position = Square(possible_move_row, possible_move_column)
                        move = Move(initial_position, final_position)
                        piece.add_moves(move)

            if not piece.moved:
                left_rook = self.squares[row][0].piece
                castling = True
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            if self.squares[row][c].has_piece():
                                castling = False
                        if castling == True:
                            piece.left_rook = left_rook
                            initial_position = Square(row, 0)
                            final_position = Square(row, 3)
                            move = Move(initial_position, final_position)
                            left_rook.add_moves(move)
                            initial_position = Square(row, column)
                            final_position = Square(row, 2)
                            move = Move(initial_position, final_position)
                            piece.add_moves(move)

                right_rook = self.squares[row][7].piece
                castling = True
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            if self.squares[row][c].has_piece():
                                castling = False
                        if castling == True:
                            piece.right_rook = right_rook
                            initial_position = Square(row, 7)
                            final_position = Square(row, 5)
                            move = Move(initial_position, final_position)
                            right_rook.add_moves(move)
                            initial_position = Square(row, column)
                            final_position = Square(row, 6)
                            move = Move(initial_position, final_position)
                            piece.add_moves(move)

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            straightline_moves([(1, -1), (-1, -1), (-1, 1), (1, 1)])
        elif isinstance(piece, Rook):
            straightline_moves([(1, 0), (0, 1), (-1, 0), (0, -1)])
        elif isinstance(piece, Queen):
            straightline_moves(
                [(1, -1), (-1, -1), (-1, 1), (1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
            )
        elif isinstance(piece, King):
            king_moves()

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
        self.squares[others][6] = Square(others, 6, Knight(colour))

        # Adding the bishops
        self.squares[others][2] = Square(others, 2, Bishop(colour))
        self.squares[others][5] = Square(others, 5, Bishop(colour))

        # Adding the rooks
        self.squares[others][0] = Square(others, 0, Rook(colour))
        self.squares[others][7] = Square(others, 7, Rook(colour))

        # Adding the queen
        self.squares[others][3] = Square(others, 3, Queen(colour))

        # Adding the king
        self.squares[others][4] = Square(others, 4, King(colour))
