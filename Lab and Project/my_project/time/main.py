def system_menu():
    bigmenu = str(input("(n)ew Route, (s)how, (c)hoose, (q)uit : ")).upper()
    return bigmenu

def menu(n,route,pick,num,status):
    if pick == 'N':
        name = str(input("Enter route name : "))
        route.append(name)
        return True
    elif pick == 'Q':
        run = False
        return run
    elif pick == 'C':
        num = int(input("Enter route nnumber: "))
        minimenu(n,route,pick,num,status)
        
def show(route):
    for i,name in enumerate(route) :
        print(f"Route {i+1} : {name}")

def minimenu(n,route,pick,num,status):
    pick = str(input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ")).upper()
    if pick == 'A':
        code = str(input("Bus Code :"))
        route.append([code]) 
        num+=1
        minimenu(n,route,pick,num,status)
    if pick == 'P':
        print(f"Route {num-2} : {route[num-3]}")
        for i,name in enumerate(route):
            print(f"{i+1}.{name} is stop (Current 0 secs / All 0 secs)")
    if pick == 'R':
        num = int(input("Bus number? : "))
        print(f"{i+1}.{route[num-1]} is stop (Current 0 secs / All 0 secs)")
        
        
n=0
route = []
run = True
status = []
num = 0
while run:
    pick = system_menu()
    # print(pick)
    run = menu(n,route,pick,num,status)
    show(route)