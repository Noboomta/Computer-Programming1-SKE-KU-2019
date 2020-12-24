import sys,math
dot_list_x = []
dot_list_y = []
num = 1

def input_xy(dot_list_x,dot_list_y,num):
    x = float(input(f"Enter x{num} :"))
    y = float(input(f"Enter y{num} :"))
    dot_list_x.append(x)
    dot_list_y.append(y)
    num+=1
    system_ask_minor(dot_list_x,dot_list_y,num)

def show_xy(dot_list_x,dot_list_y,num):
    for indexx , valuex in enumerate(dot_list_x):
        for indexy , valuey in enumerate(dot_list_y):
            if indexx == indexy:
                print(f"Point {indexx} = ({valuex:.0f},{valuey:.0f})")
    system_ask(dot_list_x,dot_list_y,num)   
    
def system_ask_minor(dot_list_x,dot_list_y,num):
    choice = str(input("(m)ore, (e)nd :"))
    if choice.upper() == 'M':
        input_xy(dot_list_x,dot_list_y,num)
    elif choice.upper() == 'E':
        system_ask(dot_list_x,dot_list_y,num)
    else:
        system_ask_minor(dot_list_x,dot_list_y,num)

def find_distance(dot_list_x,dot_list_y,num):
    x1,x2 = dot_list_x[0],dot_list_x[1] 
    y1,y2 = dot_list_y[0],dot_list_y[1] 
    dx = x2-x1
    dy = y2-y1
    dis = (dx**2 + dy**2)**0.5
    print(f"Distance from P1 to P2 is {dis:.2f}")
    system_ask(dot_list_x,dot_list_y,num)
    
def find_perimeter(dot_list_x,dot_list_y,num):
    perimeter = 0
    for indexx , valuex in enumerate(dot_list_x):
        for indexy , valuey in enumerate(dot_list_y):
            for indexx2 ,valuex2 in enumerate(dot_list_x):
                for indexy2 , valuey2 in enumerate(dot_list_y):
                    if indexx2 - indexx == 1 and indexy2 - indexy == 1 and indexx == indexy and indexx2 == indexy2 and indexx!= len(dot_list_x):
                        x1,y1,x2,y2 = valuex,valuey,valuex2,valuey2
                        dx = x1-x2
                        dy = y1-y2
                        dis = (dx**2 + dy**2)**0.5
                        perimeter += dis
    x1,y1,last_x,last_y = dot_list_x[0],dot_list_y[0],dot_list_x[-1],dot_list_y[-1]
    dx = last_x-x1
    dy = last_y-y1
    dis = (dx**2 + dy**2)**0.5
    perimeter+=dis
    print(f"Perimeter is {perimeter:.2f}")
    system_ask(dot_list_x,dot_list_y,num)
    
def reset(dot_list_x,dot_list_y,num):
    del dot_list_x
    del dot_list_y
    del num
    dot_list_x = []
    dot_list_y = []
    num = 1
    input_xy(dot_list_x,dot_list_y,num)

def system_ask(dot_list_x,dot_list_y,num):
    if len(dot_list_x)>2:
        choice = str(input("(s)how points, (p)erimeter, (n)ew, (q)uit :"))
        if choice.upper() == 'S':
            show_xy(dot_list_x,dot_list_y,num)
        elif choice.upper() == 'P':
            find_perimeter(dot_list_x,dot_list_y,num)
        elif choice.upper() == 'N':
            reset(dot_list_x,dot_list_y,num)
        elif choice.lower() == 'q':
            print("Bye")
            sys.exit()
        else :
            system_ask(dot_list_x,dot_list_y,num)
    elif len(dot_list_x) == 2:
        choice = str(input("(s)how points, (d)istance, (n)ew, (q)uit :"))
        if choice.upper() == 'S':
            show_xy(dot_list_x,dot_list_y,num)
        elif choice.upper() == 'D':
            find_distance(dot_list_x,dot_list_y,num)
        elif choice.upper() == 'N':
            reset(dot_list_x,dot_list_y,num)
        elif choice.lower() == 'q':
            print("Bye")
            sys.exit()
        else :
            system_ask(dot_list_x,dot_list_y,num)
    elif len(dot_list_x) == 1:
        choice = str(input("(s)how points, (n)ew, (q)uit :"))    
        if choice.upper() == 'S':
            show_xy(dot_list_x,dot_list_y,num)
        elif choice.upper() == 'N':
            reset(dot_list_x,dot_list_y,num)
        elif choice.lower() == 'q':
            print("Bye")
            sys.exit()
        else :
            system_ask(dot_list_x,dot_list_y,num)
            
# main

input_xy(dot_list_x,dot_list_y,num)
