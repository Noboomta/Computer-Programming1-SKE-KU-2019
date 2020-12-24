import random
import sys

SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    ''' create the deck start with 2 of clubs results willl be : (cant write the doctest because the line space) 
    ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠',
    '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']
    '''
    org_deck = []
    for suit in SUITS:
        for rank in RANKS:
            card = rank + suit
            org_deck += [card]
    return org_deck        

def swap(org_deck):
    
    
    ''' function to swap the deck to be randomness
    '''
    play_deck = []
    for i in range(52):
        r = random.randrange(0, 52-i)
        play_deck += [org_deck[r]]
        org_deck.pop(r)
    return play_deck
    
def print_format(bot,bot_value,ply1,ply1_value):
    ''' normal function to make easier to not print every times
    
    >>> print_format(['3♠'],3,['A♠', '7♥'],18)
    bot card : 3♠
    NOW vBOT HAND = <3>
    player card : A♠ 7♥
    NOW vPLAYER HAND = <18>
    
    >>> print_format(['2♠'],2,['10♦', 'K♣'],20)
    bot card : 2♠
    NOW vBOT HAND = <2>
    player card : 10♦ K♣
    NOW vPLAYER HAND = <20>
    
    >>> print_format(['2♠', 'A♠', '3♠'],16,['10♦', 'K♣'],20)
    bot card : 2♠ A♠ 3♠
    NOW vBOT HAND = <16>
    player card : 10♦ K♣
    NOW vPLAYER HAND = <20>
    
    >>> print_format(['4♦'],4,['7♣', '10♦'],17)
    bot card : 4♦
    NOW vBOT HAND = <4>
    player card : 7♣ 10♦
    NOW vPLAYER HAND = <17>
    
    >>> print_format(['4♦'],4,['7♣', '10♦', '8♣'],25)
    bot card : 4♦
    NOW vBOT HAND = <4>
    player card : 7♣ 10♦ 8♣
    NOW vPLAYER HAND = <25>
    
    '''
    print(f"bot card : ",end = "")
    show(bot)
    print(f"NOW vBOT HAND = <{bot_value}>")
    print(f"player card : ",end = "")
    show(ply1)
    print(f"NOW vPLAYER HAND = <{ply1_value}>")
    
def hand_value(list_card):
    ''' count the value by using for loop and sort A card to be last
    >>> hand_value(['7♣', '10♦', '8♣'])
    25
    >>> hand_value(['4♣', '3♦', 'K♣'])
    17
    >>> hand_value(['4♣', 'A♦', 'K♣'])
    15
    >>> hand_value(['3♦', 'K♣', 'A♦'])
    14
    >>> hand_value(['7♣', 'K♣', '10♦', '8♣'])
    35
    '''
    value = 0
    numl = []
    charl = []
    for card in list_card:
        if card[0] in ["1","2","3","4","5","6","7","8","9"]:
            numl.append(card)
        elif card[0] in ['A','K','Q','J']:
            charl.append(card)
    
    charl.sort(reverse = True)
    rlist = numl + charl
    
    for card in rlist:
        if card[0] in ["2","3","4","5","6","7","8","9"]:
            value+=int(card[0])
        elif card[0] in ['1']:
            value+=10
        elif str(card[0]) in ['J','Q','K']:
            value+=10
        elif card[0] == 'A':
            if value+11 > 21:
                value+=1
            elif value+11 == 21:
                pass
            elif value+11 <21:
                value+=11
        else:   print("ELSEEEE")
    return value
                
def already21():
    ''' Show up that player won the game
    '''
    print("\n<<< YOU WIN >>>\n")
    sys.exit()
    
def add(ply1,ply1_value,play_deck,bot,bot_value):
    ''' cant make the doctest because line over รันดอกเทสไม่ได้ครับ บรรทัดเกินถ้าเอา output มาใส่ครับ
    เช่น 
    
    add(['10♠', 'A♣'], 0, ['K♣', 'J♣', '7♦', 'Q♦', '6♥', 'J♥', '4♥', '8♥', '9♣',
    'K♠', 'Q♥', '9♠', '3♦', 'A♠', '5♣', '8♠', '9♦', '4♦', '5♦', '9♥', 'K♥', '8♦', '8♣', '3♣', 'A♦', '2♥', 'Q♣', '2♣', '2♦', '2♠', '4♣', '7♠', '10♥', 'Q♠', '4♠', '6♠', 'K♦', '3♠', '10♦', '6♦', '7♥', '5♥', 'A♥', '6♣', '7♣', '10♣', 'J♦', '5♠', '3♥'], ['J♠'], 0)
    
    จะได้
     
    <<< BLACK JACK!!!! >>>

    bot card : J♠
    NOW vBOT HAND = <0>
    player card : 10♠ A♣ K♣
    NOW vPLAYER HAND = <21>

    <<< YOU WIN >>>
    '''
    ply1 += [play_deck[0]]
    play_deck.pop(0)
    ply1_value = hand_value(ply1)
    if hand_value(ply1) == 21:
        print("\n<<< BLACK JACK!!!! >>>\n")
        print_format(bot,bot_value,ply1,ply1_value)
        already21()
    return ply1,hand_value(ply1),play_deck,bot,bot_value

