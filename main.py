import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move


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
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_piece(screen)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouse_y // SQUARE_SIZE
                    clicked_column = dragger.mouse_x // SQUARE_SIZE
                    piece = board.squares[clicked_row][clicked_column].piece
                    if board.squares[clicked_row][clicked_column].has_piece():
                        board.calc_moves(piece, clicked_row, clicked_column)
                        if piece.colour == game.next_player:
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                            game.show_hover(screen)
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQUARE_SIZE
                    motion_column = event.pos[0] // SQUARE_SIZE
                    if dragger.dragging is True:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_piece(screen)
                    game.set_hover(motion_row, motion_column)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouse_y // SQUARE_SIZE
                        released_column = dragger.mouse_x // SQUARE_SIZE

                        initial_position = Square(
                            dragger.initial_row, dragger.initial_column
                        )
                        final_position = Square(released_row, released_column)
                        move = Move(initial_position, final_position)
                        if board.valid_move(dragger.piece, move):
                            move_square = board.squares[released_row][released_column]
                            captured = move_square.has_piece()
                            game.play_sound(captured)
                            board.move(dragger.piece, move)
                            game.next_turn()
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            game.show_hover(screen)
                    piece.clear_moves()
                    dragger.undrag_piece(piece)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        game.change_theme()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            pygame.display.flip()


main = Main()
main.main_loop()
