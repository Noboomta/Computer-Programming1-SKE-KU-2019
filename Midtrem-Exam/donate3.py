import math,sys
rice_list,money_list,milk_list,list_donation,list_name=[],[],[],[],[]
total_donation = 0
def update_rice_list(donation_amount,name,rice_list,rice_name):
    
    
def update_milk_list(donate_amount,name,milk_list,money_list,money_name):
    left_money = donate_amount%1000
    milk_add = donate_amount//1000
    milk+=milk_add
    return milk_list,left_money

def display_list(money_list,rice_list,milk_list):
    print("Current donation:")
    print(f"Money = {money:.2f} Baht")
    print(f"Rice = {rice:.2f} kg")
    print(f"Milk = {milk:.0f} packs")
    print(f"Total donation = {total_donation:.2f} Baht")
    print("")
    
def display_final(list_donation,list_name):
    
    sys.exit()
    
def update_money_list(money_list,rice_list,milk_list,total_donation,list_donation,list_name):
    return money_list
    
def choice(money_list,rice_list,milk_list,total_donation,list_donation,list_name):
    
    choice = str(input("Enter donation choice (m/r): "))
    if choice.lower() == 'r' :
        total_donation += donate_amount
        rice = update_rice_list(donate_amount,rice)
        return money_list,rice_list,milk_list,total_donation,list_donation,list_name
        
    elif choice.lower() == 'm' :
        total_donation += donate_amount
        money = update_money_list(donate_amount,money)
        return money_list,rice_list,milk_list,total_donation,list_donation,list_name
    
    elif choice.lower() == 'k' :
        total_donation += donate_amount
        milk,left_money = update_milk_list(donate_amount,milk,money)
        money+= left_money
        return money_list,rice_list,milk_list,total_donation,list_donation,list_name
        
    else:
        print("Wrong choice. Start over.")
        return money_list,rice_list,milk_list,total_donation,list_donation,list_name

    
while True:
    donate_amount = float(input("Enter donation amount: "))
    if donate_amount < 0:
        display_final
    money_list,rice_list,milk_list,total_donation,list_donation,list_name = choice(money_list,rice_list,milk_list,total_donation,list_donation,list_name)
    display_final(list_donation,list_name)
