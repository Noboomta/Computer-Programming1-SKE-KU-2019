def print_field(field,symbols):
    print('-'*(2*(len(field[0]))+1))
    for i in range(len(field)):
        for j in range (0,len(field[i])):
            if (field[i][j]) == 0 and j == 0:
                print(f'| |',end ='')
            elif (field[i][j]) == -1 and j == 0:
                print(f'|X|',end ='')
            elif (field[i][j]) == -1:
                print(f'X|',end ='')
            elif j == 0:
                print(f'|{symbols[(field[i][j])-1]}|',end ='')
            elif (field[i][j]) == 0:
                print(' |',end ='')
            else:
                print(f'{symbols[(field[i][j])-1]}|',end ='') 
        print()
    print('-'*(2*(len(field[0]))+1))
def get_submarine_info(field,sub_names):
    orig_sizes = {x:0 for x in sub_names}
    curr_sizes = {x:0 for x in sub_names}
    statuses = { x:'T' for x in sub_names} 
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 3:
                orig_sizes['Seawolf'] += 1
            elif field[i][j] == 2:
                orig_sizes['Nautilus'] += 1
            elif field[i][j] == 1:
                orig_sizes['Marlin'] += 1
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 3:
                curr_sizes['Seawolf'] += 1
            elif field[i][j] == 2:
                curr_sizes['Nautilus'] += 1
            elif field[i][j] == 1:
                curr_sizes['Marlin'] += 1
    return orig_sizes,curr_sizes,statuses
def display_result(sub_name,orig_sizes,curr_sizes,status):
    print(f'Submarine name:', end ='')
    for x in sub_name:
        print(f'{x:>10}', end ='')
    print()
    print(f'Original size :', end ='')
    for x in sub_name:
        print(f'{orig_sizes[x]:>10}', end ='')
    print()
    print(f'Current size  :', end ='')
    for x in sub_name:
        print(f'{curr_sizes[x]:>10}', end ='')
    print()
    print(f'Status        :', end ='')
    for x in sub_name:
        print(f'{status[x]:>10}', end ='')
    print()
def get_attack_position(field):
    num = [1,2,3,4,5]
    num1 = [1,2,3,4,5,6]
    i = 1
    while True:
        x = int(input("Enter x position (1-5): "))
        if x in num:
            while True:
                y = int(input("Enter y position (1-6): "))
                if y in num1:
                    i += 1
                    return x,y
                else:
                    print('Invalid y position!')
        else:
            print('Invalid x position!')
def update(x, y, field, sub_names, curr_sizes, statuses):
    field[y-1][x-1] = -1
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 3:
                curr_sizes['Seawolf'] += 1
            elif field[i][j] == 2:
                curr_sizes['Nautilus'] += 1
            elif field[i][j] == 1:
                curr_sizes['Marlin'] += 1
    for x in statuses:
        if curr_sizes[x] == 0:
            statuses[x] = 'F'
    curr_sizes = {x:0 for x in sub_names}
    return field,curr_sizes,statuses
field = [[3, 0, 1, 1, 1],
         [3, 0, 0, 0, 0],
         [3, 3, 0, 0, 0],
         [0, 2, 2, 2, 0],
         [0, 0, 2, 0, 0],
         [0, 0, 0, 0, 0]]
symbols = ['@', '#', '&', '$', 'N']
sub_names = ['Marlin', 'Nautilus','Seawolf']
n = [1,2,3]
i = 1
count = 0
for q in range(len(field)):
    for w in range(len(field[q])):
        if field[q][w] in n:
            count += 1
print_field(field,symbols) 
orig_sizes,curr_sizes,statuses = get_submarine_info(field,sub_names)  
display_result(sub_names,orig_sizes,curr_sizes,statuses) 
print(f'Attack #{i}:')      
x,y = get_attack_position(field)
i += 1
ship = []
update(x, y, field, sub_names, curr_sizes, statuses)
while True:
    print_field(field,symbols) 
    curr_sizes = {x:0 for x in sub_names}
    update(x, y, field, sub_names, curr_sizes, statuses) 
    display_result(sub_names,orig_sizes,curr_sizes,statuses)
    for k in range(len(field)):
        for j in range(len(field[k])):
            if field[k][j] in n:
                ship.append(field[k][j])
    if len(ship) < count//2:
        print(f'Congratulations, you attacked 2 out of 3 submarines')
        print(f'You attacked {i-1} times.')
        break   
    else:   
        print(f'Attack #{attacktimes}:') 
        x,y = get_attack_position(field)
        update(x, y, field, sub_names, curr_sizes, statuses) 
        i += 1
    ship = []