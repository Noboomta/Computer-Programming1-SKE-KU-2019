import time

run =True
while run:
    try:
        press = str(input("(S)tart (E)lapse (Q)uit (D)isplay: ")).upper()
    except press.upper() not in ["S", "E", "Q", "S"]:
        print("FALSE")
        break
    except :
        print("NOT STR")
        break
    if press.upper() == 'S':
        start = time.time()
        e = time.time()- start
    elif press == 'E':
        e = time.time()- start
    elif press == 'Q':
        run = False
    elif press == 'D':
        # print(f"START Time(1970 00:00) == {start}")
        print(f"START Time == {start-start}")
        # print(f"Elapse Time(1970 00:00) == {e}")
        print(f"ELapse Time == {e}")
        