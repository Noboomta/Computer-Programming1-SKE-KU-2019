from error import *

__author__ = "Paruj Ratanaworabhan"
__credits__ = ["Paruj Ratanaworabhan"]
__version__ = "0.1.0"
__maintainer__ = "Paruj Ratanaworabhan"
__email__ = "paruj.r@ku.th"
__status__ = "Dev"

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
STAY_VAL = 16

def initialize_cards():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            card = rank + ' ' + suit
            deck += [card]
    return deck

def shuffle_cards(deck):
    import random
    n = len(deck)
    for i in range(n):
        r = random.randrange(i, n)
        temp = deck[r]
        deck[r] = deck[i]
        deck[i] = temp

def display_cards(lcards):
    display_str = ""
    for each_card in lcards:
        ltemp = each_card.split()
        if ltemp[1] == 'Clubs':
            display_str += ltemp[0] + '\u2663' + ' '
        elif ltemp[1] == 'Diamonds':
            display_str += ltemp[0] + '\u2666' + ' '
        elif ltemp[1] == 'Hearts':
            display_str += ltemp[0] + '\u2660' + ' '
        else:
            assert ltemp[1] == 'Spades', 'Spades expected'
            display_str += ltemp[0] + '\u2665' + ' '
    print(display_str)

def draw_cards(deck, n):
    hand = []
    for i in range(n):
        hand.append(deck.pop())
    return hand

def validate_hand(hand):
    """Return True if this hand is valid, return False, otherwise.
    """

    for each_card in hand:
        ltemp = each_card.split()
        try:
            if not (ltemp[0] in RANKS):
                raise InvalidCardRank
            if not (ltemp[1] in SUITS):
                raise InvalidCardSuit
        except InvalidCardRank:
            print("Found this invalid rank", ltemp[0], "; rank must be in", RANKS)
            return False
        except InvalidCardSuit:
            print("Found this invalid suit", ltemp[1], "; suite must be in", SUITS)
            return False
    return True

def calculate_hand_value(hand):
    """Return the value of a given hand. When there are Ace rank cards in the hand, use the max value of Ace rank, which is 11 - 1 + the number of all Ace rank cards, if the resulting hand value is not greater than 21; otherwise, use the min value of Ace rank, which is the number of all Ace rank cards.

    >>> calculate_hand_value(['2 Clubs', 'Ace Spades', 'Ace Clubs', '4 Clubs'])
    18
    >>> calculate_hand_value(['Ace Diamonds', '8 Clubs'])
    19
    >>> calculate_hand_value(['Ace Diamonds', '8 Clubs', '7 Clubs'])
    16
    >>> calculate_hand_value(['Ace Hearts', 'Ace Diamonds'])
    12
    >>> calculate_hand_value(['Ace Hearts', 'Ace Diamonds', '2 Clubs', '10 Diamonds'])
    14
    >>> calculate_hand_value(['Jack Clubs', '7 Hearts', 'Queen Hearts'])
    27
    >>> calculate_hand_value(['King Hearts', 'Queen Clubs'])
    20
    >>> calculate_hand_value(['Ace Spades', 'Queen Spades'])
    21
    >>> calculate_hand_value(['4 Hearts', '9 Hearts', '4 Diamonds'])
    17
    >>> calculate_hand_value(['4 Hearts', '9 Hearts', '4 Diamonds', '8 Spades'])
    25
    """

    assert type(hand) is list, 'Python list expected'
    assert validate_hand(hand), 'Invalid hand'
    val = 0
    num_ace = 0
    for card in hand:
        ltemp = card.split()
        if ltemp[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            val += int(ltemp[0])
        elif ltemp[0] in ['Jack', 'Queen', 'King']:
            val += 10
        else:
            assert ltemp[0] == 'Ace', 'Ace rank expected'
            num_ace += 1
    if num_ace == 0:
        return val
    else:
        if (val + num_ace - 1 + 11) > 21:
            return val + num_ace
        else:
            return val + num_ace - 1 + 11

def check_for_Blackjack(hand):
    """Return True if a given hand is a Blackjack, return False, otherwise.

    >>> check_for_Blackjack(['Ace Diamonds', '8 Clubs'])
    False
    >>> check_for_Blackjack(['Ace Hearts', 'Ace Diamonds'])
    False
    >>> check_for_Blackjack(['King Hearts', 'Queen Clubs'])
    False
    >>> check_for_Blackjack(['Ace Spades', 'Queen Spades'])
    True
    """

    assert len(hand) == 2, 'Blakjack hand must contain exactly two cards.'
    if calculate_hand_value(hand) == 21:
        return True
    else:
        return False

def must_draw_more(hand):
    """Return True if a given hand value is not enough to stay, return False, otherwise.
    
    >>> must_draw_more(['7 Clubs', '2 Clubs'])
    True
    >>> must_draw_more(['7 Clubs', '2 Clubs', '5 Hearts'])
    True
    >>> must_draw_more(['7 Clubs', '2 Clubs', '5 Hearts', '6 Diamonds'])
    False
    >>> must_draw_more(['Ace Diamonds', '8 Clubs', '7 Clubs'])
    False
    >>> must_draw_more(['Ace Hearts', 'Ace Diamonds'])
    True
    >>> must_draw_more(['Ace Hearts', 'Ace Diamonds', '2 Clubs', '10 Diamonds'])
    True
    """

    hand_val = calculate_hand_value(hand)
    if hand_val < STAY_VAL:
        return True
    else:
        return False
