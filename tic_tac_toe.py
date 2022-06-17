import pygame
import sys
import numpy as np
from math import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
import game_board as gb
# import draw_x_and_o as
from draw_shapes import *
from draw_win_line import *
import check_win as cw
import game_logic as gl
import screen as sc

# initializes pygame
pygame.init()
textfont=pygame.font.SysFont('monospace',35)

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def draw_figures(index, row, col):
    if board[index] == 'O':

        draw_cicle(row, col)
        return
    elif board[index] == 'X':

        draw_x(row, col)
        return


def restart():
    sc.screen.fill(BG_COLOR)
    gb.draw_lines()
    for row in range(len(board)):
        # for col in range(BOARD_COLS):
        board[row] = row


gb.draw_lines()

player = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            col = int((mouseX + SQUARE_SIZE) // SQUARE_SIZE)
            if (player % 2 == 1):
                gamer = 1
            else:
                gamer = 2
            index = gl.logic(board, clicked_row, col, gamer)
            textTBD2 = textfont.render("press 'r' to restart ", 1, (0, 0, 255))

            if (cw.checkWin(board, gamer) == True):
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


                if (gamer == 1):
                    textTBD = textfont.render("congradulation,player1 win", 1, (0, 0, 255))
                elif(gamer == 2):
                    textTBD = textfont.render("congradulation,player2 win", 1, (0, 0, 255))

                sc.screen.blit(textTBD,(50,200))
                sc.screen.blit(textTBD2, (90, 240))
                game_over = True


            elif (cw.checkWin(board, gamer) == 'draw' and all(map(lambda x: isinstance(x, str), board))):
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                textTBD = textfont.render("the game ends with draw", 1, (0, 0, 255))
                sc.screen.blit(textTBD, (50, 200))
                sc.screen.blit(textTBD2, (90, 240))
                game_over = True
            # else:
            #     textTBD = textfont.render("no win", 1, (255, 255, 255))
            #     sc.screen.blit(textTBD, (100, 100))
            #     game_over = True
            draw_figures(index, clicked_row, clicked_col)
            player = player + 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()

