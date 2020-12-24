import pygame

squaresizw = 100
num_rows = 3
num_cols = 3

width = (num_cols+1)*squaresizw
height = num_rows*squaresizw

letter_x = pygame.image.load("x.png")
letter_o = pygame.image.load("o.png")

class grid:
    def __init__(self):
        self.__grid_lines = [((0,100),(300,100)),((0,200),(300,200)),((100,0),(100,300)),((200,0),(200,300)),((300,0),(300,300))]
        self.__grid = [['0' for x in range(3)] for y in range(3)]
        self.switch_player = True
        self.game_over = False
        self.winner = "None"

    def draw(self,screen):
        for line in self.__grid_lines:
            pygame.draw.line(screen,(255,255,255),line[0],line[1],2)

        for y in range(len(self.__grid)):
            for x in range(len(self.__grid[y])):
                if self.get_cell_value(x,y) == "X":
                    screen.blit(letter_x,(x*squaresizw,y*squaresizw))
                elif self.get_cell_value(x,y) == "O":
                    screen.blit(letter_o,(x*squaresizw,y*squaresizw))

    def print_grid(self):
        for row in self.__grid:
            print(row)
    
    def get_cell_value(self,x,y):
        return self.__grid[y][x]

    def set_cell_value(self,x,y,value):
        self.__grid[y][x] = value

    def get_mouse(self,x,y,player):
        if self.get_cell_value(x,y) == '0':
            self.switch_player = True
            if player == "X":
                self.set_cell_value(x,y,"X")
            elif player == "O":
                self.set_cell_value(x,y,"O")
            self.check_grid(x,y,player)
        else:
            self.switch_player = False

    def get_switch_player(self):
        return self.switch_player

    def is_grid_full(self):
        for row in self.__grid:
            for value in row:
                if value == "0" :
                    return False
        return True
    
    def check_grid(self,x,y,player):
        for y in range(3):
            h = 0
            v = 0
            for x in range(3):
                if self.__grid[y][x] == player:
                    h+=1
                if self.__grid[x][y] == player:
                    v+=1
            if h == 3 or v == 3:
                self.game_over = True
                self.winner = player
        
        a=0
        for y in range(3):
            for x in range(3):
                if x==y and self.__grid[y][x] == player:
                    a+=1
        if a==3:
            self.game_over = True
            self.winner = player

        b=0
        for x in range(3):
            for y in range(3):
                if x+y==2 and self.__grid[y][x] == player:
                    b+=1
        if b==3:
            self.game_over = True
            self.winner = player

        if self.is_grid_full() and self.winner == "None":
            print("FULL!!")
            self.game_over == True      
    
    def get_winner(self):
        return self.winner

    def get_game_over(self):
        return self.game_over

    def set_winner(self,value):
        self.winner = value

    def set_game_over(self,value):
        self.game_over = value
    
    def clear_grid(self):
        print("Clear!!")
        for y in range(3):
            for x in range(3):
                self.__grid[y][x] = '0'