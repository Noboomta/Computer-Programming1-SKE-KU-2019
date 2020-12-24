# fil = input("enter file name: ")
# line = open(fil).read().splitlines()
# print(line)
# table = [x.split(",") for x in line if x!= ""]
# print(table)
# print('-'*37)
# print("    Subject Credits Grade   Point")
# for i in range(len(table)):
#     print("    ",end = "")
#     for j in range(len(table[i])):
#         print("{0:<8}".format(table[i][j]),end="")
#     print(grade_point(table[i][-1]),end = "")
#     print("")

from operator import itemgetter
# print(sorted(team,key = itemgetter(3),reverse = True))

def min(team):
    a = sorted(team,key = itemgetter(3))
    print("")
    print(a[0][0],end = "")
    print(f" got minimum win rate {a[0][3]:.5f}")
    print("")
def max(team):
    b = sorted(team,key = itemgetter(3),reverse = True)
    print("")
    print(b[0][0],end="")
    print(f" got maximum win rate {b[0][3]:.5f}")
    print("")
def max_to_min(team):
    max_to_min_team = sorted(team,key = itemgetter(3),reverse = True)
    print(f"\nTotal team(s): {len(team)}")
    
    for i in range(len(max_to_min_team)):
        print(f"{max_to_min_team[i][0]}: got win rate {max_to_min_team[i][3]:.5f}")
    print("")
    
def min_to_max(team):
    min_to_max_team = sorted(team,key = itemgetter(3))
    print(f"\nTotal team(s): {len(team)}")
    
    for i in range(len(min_to_max_team)):
        print(f"{min_to_max_team[i][0]}: got win rate {min_to_max_team[i][3]:.5f}")
    print("")
    
def letter(team):
    letter = sorted(team,key = itemgetter(0))
    # letter = sorted(team,key = lambda x: x[-1]) 
    print("")
    for i in range(len(letter)): 
        print(f"{letter[i][0]}: got win rate {letter[i][3]:.5f}")
    print("")
    
filename = input("Enter a file name: ")
line = open(filename).read().splitlines()

while True:
    order = str(input("What do you want to know ? (m)in , ma(x) , (o)rder max to min, o(r)der min to max, (q)uiz : "))
    team = [x.split(",") for x in line if x!= " "]
    print(team)
    for i in range(len(team)):
        team[i].append(int(team[i][1]) / (int(team[i][1])+int(team[i][2])))
    # print(team)
    if order.upper() == 'M':
        min(team)
    if order.upper() == 'O':
        max_to_min(team)
    if order.upper() == 'X':
        max(team)
    if order.upper() == 'R':
        min_to_max(team)
    if order.upper() == 'L':
        letter(team)
    elif order.upper() == 'Q':
        break
    
    