import pygame

from const import *


class Game:
    def __init__(self):
        pass

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
