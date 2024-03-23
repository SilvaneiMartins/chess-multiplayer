import pygame
import os

board = pygame.image.load(os.path.join("img", "board_alt.png"))

b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale2x(img))

for img in w:
    W.append(pygame.transform.scale2x(img))


def redraw_gameWindow():
    global win
    win.blit(board, (0, 0))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(10)

        redraw_gameWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Xadrez Multiplayer Online")
main()
