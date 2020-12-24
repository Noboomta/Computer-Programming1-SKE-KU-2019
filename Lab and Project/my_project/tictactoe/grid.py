import pygame
import os

SQUARESIZE = 100
NUM_ROWS = 3
NUM_COLS = 3

path = 'C:/Users/NoBoomTa/Desktop/python/vs pyt00001/my_project/tictactoe/'
letter_x = pygame.image.load(os.path.join(path, 'x.png'))
letter_o = pygame.image.load(os.path.join(path, 'o.png'))

class grid:
    def __init__(self):
        self.__grid_lines = [((0, 100), (300, 100)), 
                             ((0, 200), (300, 200)), 
                             ((100, 0), (100, 300)), 
                             ((200, 0), (200, 300)),
                             ((300, 0), (300, 300))]
        self.__grid = [[0 for x in range(3)]for y in range(3)]
        self.switch_player = True
        self.game_over = False
        self.winner = None

    def draw(self, screen):
        for line in self.__grid_lines:
            pygame.draw.line(screen, (255, 255, 255), line[0], line[1], 2)
        for y in range(len(self.__grid)):
            for x in range(len(self.__grid[y])):
                if self.get_cell_value(x, y) == 'X':
                    screen.blit(letter_x, (x*SQUARESIZE, y*SQUARESIZE))
                elif self.get_cell_value(x, y) == 'O':
                    screen.blit(letter_o, (x*SQUARESIZE, y*SQUARESIZE))

    def print_grid(self):
        for row in self.__grid:
            print(row)

    def get_cell_value(self, x, y):
        try:
            return self.__grid[y][x]
        except:
            pass

    def set_cell_value(self, x, y, value):
        self.__grid[y][x] = value

    def get_mouse(self, x, y, player):
        if self.get_cell_value(x, y) == 0:
            self.switch_player = True
            if player == 'X':
                self.set_cell_value(x, y, 'X')
            elif player == 'O':
                self.set_cell_value(x, y, 'O')
        else:
            self.switch_player = False

    def get_switch_player(self):
        return self.switch_player

    def is_grid_full(self):
        for row in self.__grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def check_three(self, n): #For check_grid.
        if n == 3:
            self.game_over = True
            return True

    def check_grid(self, player):
        _win = bool

        for y in self.__grid:
            _num = 0
            for x in y:
                if x == player:
                    _num += 1
            self.check_three(_num)
            if self.check_three(_num): _win = True

        for i in range(len(self.__grid[0])):
            _num = 0
            for y in self.__grid:
                if y[i] == player:
                    _num += 1
            self.check_three(_num)
            if self.check_three(_num): _win = True

        i = 0
        _num = 0
        for y in self.__grid:
            if y[i] == player:
                _num += 1
            i += 1
        self.check_three(_num)
        if self.check_three(_num): _win = True

        i = 2
        _num = 0
        for y in self.__grid:
            if y[i] == player:
                _num += 1
            i -= 1
        self.check_three(_num)
        if self.check_three(_num): _win = True

        if not (_win):
            if self.is_grid_full():
                #print("Full board")
                _win = False
                self.check_three(3)
            else:
                _win = True

        if _win == True:
            self.winner = player
        else:
            self.winner = None

    def clear_grid(self):
        for y in range(len(self.__grid)):
            for x in range(len(self.__grid)):
                self.__grid[y][x] = 0