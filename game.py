import pygame

from const import *
from board import Board
from dragger import Dragger
from square import Square


class Game:
    def __init__(self):
        self.next_player = "white"
        self.hovered_square = None
        self.board = Board()
        self.dragger = Dragger()

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
                    if piece is not self.dragger.piece:
                        piece.set_image(size=80)
                        image = pygame.image.load(piece.image)
                        image_center = (
                            column * SQUARE_SIZE + SQUARE_SIZE // 2,
                            row * SQUARE_SIZE + SQUARE_SIZE // 2,
                        )
                        piece.image_rect = image.get_rect(center=image_center)
                        surface.blit(image, piece.image_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                colour = (
                    (200, 100, 100)
                    if move.final.row + move.final.column % 2 == 0
                    else (200, 70, 70)
                )
                square = pygame.Rect(
                    move.final.column * SQUARE_SIZE,
                    move.final.row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                )
                pygame.draw.rect(surface, colour, square)

    def show_last_move(self, surface):
        if self.board.last_move:
            initial_position = self.board.last_move.initial
            final_position = self.board.last_move.final
            for position in [initial_position, final_position]:
                colour = (
                    (244, 247, 116)
                    if position.row + position.column % 2 == 0
                    else (172, 195, 51)
                )
                square = pygame.Rect(
                    position.column * SQUARE_SIZE,
                    position.row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                )
                pygame.draw.rect(surface, colour, square)

    def show_hover(self, surface):
        if self.hovered_square:
            colour = (180, 180, 180)
            square = (
                self.hovered_square.column * SQUARE_SIZE,
                self.hovered_square.row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE,
            )
            pygame.draw.rect(surface, colour, square, width=3)

    def next_turn(self):
        self.next_player = "white" if self.next_player == "black" else "black"

    def set_hover(self, row, column):
        self.hovered_square = self.board.squares[row][column]
