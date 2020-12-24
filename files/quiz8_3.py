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
    
    def en(self):
        l = str(input("Enter a result: "))
        a,fun,b = l.split(" ")
        print(a)
        if fun == 'won':
            a.won(b)
        elif fun == 'drew':
            a.drew(b)
        elif fun == 'losed':
            a.lose(b)
    
    # def show(self):
    def get_short_name(self):
        return self.__short_name

        
        
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
    
    
class Read_file:
    def __init__(self):
        self.team = []
    def read(self):
        self.team = []
        f = "Tname.txt"
        # file = input("Please enter a file name: ")
        file = f
        line = open(file).read().splitlines()
        team_all = [x.split(",") for x in  line if x != ""]
        for t in team_all:
            # team[0] = Football(team[0],team[1])
            self.team.append(Football(t[0],t[1]))
        return  self.team

    def show(self):
        for t in self.team :
            print(t)

    def en(self):
        l = str(input("Enter a result: "))
        a,fun,b = l.split(" ")
        for  name in self.team:
            
            if name.get_short_name() == a:
                aa = name
            if name.get_short_name() == b:
                bb = name
        if fun == 'won':
            aa.won(bb)
        elif fun == 'drew':
            aa.drew(bb)
        elif fun == 'losed':
            aa.losed(bb)
                       


read = Read_file()
read.read()
run = True
while run :
    print("Menu:")
    try:
        enter = str(input("(s)how summary (e)nter results (q)uit: ")).lower()
    except:
        print("ERROR")
        continue
    if enter == 's':
        read.show()
    elif enter == 'e':
        read.en()
    elif enter == 'q':
        break
    