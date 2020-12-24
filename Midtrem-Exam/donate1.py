# donate_amount = float(input("Enter donation amount: "))
# total_donation = donate_amount
import math,sys
total_donation = 0
money = 0
rice = 0

def choice(money,rice,total_donation,donate_amount):
    
    choice = str(input("Enter donation choice (m/r): "))
    if choice.lower() == 'r' :
        total_donation += donate_amount
        rice+= donate_amount/30
        return money,rice,total_donation,donate_amount
        
    elif choice.lower() == 'm' :
        total_donation += donate_amount
        money+= donate_amount
        return money,rice,total_donation,donate_amount
        
    else:
        print("Wrong choice. Start over.")
        return money,rice,total_donation,donate_amount
            

while True:
    donate_amount = float(input("Enter donation amount: "))
    if donate_amount < 0:
        sys.exit()
    # total_donation += donate_amount
    # choice = str(input("Enter donation choice (m/r): "))
    # if choice.lower() == 'r' :
    #     rice+= donate_amount/30
    # elif choice.lower() == 'm' :
    #     money+= donate_amount
    # else:
    #     print("Wrong choice. Start over.")
    money,rice,total_donation,donate_amount = choice(money,rice,total_donation,donate_amount)
    print("Current donation:")
    print(f"Money = {money:.2f} Baht")
    print(f"Rice = {rice:.2f} kg")
    print(f"Total donation = {total_donation:.2f} Baht")
    print("")
    