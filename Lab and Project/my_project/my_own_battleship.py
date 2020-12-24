def print_field(field,symbols):
    
    for i in range( 2*len(field[0]) + 1):
        print("-", end  = " ")
    # print('-'*(2*(len(field[0]))+1))
    for i in range(len(field)):
        for j in range (len(field[i])):
            if (field[i][j]) == 0 and j == 0:
                print(f"| |",end ="")
            elif (field[i][j]) == -1 and j == 0:
                print(f"|X|",end ="")
            elif (field[i][j]) == -1:
                print(f"X|",end ="")
            elif j == 0:
                print(f'|{symbols[(field[i][j])-1]}|',end ='')
            elif (field[i][j]) == 0:
                print(' |',end ="")
            else:
                print(f'{symbols[(field[i][j])-1]}|',end ='') 

        print()
    print('-'*(2*(len(field[0]))+1))
    
def get_submarine_info(field,sub_names):
    
    orig_sizes = {x:0 for x in sub_names}
    curr_sizes = {x:0 for x in sub_names}
    statuses = {x:'T' for x in sub_names} 
    
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
            elif field[i][j] == 1:
                curr_sizes['Marlin'] += 1
            elif field[i][j] == 2:
                curr_sizes['Nautilus'] += 1
                
    return orig_sizes,curr_sizes,statuses

def display_result(sub_name,orig_sizes,curr_sizes,status):
    
    print(f'Submarine name:',end ='')
    for x in sub_name:
        print(f'{x:>10}',end ='')
    print("")
    print(f'Original size :',end ='')
    for x in sub_name:
        print(f'{orig_sizes[x]:>10}',end ='')
    print("")
    print(f'Current size  :',end ='')
    for x in sub_name:
        print(f'{curr_sizes[x]:>10}',end ='')
    print("")
    print(f'Status        :',end ='')
    for x in sub_name:
        print(f"{status[x]:>10}",end ='')
    print("")
    
    # return True #delllllll
def get_attack_position(field):
    attacktimes = 1
    while True:
        x = int(input("Enter x position (1-5): "))
        if x >=1 and x<=5:
            while True:
                y = int(input("Enter y position (1-6): "))
                if y >=1 and y<=6:
                    attacktimes +=1
                    return x,y
                else:
                    print('Invalid y position!')                    
        else:
            print("Invalid x position!")
            
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


original_size, current_size, status = get_submarine_info(field, sub_names)
atk_time = 0
print_field(field, symbols)
display_result(sub_names, original_size, current_size, status)

while True:

    atk_time += 1
    print("Attack #{}:".format(atk_time))
    x, y = get_attack_position(field)
    update(x, y, field, sub_names, current_size, status)
    print_field(field, symbols)
    display_result(sub_names, original_size, current_size, status)
    _F_num = 0
    for val in status.values():
        if val == 'F':
            _F_num += 1
    if _F_num > len(sub_names)/2:
        break
    #print()
    
print("Congratulations, you attacked 2 out of 3 submarines")
print("You attacked {} times.".format(atk_time))
