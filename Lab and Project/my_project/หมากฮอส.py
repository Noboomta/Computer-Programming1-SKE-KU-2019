lis = [['a',0],['b',0]]
turn = 1
field = [ [0,2,0,2,0,2,0,2]  
        , [2,0,2,0,2,0,2,0] 
        , [0,0,0,0,0,0,0,0]  
        , [0,0,0,0,0,0,0,0] 
        , [0,0,0,0,0,0,0,0]  
        , [0,0,0,0,0,0,0,0]
        , [0,4,0,4,0,4,0,4] 
        , [4,0,4,0,4,0,4,0] ]

def print_field(field,symbols,turn):
    print("")
    for i in range(8):
        print('|',end = "")
        print("<{0:^1}>".format(i+1),end = "")
    print('|',end = "")
    # for i in field:
    #     for j in i:
    #         if symbols[j] == 'A' or symbols[j] == 'a':
    #             lis[0][1]+=1
    #         if symbols[j] == 'B' or symbols[j] == 'b':
    #             lis[1][1]+=1
    print("")
    print("")
    for i in range(len(field)):
        for j in field[i]:
            # print(f"{j}",end = '')
            print('|',end = "")
            print("{0:^3}".format(symbols[j]),end = "")
            if symbols[j] == 'A' or symbols[j] == 'a':
                lis[0][1]+=1
                # print(f"{lis[0][1]}",end = '')
            elif symbols[j] == 'B' or symbols[j] == 'b':
                lis[1][1]+=1
                # print(f"{lis[1][1]}",end = '')
            else:
                print("",end = '')
        print("|",end = "")
        print(f" <{i+1}> ")
        print("")
    print("-------------")
    lis[1][1] = 0
    lis[0][1] = 0
    
    if turn %2 == 1:
        turn +=1
        A_choose(field,symbols,turn)
    elif turn %2 == 0:
        turn +=1
        B_choose(field,symbols,turn)
    
    
def A_choose(field,symbols,turn):
    print("A turn")
    col = int(input("Enter columm : "))
    line = int(input("Enter line : "))
    print(symbols[field[col-1][line-1]])
    if symbols[field[col-1][line-1]] not in ['a','A']:
        A_choose(field,symbols,turn)
    lr = int(input("Enter'1' for left, '2' for right : "))
    Aupdate_field(field,symbols,turn,lr,col,line)

    
def B_choose(field,symbols,turn):
    print("B turn")
    col = int(input("Enter columm : "))
    line = int(input("Enter line : "))
    print(symbols[field[col-1][line-1]])
    if symbols[field[col-1][line-1]] not in ['b','B']:
        B_choose(field,symbols,turn)
    lr = int(input("Enter'1' for left, '2' for right : "))
    # while True:
    #     lr = int(input("Enter'1' for left, '2' for right : "))
    Bupdate_field(field,symbols,turn,lr,col,line)

    
def Aupdate_field(field,symbols,turn,lr,col,line):
    if lr == 1: #left
        if line-2<0 or col==8:
            print("error out field")
            A_choose(field,symbols,turn)
        else:
            org = field[col-1][line-1]
            field[col-1][line-1] = 0
            if field[col][line-2] != 0 and line-3<0 or col+1>8:
                print("error hit")
                field[col-1][line-1] = org
                A_choose(field,symbols,turn)
            if field[col][line-2] != 0:
                field[col][line-2] = 0
                field[col+1][line-3] = org
            else:
                field[col][line-2] = org
    elif lr == 2: #right
        if line==8 or col==8:
            print("error out field")
            A_choose(field,symbols,turn)
        else:    
            org = field[col-1][line-1]
            field[col-1][line-1] = 0
            if field[col][line] != 0 and line+1>=8 or col<=0:
                print("error hit")
                field[col-1][line-1] = org
                A_choose(field,symbols,turn)
            if field[col][line] != 0:
                field[col][line] = 0
                field[col+1][line+1] = org
            else:
                field[col][line] = org
    print_field(field,symbols,turn)

def Bupdate_field(field,symbols,turn,lr,col,line):
    if lr == 1: #left
        if line-2<0 or col==0:
            print("error out field")
            B_choose(field,symbols,turn)
        else:
            org = field[col-1][line-1]
            field[col-1][line-1] = 0
            if field[col-2][line-2] != 0 and line-3<0 or col-1==0:
                print("error hit")
                field[col-1][line-1] = org
                B_choose(field,symbols,turn)
            if field[col-2][line-2] != 0:
                field[col-2][line-2] = 0
                field[col-3][line-3] = org
            else:
                field[col-2][line-2] = org
    elif lr == 2: #right
        if line>=8 or col==0:
            print("error out field")
            B_choose(field,symbols,turn)
        else:
            org = field[col-1][line-1]
            field[col-1][line-1] = 0
            if field[col-2][line-2] != 0 and line+1<0 or col-2==0:
                print("error hit")
                field[col-1][line-1] = org
                B_choose(field,symbols,turn)
            if field[col-2][line] != 0:
                field[col-2][line] = 0
                field[col-3][line+1] = org
            else:
                field[col-2][line] = org
    print_field(field,symbols,turn)

symbols = [' ','A','a','B','b']

print_field(field,symbols,turn)