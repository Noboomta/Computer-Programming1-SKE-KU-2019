import pygame
from grid import *

SQUARESIZE = 100
NUM_ROWS = 3
NUM_COLS = 4

WIDTH = NUM_COLS * SQUARESIZE
HEIGHT = NUM_ROWS * SQUARESIZE

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption('Tic-Tac-Toe')
font = pygame.font.SysFont("comicsans", 20, True)

board = grid()
run = True
player = 'X'

while run:
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not board.game_over:
            pos = pygame.mouse.get_pos()
            #print(pos[0]//100, pos[1]//100)
            board.get_mouse(pos[0]//100, pos[1]//100, player)

            board.check_grid(player)

            if not (board.game_over):
                if board.get_switch_player():
                    if player == 'X':
                        player = 'O'
                    else:
                        player = 'X'

        if event.type == pygame.KEYDOWN and board.game_over:
            if event.key == pygame.K_SPACE:
                board.clear_grid()
                board.game_over = False
                board.winner = None
                player = 'X'

    screen.fill((0, 0, 0))

    if board.game_over == True:
        if board.winner == None:
            text = font.render('tie!!', 1, (255, 255, 255))
            screen.blit(text, (WIDTH - int(SQUARESIZE*0.75) + 10, int(HEIGHT/2) - 8))
            text = font.render('press SPACE', 1, (255, 255, 255))
            screen.blit(text, (WIDTH - int(SQUARESIZE*0.75) - 21, int(HEIGHT/2) + 8))
        else:
            text = font.render(board.winner + ' win!!', 1, (255, 255, 255))
            screen.blit(text, (WIDTH - int(SQUARESIZE*0.75), int(HEIGHT/2) - 8))
            text = font.render('press SPACE', 1, (255, 255, 255))
            screen.blit(text, (WIDTH - int(SQUARESIZE*0.75) - 21, int(HEIGHT/2) + 8))
        
    board.draw(screen)
    pygame.display.update()
pygame.quit()