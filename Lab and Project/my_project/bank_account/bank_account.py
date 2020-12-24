from error import AccountNotFound, InsufficientFund

account_database = [
    {"account_number":"246-35-37789", "type":"saving", "account_name":"David Patterson", "balance":92456},
    {"account_number":"246-67-24554", "type":"checking", "account_name":"John Hennessy", "balance":77843},
    {"account_number":"246-44-77534", "type":"saving", "account_name":"Mark Hill", "balance":1245},
    {"account_number":"246-44-19233", "type":"saving", "account_name":"David Wood", "balance":220441}
]

def create_account(num, type, name, init_balance):
    try:
        index = search_account_db(num)
    except AccountNotFound:
        account = {}
        account["account_number"] = num
        account["type"] = type
        account["account_name"] = name
        account["balance"] = init_balance
        account_database.append(account)
    else:
        print("Account", num, "already exists")

def delete_account(num):
    try:
        index = search_account_db(num)
    except AccountNotFound:
        print(num, "account is invalid; nothing to be deleted.")
    else:
        del account_database[index]

def search_account_db(num):
    for i in range(len(account_database)):
        if account_database[i]["account_number"] == num:
            return i
    raise AccountNotFound

def deposit(account_num, amount):
    try:
        index = search_account_db(account_num)
        account_database[index]["balance"] += amount
    except AccountNotFound:
        print(account_num, "account is invalid; no deposit action performed.")

def witdraw(account_num, amount):
    try:
        index = search_account_db(account_num)
        if account_database[index]["balance"] >= amount:
            account_database[index]["balance"] -= amount
        else:
            raise InsufficientFund
    except AccountNotFound:
        print(account_num, "account is invalid; no witdrawal action performed.")
    except InsufficientFund:
        print(amount, "witdrawal amount exceeds the balance of", account_database[index]["balance"], "for", account_num, "account.")

def show_account(account_num):
    try:
        index = search_account_db(account_num)
        print(account_database[index])
    except AccountNotFound:
        print(account_num, "account is invalid; nothing to be shown for.")
