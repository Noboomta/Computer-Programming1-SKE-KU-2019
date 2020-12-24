from func import *

org_deck = create_deck()

play_deck = swap(org_deck)
    
'''main'''

valid = True
print("WELCOME TO BLACKJACK GAME\n")
ply1, ply2, bot = [],[],[]
ply1_value, ply2_value, bot_value = 0,0,0

bot += [play_deck[0]]
play_deck.pop(0)
ply1 += [play_deck[0]]
play_deck.pop(0)
ply1 += [play_deck[0]]
play_deck.pop(0)
bot_value = hand_value(bot)
ply1_value = hand_value(ply1)

while(valid):
    main_menu(ply1,ply1_value,play_deck,bot,bot_value)        




