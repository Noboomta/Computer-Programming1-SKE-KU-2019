from OO_bank_account import BankAccount

account1 = BankAccount("246-35-37789", "saving", "David Patterson", 92456)
account2 = BankAccount("246-67-24554", "checking", "John Hennessy", 77843)
account3 = BankAccount("246-44-77534", "saving", "Mark Hill", 1245)
account4 = BankAccount("246-44-19233", "saving", "David Wood", 220441)
BankAccount.show_all()
print("account3 info:")
account3.show_account()
account3.deposit(5000)
print("account3 info:")
account3.show_account()
account3.witdraw(15000)
print("account3 info:")
account3.show_account()
account3.remove()
print("account3 info:")
account3.show_account()

"""
Expected output:

List all accounts:
246-35-37789 saving David Patterson 92456
246-67-24554 checking John Hennessy 77843
246-44-77534 saving Mark Hill 1245
246-44-19233 saving David Wood 220441
account3 info:
246-44-77534 saving Mark Hill 1245
account3 info:
246-44-77534 saving Mark Hill 6245
15000 witdrawal amount exceeds the balance of 6245 for 246-44-77534 account
account3 info:
246-44-77534 saving Mark Hill 6245
account3 info:
246-44-77534 account is invalid; nothing to be shown for

"""
