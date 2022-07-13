import pygame

from const import *
from board import Board


class Game:
    def __init__(self):
        self.board = Board()

    # Methods to show different images

    def show_bg(self, surface):
        for row in range(ROWS):
            for column in range(COLS):
                if (row + column) % 2 == 0:
                    colour = (234, 235, 200)
                else:
                    colour = (199, 154, 88)

                square = pygame.Rect(
                    column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                )
                pygame.draw.rect(surface, colour, square)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for column in range(COLS):
                if self.board.squares[row][column].has_piece():
                    piece = self.board.squares[row][column].piece

                    image = pygame.image.load(piece.image)
                    image_center = (
                        column * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    )
                    piece.image_rect = image.get_rect(center=image_center)
                    surface.blit(image, piece.image_rect)
