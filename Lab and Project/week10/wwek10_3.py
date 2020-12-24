def print_field(field,symbols):
    symbols.reverse()
    symbols.append(' ')
    symbols.reverse()
    print("-----------")
    for i in range(len(field)):
        for j in field[i]:
            # print(f"{j}",end = '')
            print('|',end = "")
            print(f"{symbols[j]}", end='')
        print("|")
    print("-----------")

field = [ [3,0,1,1,1] , [3,0,0,0,0] 
        , [3,3,0,0,0] , [0,2,2,2,0] 
        , [0,0,2,0,0] , [0,0,0,0,0] ]

symbols = ['@','#','&','$','N']

print_field(field,symbols)