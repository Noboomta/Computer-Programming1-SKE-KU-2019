import random

class Blackjack():
    
    __deck = []
    __player_hand = []
    __bot_hand = []
    __player_status = 'NORMAL'
    __bot_status = 'NORMAL'
    __player_value = 0
    __bot_value = 0
    game_end = False
    SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # def __del__(self):
    #     print("DESTROYED NOT COMPLETE: CODE001??! BLACKJACK__Main.py/G1.py")        
    def deck_create(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__deck.append(rank+suit)    
        self.__condition = ''
    def shuffle_card(self):
        random.shuffle(self.__deck)
    def show_deck(self):
        print(self.__deck)
    def get_card(self):
        return self.__deck.pop(0)
    def draw_card(self,hand,value):
        hand.append(self.get_card())
        value = self.card_value(hand)
        if value >= 21:
            self.game_end = True
    def card_value(self,hand):
        letter_card = []
        num_card = []
        value = 0
        sorted_hand = []
        for card in hand:
            if card[0] in ['1','2','3','4','5','6','7','8','9']:
                num_card.append(card)
            elif card[0] in ['K','Q','A','J']:
                letter_card.append(card)
                letter_card.sort(reverse = True)
        sorted_hand = num_card + letter_card
        for card in sorted_hand:
            if card[0] in ['2','3','4','5','6','7','8','9']:    value += int(card[0])
            elif card[0] == '1':    value += 10
            elif card[0] in ['K','Q','J']:  value += 10
            elif card[0] == 'A':
                if value > 10 : value += 1
                elif value <= 10 :  value += 11
        return int(value)
    def show_hand(self):
        print("player hand [",end = ' ')
        for card in self.__player_hand:
            print(f'{card}',end = ' ')
        print("]")
        
        print("bot hand [",end = ' ')
        for card in self.__bot_hand:
            print(f'{card}',end = ' ')
        print("]")
    def show_value(self,player,bot):
        print(f"player hand value = {self.card_value(player)}")
        print(f"bot hand value = {self.card_value(bot)}")
    def set_all(self):
        #set value of player and bot
        self.__player_value = self.card_value(self.__player_hand)
        self.__bot_value = self.card_value(self.__bot_hand)
        #game status set zone
        if self.__player_value > self.__bot_value and self.__player_value <= 21 :     
            self.game_status = 'player win'
        elif self.__bot_value > self.__player_value and self.__bot_value <= 21 :
            self.game_status = 'bot win'
        elif self.__player_value > 21:
            self.game_status = 'player loose'
        elif self.__bot_value > 21:
            self.game_status = 'bot loose'
        #statement zone
        if self.card_value(self.__player_hand) >= 21 :
            self.__game_end = True
            if self.card_value(self.__player_hand) == 21 :
                self.__player_status == 'BLACKJACK'
            elif self.card_value(self.__player_hand) > 21 :
                self.__player_status == 'OVER 21'
        if self.card_value(self.__bot_hand) >= 21 :
            self.__game_end = True
            if self.card_value(self.__bot_hand) == 21 :
                self.__bot_status == 'BLACKJACK'
            elif self.card_value(self.__bot_hand) > 21 :
                self.__bot_status == 'OVER 21'
        #game end set
        if self.__player_value >= 21 or self.__bot_value > 21 or self.__bot_value>self.__player_value:
            self.game_end = True
    def space(self):
        print("--------")
        
    def start(self):
        self.__name = str(input(f"<Blackjack> Enter player name: ")).upper()
        self.__deck = []
        self.__player_hand = []
        self.__bot_hand = []
        self.__player_status = 'NORMAL'
        self.__bot_status = 'NORMAL'
        self.__player_value = 0
        self.__bot_value = 0
        self.game_end = False
         
        #deck generated and shuffle
        self.deck_create()
        self.shuffle_card()
        
        #start game with 2draw fro player and 1 for bot
        #show card and value of player and bot
        self.draw_card(self.__player_hand, self.__player_value)
        self.draw_card(self.__player_hand, self.__player_value)
        self.draw_card(self.__bot_hand, self.__bot_value)
        self.show_hand()
        self.show_value(self.__player_hand, self.__bot_hand)
        # self.set_all()
        self.space()
        
        self.running()
        return self.__name, self.game_status
    def running(self):
        
        while self.card_value(self.__player_hand) < 16 and self.game_end == False:
            self.set_all()
            print(f"auto draw for player (value = {self.__player_value} < 16)")
            self.draw_card(self.__player_hand, self.__player_value)
            self.show_hand()
            self.show_value(self.__player_hand,self.__bot_hand)
            # self.set_all()
            self.space()
            
        while self.game_end == False:
            self.set_all()
            try:
                want = str(input("Want to (H)it or (S)tand : ")).upper()
            except want not in ['H','S']:
                continue
            if want == 'H':
                self.draw_card(self.__player_hand, self.__player_value)
                self.show_hand()
                self.show_value(self.__player_hand,self.__bot_hand)
                # self.set_all()
                self.space()
            if want == 'S' :
                self.space()
                print("Player finished")
                print("bot turn start")
                self.space()
                self.set_all()
                break
        
        while (self.card_value(self.__bot_hand) <= self.card_value(self.__player_hand) )and( self.card_value(self.__bot_hand) < 21 ) and self.game_end == False:
            self.set_all()
            self.draw_card(self.__bot_hand, self.__bot_value)
            self.show_hand()
            self.show_value(self.__player_hand, self.__bot_hand)
            self.space()
            self.set_all()
        
        if self.game_end == True:
            self.set_all()
            print(self.game_status)
            if self.__bot_value>21:
                print('with condition: Bot score > 21')
                self.__condition = 'with condition: Bot score > 21'
            elif self.__player_value>21:
                print('with condition: Player score > 21')
                self.__condition = 'with condition: Player score > 21'
            elif self.__bot_value==21:
                print('with condition: Bot got BlackJack')
                self.__condition = 'with condition: Bot got BlackJack'
            elif self.__player_value==21:
                print('with condition: Player got BlackJack')
                self.__condition = 'with condition: Player got BlackJack'
            elif self.__bot_value>self.__player_value:
                print('with condition: Bot value > Player value')
                self.__condition = 'with condition: Bot value > Player value'
            elif self.__player_value>self.__bot_value:
                print('with condition: Player value > Bot value')
            self.__condition = 'with condition: Player value > Bot value'