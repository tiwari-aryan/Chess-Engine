import pygame
import sys

from const import *
from game import Game


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Engine")

        self.game = Game()

    def main_loop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_piece(screen)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouse_y // SQUARE_SIZE
                    clicked_column = dragger.mouse_x // SQUARE_SIZE

                    if board.squares[clicked_row][clicked_column].has_piece():
                        piece = board.squares[clicked_row][clicked_column].piece
                        board.calc_moves(piece, clicked_row, clicked_column)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging is True:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_piece(screen)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if board.squares[clicked_row][clicked_column].has_piece():
                        dragger.undrag_piece(piece)
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            pygame.display.flip()


main = Main()
main.main_loop()
