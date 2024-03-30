import pygame
import os

from board import Board
from piece import Bishop

board = pygame.transform.scale(pygame.image.load(os.path.join("img", "board_alt.png")), (780, 780))
rect = (115, 115, 550, 550)

def redraw_gameWindow():
    global win, bo

    win.blit(board, (0, 0))
    bo.draw(win, bo.board)

    pygame.display.update()

def click(pos):
    """
    :return: pos(x, y) in range 0-7 7-0
    """
    x = pos[0]
    y = pos[1]

    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[0]
            i = int(divX / (rect[2] / 8))
            j = int(divY / (rect[3] / 8))
            return i, j

def main():
    global bo
    bo = Board(8, 8)
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
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                # bo.board[i][j].selected = True
                bo.select(i, j)


width = 780
height = 780

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Xadrez Multiplayer Online")
main()
