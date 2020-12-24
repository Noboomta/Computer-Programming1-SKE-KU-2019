hello = 0
bye = 0
while True:
    m = int(input("Enter m: "))
    if m <=0:
        print("You print Hello for {0} lines".format(hello))
        print("You print Bye for {0} lines".format(bye))
        break
    n = int(input("Enter n: "))
    for i in range(m):
        print(f"Hello #{i}")
        hello += 1
    for j in range(n):
        print(f"Bye {m-1} {j}")
        bye += 1
        