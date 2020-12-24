from OO_error import AccountNotFound, InsufficientFund

class BankAccount:

    __account_database = []
    class_name = "BankAccount"
 
    def __init__(self, num, type, name, init_balance):
        self.account_number = num
        self.type = type
        self.account_name = name
        self.balance = init_balance
        self.__account_database.append(self)

    def remove(self):
        pass

    def deposit(self, amount):
        pass

    def witdraw(self, amount):
        pass

    def show_account(self):
        pass

    @classmethod    
    def show_all(cls):
        print("List all accounts:")
        for acc in cls.__account_database:
            print(acc.account_number, acc.type, acc.account_name, acc.balance)


