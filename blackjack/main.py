# To do: option that allows player to draw more cards if he does not want to stand
import sys
from BJ import *

__author__ = "Paruj Ratanaworabhan"
__credits__ = ["Paruj Ratanaworabhan"]
__version__ = "0.1.0"
__maintainer__ = "Paruj Ratanaworabhan"
__email__ = "paruj.r@ku.th"
__status__ = "Dev"

# initialize a deck of cards
deck = initialize_cards()

# shuffle the deck
shuffle_cards(deck)

# draw a player hand
player_hand = draw_cards(deck, 2)

# draw the computer hand
computer_hand = draw_cards(deck, 2)

# display player_hand
print("Your hand: ", end = '')
display_cards(player_hand)

# display computer_hand
print("Computer hand: ", end = '')
display_cards(computer_hand[1:])

# check if decision can be made right away with Blackjack hands
player_BJ = check_for_Blackjack(player_hand)
computer_BJ = check_for_Blackjack(computer_hand)
if player_BJ and computer_BJ:
    print("Both tie")
elif player_BJ:
    print("Player wins")
elif computer_BJ:
    print("Computer wins")

if player_BJ or computer_BJ:
    print("Computer hand: ", end='')
    display_cards(computer_hand)
    sys.exit()

# player must draw more cards if hand value is below the threshold
while (must_draw_more(player_hand)):
    player_hand += draw_cards(deck, 1)
    print("Your hand: ", end = '')
    display_cards(player_hand)
    
# computer must draw more cards if hand value is below the threshold
while (must_draw_more(computer_hand)):
    computer_hand += draw_cards(deck, 1)
    print("Computer hand: ", end = '')
    display_cards(computer_hand[1:])

# determine who wins or they are both tie
player_stand = calculate_hand_value(player_hand)
computer_stand = calculate_hand_value(computer_hand)
if player_stand > 21:
    if computer_stand > 21:
        print("Both tie")
    else:
        print("Computer wins")
else:
    if computer_stand > 21:
        print("Player wins")
    else:
        # the computer can fight back as it knows what the hand value for player is
        while computer_stand < player_stand:
            computer_hand += draw_cards(deck, 1)
            computer_stand = calculate_hand_value(computer_hand)
            print("Computer hand adjusted: ", end = '')
            display_cards(computer_hand[1:])
        if computer_stand > 21:
            print("Player wins")
        elif computer_stand == player_stand:
            print("Both tie")
        else:
            print("Computer wins")
print("Computer hand final: ", end = '')
display_cards(computer_hand)
