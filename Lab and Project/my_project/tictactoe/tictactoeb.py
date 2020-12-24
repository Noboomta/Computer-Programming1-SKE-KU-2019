import pygame
from gridb import *

'''
1.DRAW BOARD
2.PLACE X or O
3.CHECK WINNER
LOOP STEP 1-3
'''

SQUARESIZE =100
NUM_ROWS = 3
NUM_COLS = 3

WIDTH = (NUM_COLS+1)*SQUARESIZE
HEIGHT = NUM_ROWS*SQUARESIZE

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption('Tic-Tac-Toe')
font = pygame.font.SysFont("comicsans", 20, True)

# font = pygame.font.SysFont('Tahoma', 60, True, False)
# text = font.render('Hello world', True, (0, 0, 0))

# screen = pygame.display.set_mode((1000, 1000))
WHITE = pygame.Color(255, 255, 255)
# RED = pygame.Color(255, 0, 0) 

board = grid()
# board.draw(screen)
# pygame.display.update()

def xy(posx,posy):
    if posx in range(0,100):x = 0
    elif posx in range(100,200):x = 1
    elif posx in range(200,300):x = 2
    elif posx in range(300,400):x = 3
    if posy in range(0,100):y = 0
    elif posy in range(100,200):y = 1
    elif posy in range(200,300):y = 2
    return x,y

run = True
player = 'X'

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not board.get_game_over():
            if pygame.mouse.get_pressed()[0]:
            # print(pygame.mouse.get_pressed())
                posx,posy = pygame.mouse.get_pos()
                print(posx,posy)
                indexx,indexy = xy(posx,posy)
                print(indexx,indexy)
                board.get_mouse(indexx,indexy,player)
                
                
                board.check_grid(player)
                
                # if board.get_winner != 'None':
                #     if board.get_winner == player:
                        
                
                if board.get_switch_player() == True and board.get_game_over() != True:
                    if player=='X':
                        player = 'O'
                    else: 
                        player = 'X'
                board.print_grid()
        if event.type == pygame.KEYDOWN  and board.get_game_over():
            if event.key == pygame.K_SPACE:
                board.clear_grid()
                board.game_over = False
                board.winner = 'None'
                player = 'X'
            
    screen.fill((0, 0, 0))
    if board.get_game_over() or board.is_grid_full():
        # text = font.render(board.get_winner() + ' wins!', 1, (255,255,255))
        # screen.blit(text, (WIDTH-int(SQUARESIZE*0.75),int(HEIGHT/2)))
        if board.get_winner() == 'None':
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