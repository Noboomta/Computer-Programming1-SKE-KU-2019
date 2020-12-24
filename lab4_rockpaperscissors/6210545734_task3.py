import math
def check_valid_input(s):
    """ function which check that the input is True or False """
    if s == "rock" or s == "paper" or s == "scissors" or s == "spock" or s == "lizard":
        return True
    elif s == "gun" or s == "zombie" :
        return True
    else:
        return False
    
def convert_to_num(s):
    """ function which tranfer string to a number of choice 
    
    >>> convert_to_num("rock")
    2
    >>> convert_to_num("scissors")
    0
    """
    if s == "scissors":
        return 0
    elif s == "paper":
        return 1
    elif s == "rock":
        return 2
    elif s == "lizard":
        return 3
    elif s == "gun":
        return 4
    elif s == "zombie":
        return 5
    elif s == "spock":
        return 6
    else:
        print("Error: should not reach this if input is a valid one")

def convert_to_string(n):
    """ function which tranfer number of choice to string 
    
    >>> convert_to_string(3)
    'lizard'
    >>> convert_to_string(0)
    'scissors'
    
    """
    if n == 0:
        return "scissors"
    elif n == 1:
        return "paper"
    elif n == 2:
        return "rock"
    elif n == 3:
        return "lizard"
    elif n == 4:
        return "gun"
    elif n == 5:
        return "zombie"
    elif n == 6:
        return "spock"
    else:
        print("Error: should not reach this if input is a valid one")

# def game_decision(player_choice_num, computer_choice_num):
#     if player_choice_num == computer_choice_num:
#         print("Both ties!")
#     elif ((player_choice_num + 1) % 3) == computer_choice_num:
#         print("Computer wins!")
#     else:
#         print("Player wins!")
        
def game_decision7(player,com):
    """ function which recieve a choice from player and computer then display who is the winner 
    
    >>> game_decision7(0,0)
    Both ties!
    >>> game_decision7(0,1)
    Player wins!
    >>> game_decision7(1,2)
    Computer wins!
    >>> game_decision7(2,5)
    Player wins!
    >>> game_decision7(5,1)
    Player wins!
    >>> game_decision7(3,6)
    Computer wins!
    >>> game_decision7(4,0)
    Computer wins!
    """
    if com<0 :
        com+=7
    if player == com:
        print("Both ties!")
    elif com == 1 or com == 3 or com == 5:
        print("Player wins!")
    else :
        print("Computer wins!")
    
# get an input from a player and validate
def main():
    valid = False
    while valid == False:
        player_choice = input("Enter your choice: ")
        valid = check_valid_input(player_choice)
        if valid == False:
            print("Invalid choice. Enter again.")

    # random a response from a computer and print out player and computer choices
    import random
    computer_choice_num = random.randint(0, 6)
    computer_choice = convert_to_string(computer_choice_num)
    player_choice_num = convert_to_num(player_choice)
    print("Players chooses ", player_choice)
    print("Computer chooses ", computer_choice)
    game_decision7(0, computer_choice_num-player_choice_num)

# instead of this ugly if-elif-else nested block

if __name__ == "__main__":
    import doctest
    doctest.testmod()