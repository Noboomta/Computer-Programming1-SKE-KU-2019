import math,sys
item = []
def new_item(item):
    nit = str(input("Name : "))
    item.append(nit)
    print(f"{nit} added")
    menu_text(item)
    
def menu_text(item):
    menu = str(input("(N)ew (S)how (D)elete (Q)uit : "))
    if menu.upper() == 'N':
        new_item(item)
    elif menu.upper() == 'S':
        show_item(item)
    elif menu.upper() == 'D':
        delete_item(item)
    elif menu.upper() == 'Q':
        print("Bye")
        sys.exit()
    else:   
        print("Incorrect Menu")
        menu_text(item)
        
def show_item(item):
    for index,value in enumerate(item):
        print(f"({index+1}) {value}")
    menu_text(item)
    
def delete_item(item):
    try:
        indexd = int(input("Number? : "))
    except:
        print("Not a number")
        delete_item(item)
    if indexd > len(item) or indexd<=0:
        print("Not in range")
        delete_item(item)
    # elif type(indexd) != int :
    #     print("Not a number")
    #     delete_item(item)
    else:   item.pop(indexd-1)
    # print(len(item))
    if len(item) == 0:
        while True:
            nq = str(input("(N)ew (Q)uit : "))
            if nq.upper() == 'N' or nq.upper() == 'Q':
                if nq.upper() == 'N':
                    new_item(item)
                    break
                elif nq.upper() == 'Q':
                    print("Bye")
                    sys.exit()
            print("Incorrect Menu")
        menu_text(item)
    show_item(item)
    menu_text(item)

nq = str(input("(N)ew (Q)uit : "))
while True:
    if nq.upper() == 'N' or nq.upper() == 'Q':
        if nq.upper() == 'N':
            new_item(item)
            break
        elif nq.upper() == 'Q':
            print("Bye")
            sys.exit()
    print("Incorrect Menu")
    nq = str(input("(N)ew (Q)uit : "))
# menu_text(item)
# if menu_text 