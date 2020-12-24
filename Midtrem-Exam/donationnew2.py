def update_milk_list (amount, name, milk_list, milk_namelist, money_list, money_namelist):
    """ Update lists of milk and monday donation and donators.
        >>> update_milk_list (4000, 'evan', [2], ['dave'], [1000, 500], ['ann', 'dave'])
        # print nothing
        >>> update_milk_list (3200, 'ryan', [2], ['nina'], [500, 1050.25], ['nina', 'owen'])
        # print nothing
    """
    if amount//1000 != 0:
        milk_list.append(amount//1000)
        milk_namelist.append(name)
        if amount%1000 != 0:
            money_list.append(amount%1000)
            money_namelist.append(name)
    return None
def display_list(total_donation, money_list, milk_list):
    """ Display values of current donation and total_money on screen
        >>>  display_list(10500, [1500], [2])
        Current donation:
        Money (1 donators) = 1500.00 Baht
        Milk (1 donators) = 2 packs
        Total donation = 10500.00 Baht
    """
    print('Current donation: ')
    print(f'Money ({len(money_list)} donators) = {sum(money_list):.2f} Baht')
    print(f'Milk ({len(milk_list)} donators) = {sum(milk_list):.0f} packs')
    print(f'Total donation = {total_donation:.2f} Baht\n')
def display_final(list_, namelist):
    """ Display values of final donation on screen
        >>>  display_final([100], ['bob'])
        (bob: 100.00),
        Average donation = 100.00
        >>>  display_final([1000, 500], ['ann', 'dave'])
        (ann: 1000.00), (dave: 500.00),
        Average donation = 750.00
    """
    for i in range(len(list_)):
        print("({0}: {1:.2f}),".format(namelist[i],list_[i]),end=" ")
    print()
    print("Average donation = {0:.2f}".format(sum(list_)/len(list_)))
money_list = []
money_namelist = []
milk_list = []
milk_namelist = []
total_donation = 0
amount = float(input("Enter donation amount: "))

while amount > 0:
    item = str(input("Enter donation choice (m/k): "))
    name = str(input("Enter your name: "))
    if item.lower() == "m":
        money_list.append(amount)
        total_donation += amount
        money_namelist.append(name)
    elif item.lower() == "k":
        update_milk_list(amount, name, milk_list, milk_namelist, money_list, money_namelist)
        total_donation += amount
    else:
        print("Wrong choice. Start over.")
    display_list(total_donation,money_list,milk_list)
    print()
    try:
        amount = float(input("Enter donation amount: "))
    except:
        break

print("Final donation:")
print("Money (Baht):")
display_final(money_list,money_namelist)
print("Milk (pack):")
display_final(milk_list,milk_namelist)