import random
ans1 = random.randint(1, 6)
ans = []
gues = []

def check(ans,gues):
    orga = []
    for i in ans:
        orga.append(i)
    index = 0
    same = 0
    for index_ans,ansx in enumerate(ans):
        for index_gues,guesx in enumerate(gues):
            if index_ans == index_gues and ansx == guesx:
                index += 1
    for i in gues:
        if i in ans:
            same  += 1
            ans.remove(i)
    print(f"your guess = {gues}")
    print(f"orga = {orga}")
    gues = []
    # print(f"ans = {ans}")
    print(f"indexTrue = {index} , ValueSame = {same}")
    print("*"*index,end='')
    print("o"*int(same-index))
    
    
    
    return orga,gues    
    

for i in range(4):
    ans.append( random.randint(1, 6) )

print(ans)

while True:
    try:
        guess = str(input("Enter : "))
    except:
        print("Error input")
    for i in guess:
        gues.append(int(i))
    # print(gues)
    
    ans,gues = check(ans,gues)