def main_menu(ply1,ply1_value,play_deck,bot,bot_value):
    ''' function of menu page
    cant make the doctest because line over รันดอกเทสไม่ได้ครับ บรรทัดเกินถ้าเอา output มาใส่ครับ
    เช่น 
    
    main_menu(['10♠', 'A♣'], 0, ['K♣', 'J♣', '7♦', 'Q♦', '6♥', 'J♥', '4♥', '8♥', '9♣',
    'K♠', 'Q♥', '9♠', '3♦', 'A♠', '5♣', '8♠', '9♦', '4♦', '5♦', '9♥', 'K♥', '8♦', '8♣', '3♣', 'A♦', '2♥', 'Q♣', '2♣', '2♦', '2♠', '4♣', '7♠', '10♥', 'Q♠', '4♠', '6♠', 'K♦', '3♠', '10♦', '6♦', '7♥', '5♥', 'A♥', '6♣', '7♣', '10♣', 'J♦', '5♠', '3♥'], ['J♠'], 0)
    
    จะได้
    
    <<< BLACK JACK!!!! >>>

    bot card : J♠
    NOW vBOT HAND = <10>
    player card : 10♠ A♣ K♣
    NOW vPLAYER HAND = <21>

    <<< YOU WIN >>>
    
    '''
    ply1_value = hand_value(ply1)
    bot_value = hand_value(bot)
    print_format(bot,bot_value,ply1,ply1_value)
    ply1_value = hand_value(ply1)
    if ply1_value>21:
        print("\n<<< YOU HAVE > 21 LOOSE >>>\n")
        sys.exit()
    elif ply1_value == 21:
        print("\n<<< BLACK JACK!!!! >>>\n")
        print_format(bot,bot_value,ply1,ply1_value)
        already21()
    elif ply1_value <16:
        print("\n-----------------------\nLESS THAN 16, MUST DRAW MORE\n")
        add(ply1,ply1_value,play_deck,bot,bot_value)
    else :
        try:
            r = int(input(f"\n-----------------------\npick your Decision (1)hit (0)stand (3)exit: "))
        except:
            print("???? AGIAN PLS ????")
            main_menu(ply1,ply1_value,play_deck,bot,bot_value)
        if r==1:
            print(" ")
            add(ply1,ply1_value,play_deck,bot,bot_value)
        if r==0:
            bot_mind(ply1,ply1_value,play_deck,bot,bot_value)
        if r == 3:
                sys.exit()
        if r>=2:
                main_menu(ply1,ply1_value,play_deck,bot,bot_value)
                
def show(hand_card):
    ''' show vard on hand in any hand(player or bot)
    
    doctest รันไม่ถูกอะครับ แต่มันได้ผลลัพธ์เหมือนกันเป้ะเลยนะครับ
    
    >>> show(['7♣', '10♦', '8♣'])
    7♣ 10♦ 8♣
    >>> show(['K♣', '7♣', '10♦', '8♣'])
    K♣ 7♣ 10♦ 8♣
    >>> show(['K♣', '7♣', '10♦', '3♣', 'A♠'])
    K♣ 7♣ 10♦ 3♣ A♠
    >>> show(['2♣', '8♦', 'J♣', 'A♠'])
    2♣ 8♦ J♣ A♠
    >>> show(['K♣', '7♣', '2♦', '2♣', 'A♠'])
    K♣ 7♣ 2♦ 2♣ A♠
    '''
    for card in hand_card:
        print(f"{card} ",end = "")
    print()

def bot_mind(ply1,ply1_value,play_deck,bot,bot_value):
    ''' function bot thinking to decise to draw more or not by check with player value and its value
     
     เหมือนเดิมครับ รัน doctest ไม่ได้ เพราะdeckมันเกินบรรทัดเลยรันแล้วผิดครับ
    '''
    valid = True
    print("\n-----------------------\nOPEN BOT HIDDEN CARD")
    bot += [play_deck[0]]
    play_deck.pop(0)
    t = 0
    while valid:
        ply1_value = hand_value(ply1)
        bot_value = hand_value(bot)
        if t>=1:
            print("\n-----------------------\nBOT DRAW MORE")
        if bot_value>ply1_value and bot_value<21:
            print()
            print_format(bot,bot_value,ply1,ply1_value)
            print("\n<<< Bot win >>>\n")
            valid = False
            sys.exit()
        elif bot_value == 21:
            print()
            print_format(bot,bot_value,ply1,ply1_value)
            print("\nBLACK JACK!!!!\n")
            print("\n<<< Bot win >>>\n")
            valid = False
            sys.exit()
        elif ply1_value<=21 and ply1_value == bot_value:
            print()
            print_format(bot,bot_value,ply1,ply1_value)
            print("\n<<< BOTH TIES >>>\n")
            sys.exit()
        elif bot_value<ply1_value and bot_value<21:
            print()
            print_format(bot,bot_value,ply1,ply1_value)
            bot += [play_deck[0]]
            play_deck.pop(0)
            bot_value = hand_value(bot)
        elif bot_value>21 :
            print()
            print_format(bot,bot_value,ply1,ply1_value)
            print("\n<<< YOU WIN, BOT > 21 >>>\n")
            valid = False
            sys.exit()
        t+=1
        
