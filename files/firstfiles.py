# fil = input("Enter file name: ")
# # line = open(fil).read().splitlines(",")
# a = "1,2,3,'s'"
# linee = [i for i in a]

# # for i in range(len(linee)):
# #     # print(f"Line {i+1}: {line[i]}")
# #     print("{0:<5}".format(linee[i]))
# b = a.split(",") 
# print(b)

def grade_point(grade):
    if grade == "A":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3.0  
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1.0
    elif grade == "F":
        return 0.0

fil = input("enter file name: ")
line = open(fil).read().splitlines()
print(line)
table = [x.split(",") for x in line if x!= ""]
print(table)
print('-'*37)
print("    Subject Credits Grade   Point")
for i in range(len(table)):
    print("    ",end = "")
    for j in range(len(table[i])):
        print("{0:<8}".format(table[i][j]),end="")
    print(grade_point(table[i][-1]),end = "")
    print("")
print('-'*37)

d = [[1,2],[12,3],[2,1]]
from operator import itemgetter
print(sorted(d,key = itemgetter(1),reverse = True))


