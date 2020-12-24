import pygame
import os

SQUARESIZE =100
NUM_ROWS = 3
NUM_COLS = 3

WIDTH = (NUM_COLS+1)*SQUARESIZE
HEIGHT = NUM_ROWS*SQUARESIZE

path = 'C:/Users/NoBoomTa/Desktop/python/vs pyt00001/my_project/tictactoe/'
letter_x = pygame.image.load(os.path.join(path, 'x.png'))
letter_o = pygame.image.load(os.path.join(path, 'o.png'))

class grid:
    def __init__(self):
        self.__grid_line = [ ((0,100), (300,100)) , ((0,200),(300,200)) , ((100,0),(100,300)) , ((200,0),(200,300)), ((300,0),(300,300))]
        self.__grid = [ ['0' for x in range(3)] for y in range(3) ]
        self.switch_player = True
        self.game_over = False
        self.winner = 'None'
    
    def draw(self,screen):
        for line in self.__grid_line:
            pygame.draw.line(screen, (0,255,0), line[0], line[1], 2)
        
        for y in range(len(self.__grid)):
            for x in  range(len(self.__grid[y])):
                if self.get_cell_value(x,y) == 'X':
                    screen.blit(letter_x,(x*SQUARESIZE,y*SQUARESIZE))
                elif self.get_cell_value(x,y) == 'O':
                    screen.blit(letter_o,(x*SQUARESIZE,y*SQUARESIZE))
        
    def print_grid(self):
        for row in self.__grid:
            print(row)
            
    def is_grid_full(self):
        for row in  self.__grid:
            for value in row:
                if value == '0':
                    return False
        return True

    def check_grid(self,player):
        
        for i in range(3):
            row = 0
            for y in self.__grid:
                if y[i] == player:
                    row+=1
            if row == 3:
                self.game_over = True
                self.winner = player
                break
            
        for i in range(3):     
            for y in self.__grid:
                column = 0
                for i in y:
                    if i == player:
                        column+=1
                if column == 3:
                    self.game_over = True
                    self.winner = player
                    break
        
        leftdown_to_righttop = 0     
        for i in range(3):
            for j in range(3):
                if i+j == 2 :
                    if self.__grid[i][j] == player:
                        leftdown_to_righttop += 1
        if leftdown_to_righttop == 3:
            self.game_over = True
            self.winner = player
            
        rightdown_to_lefttop = 0
        for i in range(3):
            for j in range(3):
                if i==j :
                    if self.__grid[i][j] == player:
                        rightdown_to_lefttop += 1
        if rightdown_to_lefttop == 3:
            self.game_over = True
            self.winner = player
            
        if self.is_grid_full() and self.winner == 'None':
            self.game_over = True
            
            
    def get_winner(self):
        return self.winner
    
    def get_game_over(self):
        return self.game_over
    
    def set_winner(self, value):
         
        self.winner = value
        
    def set_game_over(self, value):
        self.game_over = value
        
    def clear_grid(self):
        print("CLEAR GRID")
        for y in range(len(self.__grid)):
            for x in range(len(self.__grid)):
                self.__grid[y][x] = '0'
        
            
    def get_cell_value(self,x,y):
        return self.__grid[y][x]        
    
    def set_cell_value(self,x,y,value):
        self.__grid[y][x] = value
    
    def get_switch_player(self):
        return self.switch_player
    
    def get_mouse(self,x,y,player):
        if self.get_cell_value(x,y) == "0":
            self.switch_player = True
            if player == 'X':
                self.set_cell_value(x,y,'X')
            elif player == 'O':
                self.set_cell_value(x,y,'O')
            self.check_grid(player)
        else:   self.switch_player = False
            
