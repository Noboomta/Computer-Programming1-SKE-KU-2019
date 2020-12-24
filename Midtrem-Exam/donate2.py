import math,sys
total_donation = 0
money = 0
rice = 0
milk = 0

def display(rice,milk,money,total_donation):
    
    print("Current donation:")
    print(f"Money = {money:.2f} Baht")
    print(f"Rice = {rice:.2f} kg")
    print(f"Milk = {milk:.0f} packs")
    print(f"Total donation = {total_donation:.2f} Baht")
    print("")

def update_milk(donate_amount,milk,money):
    left_money = donate_amount%1000
    milk_add = donate_amount//1000
    milk+=milk_add
    return milk,left_money

def update_rice(donate_amount,rice):
    rice+= (donate_amount/30)
    return rice

def update_money(donate_amount,total_money):
    total_money += donate_amount
    return total_money

def update_total_donation(money,total_donation):
    total_donation+=money
    return total_donation

def choice(money,rice,milk,total_donation,donate_amount):
    
    choice = str(input("Enter donation choice (m/r/k): "))
    if choice.lower() == 'r' :
        total_donation += donate_amount
        rice = update_rice(donate_amount,rice)
        return money,rice,milk,total_donation,donate_amount
        
    elif choice.lower() == 'm' :
        total_donation += donate_amount
        money = update_money(donate_amount,money)
        return money,rice,milk,total_donation,donate_amount
    
    elif choice.lower() == 'k' :
        total_donation += donate_amount
        milk,left_money = update_milk(donate_amount,milk,money)
        money+= left_money
        return money,rice,milk,total_donation,donate_amount
        
    else:
        print("Wrong choice. Start over.")
        return money,rice,milk,total_donation,donate_amount

while True:
    try:
        donate_amount = float(input("Enter donation amount: "))
    except:
        continue
    if donate_amount < 0:
        sys.exit()
    money,rice,milk,total_donation,donate_amount = choice(money,rice,milk,total_donation,donate_amount)
    display(rice,milk,money,total_donation)