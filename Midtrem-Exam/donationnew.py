money_list = []
name_list = []
milk_list = []
money_namelist = []
milk_namelist = []
total_donation = 0
# def display_final(list_, namelist):
#     print("Money (Baht):")
#     for i in range(len(money_list)):
#         print(f"({name_list[i]}: {money_list[i]:.2f})",end= ",")
#     avg = 0
#     for index,value in enumerate(money_list):
#         avg+=value
#     print(f"\nAverage donation = {avg/len(money_list):.2f}")
#     print("Milk (Pack):")
#     for i in range(len(money_list)):
#         print(f"({money_namelist[i]}: {milk_list[i]:.2f})",end= ",")
#     avg = 0
#     for index,value in enumerate(milk_list):
#         avg+=value
    
def display_list(total_donation, money_list, milk_list):
    print("Current donation:")
    print("Money({0} donators) = {1:.2f} Baht".format(len(money_list),sum(money_list)))
    print("Milk ({0} donators) = {1:.0f} packs".format(len(milk_list),sum(milk_list)))
    print("Total donation = {0:.2f} Baht".format(total_donation))

def display_final(list_, namelist):
    for i in range(len(list_)):
        # print("({0}: {1:.2f}),".format(namelist[i],list_[i]),end=" ")
        print(f"({namelist[i]}: {list[i]:.2f}),",end = " ")
    print("\nAverage donation = {0:.2f}".format(sum(list_)/len(list_)))

# def update_milk_list (amount, name, milk_list, milk_namelist, money_list, money_namelist):
#     return None

def update_milk_list (amount, name, milk_list, milk_namelist, money_list, money_namelist):
    if amount>1000 :
        milk_list.append(amount//1000)
        milk_namelist.append(name)
        if amount%1000 != 0:#เศษ
            money_list.append(amount%1000)
            money_namelist.append(name)
    return None

def choice(choice):
    if choice.upper() == 'M' or choice.upper() == 'K':
        pass
    else:   print("Wrong choice. Strat over.")
while True:
    donation_amount = float(input("Enter donation amount: "))
    if donation_amount<0:
        break
    else:
        choice = str(input("Enter donation choice (m/k): "))
        total_donation += donation_amount
        # money_list.append(donation_amount)
        donator = str(input("Enter your name: "))
        if choice.upper() == 'M':
            money_list.append(donation_amount)
            money_namelist.append(donator)
        elif choice.upper() == 'K':
            update_milk_list(donation_amount,donator,milk_list,milk_namelist,money_namelist)
        else:   print("Wrong choice. Strat over.")
        display_list(money_list,total_donation,milk_list)
display_final(money_list,money_namelist)
