class Football:
    
    def __init__(self,short_name, full_name, win = 0, draw = 0, lose = 0):
        self.__short_name = short_name
        self.__full_name = full_name
        self.__win = win
        self.__draw = draw
        self.__lose = lose
    
    def __str__(self):
        return f'#{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}'
    
    def won(self,team):
        self.__win += 1
        team.__lose += 1
        
    def drew(self,team):
        self.__draw += 1
        team.__draw += 1
    
    def losed(self,team):
        self.__lose += 1
        team.__win += 1
        
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
LIV = Football("LIV","Liverpool")
print(ARS)
print(LIV)

ARS.won(LIV)
print(ARS)
print(LIV)

LIV.drew(ARS)
print(ARS)
print(LIV)

ARS.losed(LIV)
print(ARS)
print(LIV)

print()

''' THE BEST TEAM ON THE WORLD'''
CHE = Football("CHE","Chelsea") 
MUN = Football("MUN","Manchester Unites")
MCI = Football("MCI","Manchester City")
print(CHE)
print(MUN)
print(MCI)

MCI.losed(CHE)
print(CHE)
print(MUN)
print(MCI)

MUN.won(MCI)
print(CHE)
print(MUN)
print(MCI)