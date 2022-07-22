import os
from math import inf


class Piece:
    def __init__(self, name, colour, value, image=None, image_rect=None):
        self.name = name
        self.colour = colour
        value_sign = 1 if colour == "white" else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.image = image
        self.set_image()
        self.image_rect = image

    def set_image(self, size=80):
        self.image = os.path.join(
            f"assets/images/imgs-{size}px/{self.colour}_{self.name}.png"
        )

    def add_moves(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []


class Pawn(Piece):
    def __init__(self, colour):
        self.dir = -1 if colour == "white" else 1
        super().__init__("pawn", colour, 1.0)


class Knight(Piece):
    def __init__(self, colour):
        super().__init__("knight", colour, 3.0)


class Bishop(Piece):
    def __init__(self, colour):
        super().__init__("bishop", colour, 3.0)


class Rook(Piece):
    def __init__(self, colour):
        super().__init__("rook", colour, 5.0)


class Queen(Piece):
    def __init__(self, colour):
        super().__init__("queen", colour, 9.0)


class King(Piece):
    def __init__(self, colour):
        super().__init__("king", colour, inf)
