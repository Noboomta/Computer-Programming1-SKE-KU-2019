money_list = []
money_name_list = []
money = 0
rice_list = []
rice_name_list = []
rice = 0

def display():
    print("")
    print("Rice list contain.")
    if(len(rice_list)>=1):
        for i in range(len(rice_list)):
            print(f"Rice from {rice_name_list[i]} = {rice_list[i]}")
        print("average of rice: ", sum(rice_list)/len(rice_list))
    
    print("Money list contain.")
    if(len(money_list)>=1):
        for i in range(len(money_list)):
            print(f"Money from {money_name_list[i]} = {money_list[i]}")
        print("average of money: ", sum(money_list)/len(money_list))
    print("")

def update_rice():
    donate = float(input("donate: "))
    name = str(input("name: "))
    rice_add = donate//30
    rice_name_list.append(name)
    rice_list.append(rice_add)

def update_money():
    donate = float(input("donate: "))
    name = str(input("name: "))
    money_name_list.append(name)
    money_list.append(donate)

def choice():
    choice = str(input("Enter donation choice (m/r): "))
    if choice.lower() == 'r' :
        update_rice()
    elif choice.lower() == 'm' :
        update_money()
    else:
        choice()

while True:
    choice()
    display()