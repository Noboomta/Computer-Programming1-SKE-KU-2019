import random
class RPS:
    def __init__(self):
        self.__name = str(input(f"<RockPaperScissorAI> Enter player name: ")).upper()
        self.__win,self.__lose,self.__draw = 0,0,0
    def get_win(self):
        return self.__win
    def get_lose(self):
        return self.__lose
    def get_draw(self):
        return self.__draw
    def get_player_name(self):
        return self.__name
    def start(self):
        self.__last_turnd = random.randint(1,3)
        if self.__last_turnd == 1:
            self.__last_turn = 'rock'
        elif self.__last_turnd == 2:
            self.__last_turn = 'paper'
        elif self.__last_turnd == 3:
            self.__last_turn = 'sciss'
        print(f'Start with : {self.__last_turn}')
        self.running()
        
        return self.get_player_name() , [self.get_win(), self.get_lose(),self.get_draw()]
    
    def running(self):
        while True:
            print('===============================')
            press = str(input('b(win) n(lose) m(draw) (,)finish : '))
            if press == 'b':
                self.__win+=1
                if self.__last_turn == 'rock':
                    self.__next_turn = 'sciss'
                elif self.__last_turn == 'sciss':
                    self.__next_turn = 'paper'
                elif self.__last_turn == 'paper':
                    self.__next_turn = 'rock'
            elif press == 'n':
                self.__lose+=1
                if self.__last_turn == 'rock':
                    self.__next_turn = random.choice(['rock','paper'])
                elif self.__last_turn == 'sciss':
                    self.__next_turn = random.choice(['sciss','rock'])
                elif self.__last_turn == 'paper':
                    self.__next_turn = random.choice(['paper','sciss'])
            elif press == 'm':
                self.__draw+=1
                if self.__last_turn == 'rock':
                    self.__next_turn = random.choice(['sciss','rock'])
                elif self.__last_turn == 'sciss':
                    self.__next_turn = random.choice(['paper','sciss'])
                elif self.__last_turn == 'paper':
                    self.__next_turn = random.choice(['rock','paper'])
            elif press == ',':
                break
        
            print('Have to : ',end = '')
            print(self.__next_turn)
            if self.__win+self.__draw+self.__lose > 0:
                print(f'round = {self.__win+self.__lose+self.__draw}')
                print(f'win = {self.__win}')
                print(f'lose = {self.__lose}')
                print(f'draw = {self.__draw}')
                print(f'%win from all = {self.__win/(self.__win+self.__lose+self.__draw) * 100}')
                if self.__win+self.__lose > 0:
                    print(f'%win from winlose = {self.__win/(self.__win+self.__lose) * 100}')
                else:
                    print()
            
            self.__last_turn = self.__next_turn
        print('===============================')
        print('final result')
        print(f'round = {self.__win+self.__lose+self.__draw}')
        print(f'win = {self.__win}')
        print(f'lose = {self.__lose}')
        print(f'draw = {self.__draw}')
        print(f'%win from all = {self.__win/(self.__win+self.__lose+self.__draw) * 100}')
        print(f'%win from winlose = {self.__win/(self.__win+self.__lose) * 100}')
        print('===============================')
        
    
# r = RPS()
# r.start()