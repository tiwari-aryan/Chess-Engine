import pygame
from const import *


class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.initial_row = 0
        self.initial_column = 0

    def update_piece(self, surface):
        self.piece.set_image(size=128)
        image_file = self.piece.image
        image = pygame.image.load(image_file)
        image_center = self.mouse_x, self.mouse_y
        self.piece.image_rect = image.get_rect(center=image_center)
        surface.blit(image, self.piece.image_rect)

    def update_mouse(self, pos):
        self.mouse_x, self.mouse_y = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQUARE_SIZE
        self.initial_column = pos[0] // SQUARE_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self, piece):
        self.piece = None
        self.dragging = False
