import pygame
import os

from board import Board
from piece import Bishop

board = pygame.transform.scale(pygame.image.load(os.path.join("img", "board_alt.png")), (780, 780))
rect = (115, 115, 550, 550)

def redraw_gameWindow():
    global win

    win.blit(board, (0, 0))
    bo = Board(8, 8)
    bo.draw(win)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(10)

        redraw_gameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


width = 780
height = 780

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Xadrez Multiplayer Online")
main()
