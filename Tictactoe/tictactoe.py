import pygame
from grid import *

squaresizw = 100
num_rows = 3
num_cols = 3

width = (num_cols+1)*squaresizw
height = num_rows*squaresizw

pygame.init()
screen = pygame.display.set_mode([width,height])

pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.SysFont("comicsans",20,True)

board = grid()
run = True
player = "X"

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not board.get_game_over():
            # print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                board.get_mouse(pos[0]//100,pos[1]//100,player)
                # if board.get_switch_player() == True:
                #     if player == "X":
                #         player = "O"
                #     else:
                #         player = "X"
                # board.print_grid()
                x,y =0,0
                board.check_grid(x,y,player)
                if board.get_switch_player() == True and board.get_game_over() != True:
                    if player=='X':
                        player = 'O'
                    else: 
                        player = 'X'
                board.print_grid()
                    
        if event.type == pygame.KEYDOWN  and board.get_game_over() :
            if event.key == pygame.K_SPACE:
                board.clear_grid()
                board.game_over = False
                board.winner = 'None'
                player = "x"
        
        

    screen.fill((0,0,0))    
    if board.get_game_over() or board.is_grid_full():
        if board.get_winner() == "None":
            text = font.render('tie!!', 1, (255, 255, 255))
            screen.blit(text, (width - int(squaresizw*0.75) + 10, int(height/2) - 8))
            text = font.render('press SPACE', 1, (255, 255, 255))
            screen.blit(text, (width - int(squaresizw*0.75) - 21, int(height/2) + 8))
        
        else:
            text = font.render(board.winner + "Wins!",1,(255,255,255))
            screen.blit(text,(width-int(squaresizw*0.75),int(height/2) - 8)) 
            text = font.render('press SPACE', 1, (255, 255, 255))
            screen.blit(text, (width - int(squaresizw*0.75) - 21, int(height/2) + 8))
            
    board.draw(screen)
    pygame.display.update()

pygame.quit()