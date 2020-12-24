import random
class Ntplayer:
    def __init__(self, name='', coin=11, number = 1):
        self.__name = name
        self.__coin = coin
        self.__number = number
        self.__hand = []
        self.__point = 0
    
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def get_hand(self):
        self.__hand.sort()
        return (self.__hand)
    
    def get_coin(self):
        return self.__coin
    
    def get_point(self):
        return self.__point

    def show_coin(self):
        print(self.__coin)
        
    def give_coin(self):
        self.__coin -= 1
        
    def add_card(self, card):
        self.__hand.append(card)
        
    def add_coin(self, coin):
        print(f'coin add == {coin}')
        self.__coin += coin
    
    def cal_point(self):
        self.__point = 0
        for card_number, card in enumerate(self.__hand):
            if card_number == 0:
                self.__point += int(card)
            else:
                if int(card) - int(self.__hand[card_number-1]) == 1:
                    pass
                else:
                    self.__point += int(card)
        self.__point -= int(self.__coin)
            
    @property
    def name(self):
        self.__name
    @name.setter
    def name(self,newname):
        self.__name = newname
    @property
    def coin(self):
        self.__coin
    @name.setter
    def coin(self,newcoin):
        self.__coin   
    @property
    def hand(self):
        self.__hand
    @hand.setter
    def hand(self,new_hand):
        self.__hand = new_hand
        
