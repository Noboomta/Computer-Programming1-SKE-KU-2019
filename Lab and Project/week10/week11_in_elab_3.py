hello = 0
bye = 0
while True :  
    m = int(input("Enter m: ")) 
    if m<0:
        print("You print Hello for {0} lines".format(hello))
        print("You print Bye for {0} lines".format(bye))
        break
    n = int(input("Enter n: "))
    for i in range(n):
        print("Bye #{}".format(i))
        bye += 1
        for j in range(m):
            print("Hello {} {}".format(j, i))
            hello += 1
    
