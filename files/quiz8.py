class Football:
    
    def __init__(self,short_name, full_name, win = 0, draw = 0, lose = 0):
        self.__short_name = short_name
        self.__full_name = full_name
        self.__win = win
        self.__draw = draw
        self.__lose = lose
    
    def __str__(self):
        return f'#{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}'
    
    @property
    def win(self):
        self.__win 
    @win.setter
    def win(self,newwin):
        self.__win = newwin
    
    @property
    def draw(self):
        self.__draw 
    @draw.setter
    def draw(self,newdraw):
        self.__draw = newdraw
    
    @property
    def lose(self):
        self.__lose
    @lose.setter
    def lose(self,newlose):
        self.__lose = newlose
        
    
ARS = Football("ARS","Arsenal")
print(ARS)
ARS.win = 1
print(ARS)
ARS.draw = 4
print(ARS)
ARS.lose = 2
print(ARS)

LIV = Football("LIV","Liverpool",1,3,4)
print(LIV)
LIV.win = 3
print(LIV)
LIV.draw = 1
print(LIV)
LIV.lose = 6
print(LIV)