class Nothank:
    def __init__(self, number_player=1):
        self.__number_player = number_player
        self.__deck = []
        self.__player = []
        self.__hand = []
        self.__game_end = False
        self.__data = dict()
        number = 0
        for player in range(0,self.__number_player):
            name  = self.add_player_name(player)
            number+=1
            player = Ntplayer(name, 11, number)
            self.__player.append(player)
            
    def init_deck(self):
        for i in range(3,36):
            self.__deck.append(i)
    def add_player_name(self,player_num):
        name = str(input(f"<No Thank> Enter player {player_num+1} name: ")).upper()
        return name
    def cut_out_deck(self):
        for i in range(1,10):
            cut = random.randint(0, 33-i)
            self.__deck.pop(cut)
    def shuffle_card(self):
        random.shuffle(self.__deck)
        # self.__deck = [35,32,12,22,21,20,18]
    def show_deck(self):
        for card in self.__deck:
            print(card,end = " ")
        print()
        print(self.__deck)
        print(len(self.__deck))
    def ask_to_pick(self, player):
        ques = f'Do you want to pick up {self.__top_card}'
        ques_coin = f'Want to know coin '
        ans = 'C'
        while ans == 'C' or ans not in ['Y','N']:
            try:
                print(ques)
                ans = str(input('(Y)es or (N)o (C)oin : ')).upper()
            except ans not in ['Y','N']:
                self.ask_to_pick(self)
            
            # try:
            #     c = str(input(f'{ques_coin} (Y)es (N)o : ')).upper()
            # except :
            #     pass
                
            # if c == 'Y':
            #     print(f'Your coin : {self.__coin}')
            # elif c == 'N':
            #     pass
            
            if ans == 'N':
                return ans
            elif ans == 'Y':
                return ans    
            elif ans == 'C':
                print()
                print(f'Your coin : {player.get_coin()}')
                
    
    def start(self):
        self.init_deck()
        print('<No Thank> Deck created 33 cards (3-35).')
        self.shuffle_card()
        print('<No Thank> Deck shuffled.')
        self.cut_out_deck()
        print('<No Thank> Deck cut 9 cards.')
        self.shuffle_card()
        # self.show_deck()
        print(f'<No Thank> Game started with {len(self.__player)} player.')
        self.running()
        
        
        return self.get_data()
    def get_data(self):
        return self.__data
    def set_top_card(self):
        # print("The card on the stand is : ",end = '')
        # print(self.__deck[0])
        
        self.__top_card = self.__deck[0]
        print('Deck start with : ',end = "")
        print("|"*len(self.__deck),end='')
        self.__deck.pop(0)
        # print('<No Thank> Deck have more ',end = '')
        
        print()
    
    def new_top_card(self):
        self.__top_card = self.__deck[0]
        self.__deck.pop(0)
    
    def space(self):
        print("------------")
        
    def show_hand(self):
        for player_number, player in enumerate(self.__player):
            # print(f'{player.get_name()} : {player.get_hand()}')
            hand = player.get_hand()
            print(f'{player.get_name()} : ',end = '')
            for card_number, card in enumerate(hand):
                if card - hand[card_number-1] == 1 and card_number>0:
                    print(f',{card}',end = '')
                else:
                    if card_number == 0:
                        print(f'[{card}',end = '')
                    else:
                        print(f'] [{card}',end = '')
            
            if len(hand) == 0:
                print('[ ]') 
            else:       
                print(']')
    
    def show_all(self):
        self.__winner = 'HCHYCYGHDCGFSFXTWUMCKIIK'
        self.__lowest_point = 100000
        for player_number, player in enumerate(self.__player):
            print(f'{player.get_name()}:')
            hand = player.get_hand()
            print(f'hand : ',end = '')
            for card_number, card in enumerate(hand):
                if card - hand[card_number-1] == 1 and card_number>0:
                    print(f',{card}',end = '')
                else:
                    if card_number == 0:
                        print(f'[{card}',end = '')
                    else:
                        print(f'] [{card}',end = '')
            
            if len(hand) == 0:
                print('[ ]') 
            else:       
                print(']')
            print(f'coin : {player.get_coin()}')
            print(f'point : {player.get_point()}')
            if player.get_point()<self.__lowest_point:
                self.__lowest_point = player.get_point()
                self.__winner = player.get_name()
            print()
        self.__data = dict()
        print(f'winner is {self.__winner}')
        for player_number, player in enumerate(self.__player):
            if player.get_name() == self.__winner:
                self.__data[player.get_name()] = 'win'
            else:
                self.__data[player.get_name()] = 'lose'
        
    def show_coin(self):
        for player_number, player in enumerate(self.__player):
            print(f'{player.get_name()} : {player.get_coin()}')
    
    def cal_point(self):
        for player_number, player in enumerate(self.__player):
            player.cal_point()
            
    def show_point(self):
        for player_number, player in enumerate(self.__player):
            print(f'{player.get_name()} : {player.get_coin()}')
    
    # def player_draw(self, player):
        
    def running(self):
        while self.__game_end == False:
            self.set_top_card()
            coin_turned = 0
            while self.__game_end == False:
                
                for player_number, player in enumerate(self.__player):
                    
                    print()
                    self.space()
                    # print(f'middle coin now is {coin_turned}')
                    # print(f'player num{player_number+1} is {player.get_name()}')
                    self.show_hand()
                    # print('coin = ',end = '')
                    # player.show_coin()
                    # print(f'AAA>>>> {player.get_coin()}')
                    
                    # Active player loop
                    
                    while self.__game_end == False :
                        
                        print('<No Thank> Deck have more ',end = '')
                        print("|"*len(self.__deck))       
                        print(f'<No Thank> Coin in the middle have {coin_turned}')                       
                        print(f'<Turn> Player number{player.get_number()}: {player.get_name()}')
                        print(f'<Turn> Card on the stand {self.__top_card}')
                        
                        if self.ask_to_pick(player) == 'N':
                            if player.get_coin() > 0:
                                player.give_coin()
                                coin_turned += 1
                                break
                            else:
                                print('No Coin !!!!!!!')
                               
                        player.add_card(self.__top_card)
                        player.add_coin(coin_turned)
                        coin_turned = 0
                        # print(f'middle coin now is {coin_turned}')
                        self.show_hand()
                        
                        if len(self.__deck) != 0:
                            self.new_top_card()
                            print('Next card')
                            # print("|"*len(self.__deck),end='')
                            print()
                            
                        else:
                            self.__game_end = True
                        
                            
                        # if self.ask_to_pick(player) == 'Y':
                        #     player.add_card(self.__top_card)
                        #     player.add_coin(coin_turned)
                        #     coin_turned = 0
                        #     print(f'middle coin now is {coin_turned}')
                        #     self.show_hand()
                            
                        #     if len(self.__deck) != 0:
                        #         self.new_top_card()
                        #         print('Next card')
                        #         print("|"*len(self.__deck),end='')
                        #         print()
                                
                        #     else:
                        #         self.__game_end = True
                            
                        # else:
                        #     if player.get_coin() == 0:
                        #         print('No Coin !!!!!!!')
                        #         player.add_card(self.__top_card)
                        #         player.add_coin(coin_turned)
                        #         coin_turned = 0
                        #         print(f'middle coin now is {coin_turned}')
                        #         self.show_hand()
                                
                        #         if len(self.__deck) != 0:
                        #             self.new_top_card()
                        #             print('Next card')
                        #             print("|"*len(self.__deck),end='')
                        #             print()
                        #         else:
                        #             self.__game_end = True
                        #     else:
                        #         player.give_coin()
                        #         coin_turned += 1
                        #         break

                        # print(f'CCC>>>>> {player.get_coin()}')
                        #add card accept 
                        
                        
                        
                        
                        # print('coin = ',end = '')
                        # player.show_coin()
                        
                        
                        
                            
                        
                        
                        #return the same route
                    # print(f'BBB>>>> {player.get_coin()}')
                        
                    
                    
                            
            coin_turned = 0
            print()
            if len(self.__deck) == 0:
                self.__game_end =True
        
        self.__game_end = False
        
        print('Card is out\n')
        self.cal_point()
        self.show_all()
        
            
        
# NT = Nothank(3)
# NT.start()



