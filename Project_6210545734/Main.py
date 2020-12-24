import random
from datetime import date
from games.G1 import *
from games.G2 import *
from games.G3 import *
# from G3 import *

'''   No Thank  '''
'''  BlackJack  '''
'''    Mario    '''
''' master mind '''
'''   parking   '''

class Gamestat:
    def __init__(self, name):
        self.__name = name
        self.__win = 0
        self.__lose = 0
        self.__round = 0
    def add_win(self,value = 1):
        self.__win = int(self.__win) + value
    def add_lose(self,value = 1):
        self.__lose = int(self.__lose) + value
    def add_round(self,value = 1):
        self.__round = int(self.__round) + value
    def get_name(self):
        return self.__name
    def check(self,data):
        # print(data, "wow")
        if data in ['bot loose','player win','win']:
            # print('WINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
            self.add_win()
            self.add_round()
        elif data in ['bot win','player loose','lose']:
            # print('LOSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
            self.add_lose()
            self.add_round()
        elif self.__name == 'Rockpaperscissor':
            win,lose,draw = data
            self.add_win(win)
            self.add_lose(lose)
            self.add_round(draw)
        else:
            pass
            # print('NOTIN DATAAAAAAAAAAAAAAAAAAAAAAAAA')
    
    def create(self, data):
        w,l,r = data.split(':')
        self.__win = w
        self.__lose = l
        self.__round = r
            
    def __str__(self):
        return str(self.__name) + "." + str(self.__win) + ":" + str(self.__lose) + ":" + str(self.__round)

class Player:
    def __init__(self, name):
        self.__name = name
        bjstat = Gamestat('blackjack')
        ntstat = Gamestat('NoThanks')
        rpsstat = Gamestat('Rockpaperscissor')
        self.__gamelist = [bjstat,ntstat,rpsstat]
    def get_name(self):
        return self.__name
    def check(self, _data):
        # if game == 'blackjack':
        #     if result == 'bot win' or result == 'player loose':
        #         bjstat.add_lose()
        #     elif result == 'bot loose' or result == 'player win':
        #         bjstat.add_win()
        # elif game == 'NoThank':
        #     if result == 'lose':
        #         ntstat.add_lose()
        #     elif result
        for gamename, data in _data.items():
            # print(data)
            for game in self.__gamelist:      
                # print(f'GGG{game.get_name()}')
                if gamename == game.get_name():
                    game.check(data)
                    
    def create(self, stat):
        game_data = stat.split(',')
        for game in game_data:
            game_name, data = game.split('.')
            for _game in self.__gamelist:
                if game_name == _game.get_name():
                    _game.create(data)
    
    def __str__(self):
        return self.__name + "-" + str(self.__gamelist[0]) + "," + str(self.__gamelist[1]) + "," + str(self.__gamelist[2]) 
        
class Playerhanderer:
    def __init__(self):
        self.__PlayerList = []
    def get_player_list(self):
        return self.__PlayerList
    def check(self, result):
        for name,data in result.items():
            # print(name)
            # print(data)
            all_name = []
            for player in self.__PlayerList:
                all_name.append(player.get_name())
            if name not in all_name:
                self.__PlayerList.append(Player(name))
            for player in self.__PlayerList:
                if name == player.get_name():
                    player.check(data)
    def write(self):
        data = self.firstline + "\n"
        for player in self.__PlayerList:
            data = data + str(player) + "\n"
            #print(data)
        with open('texts/stat.txt','w') as stat_file:
            stat_file.write(data)
     
    def read(self):
        with open('texts/stat.txt','r') as stat_file:
            # self.firstline = stat_file[0]
            for line_number,a in enumerate(stat_file):
                if line_number == 0:
                    self.firstline = a
                    print()
                    print(a)
                elif line_number > 0 and len(a) > 10:
                    print(a,end='')
                    playername,stat = a.split('-')
                    player_n = Player(playername)
                    self.__PlayerList.append(player_n)
                    player_n.create(stat)
            print()
        # file = open('texts/stat.txt')
        # for line_number,line in enumerate(file.readline()):
        #     if line_number == 0:
        #         self.firstline = line
        #     elif line_number>0 and len(line)>10:
        #         print(line,end = '')
        #         playername,stat = line.split('-')
        #         player_n = Player(playername)
        #         self.__PlayerList.append(player_n)
        #         player_n.create(stat)
class Game:
    
    player_name = ""
    def __init__(self,player_name):
        self.player_name = player_name
        print(self.player_name)
    
    def __str__(self):
        return 'ppp'
    
    # def set_name(self,new_name):
    #     self.__name = new_name
    
    # def get_name(self):
    #     return self.__name        
    

    def start(self):
        pass
    
    def running(self):
        pass
    
    def end(self):
        pass
    

class Menu():
    
    def __init__(self):
        pass
    
    def select_game(self):
        run =True
        playerhander = Playerhanderer()
        playerhander.read()
        while run:
            
            try:
                print('〓〓〓〓〓〓〓〓〓〓〓〓〓〓')
                print()
                today = date.today()
                print("Today's date:", today)
                print()
                print("Gamelist:\n")
                print('(1)FirstGame : Blackjack!')
                print('(2)SecondGame : NoThank')
                print('(3)ThirdGame : RockPaperScissorAI!')
                print('(4)show all stat')
                print('(8)To stop run')
                print()
                choose = int(input("enter 1,2,3,4,8 :"))
                print('〓〓〓〓〓〓〓〓〓〓〓〓〓〓')
                print()
            except:
                print("error")
                continue
                
            if choose == 1:
                bj = Blackjack()
                player_name, result = bj.start()
                temp = dict()
                temp[player_name] = {'blackjack': result}
                playerhander.check(temp)
                #print(temp)
                playerhander.write()
            if choose == 2:
                #add filename G2'''  '''
                g2run = True
                while g2run:
                    try:
                        player = int(input('Enter number of player : '))
                    except:
                        continue
                    g2run = False
                    NT = Nothank(player)
                    data = NT.start()
                    temp = dict()
                    for player_name, result in data.items():
                        temp[player_name] = {'NoThanks': result}
                    playerhander.check(temp)
                    #print(temp)
                    playerhander.write()
            if choose == 3:
                rps = RPS()
                player_name,result = rps.start()
                temp = dict()
                temp[player_name] = {'Rockpaperscissor': result}
                playerhander.check(temp)
                #print(temp)
                playerhander.write()
            if choose == 4:
                print('ALL GAME STAT OF ALL PLAYER')
                print()
                for player in playerhander.get_player_list():
                    print(player)
                print()
            if choose == 8:
                print('THANK FOR PLAYING, BYEBYE')
                run = False
                exit()
            
menu = Menu()
menu.select_game()