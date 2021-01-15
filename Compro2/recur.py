# color = ["red", "blue", "red"]
# color = color[0:2].append("purple") + color[2:]
# color[2:2] = ["purple"]
# print(color)
class node:
    def __init__(self, name, next=None, last=None):
        self.name = name
        self.next = next
        self.last = last
    def __str__(self) -> str:
        return f"Name = {self.name}"

c1 = node("1")
c2 = node("2")
c3 = node("3")
c4 = node("4")
c5 = node("5")
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5

a = int(input("track : "))
s = str(input("color: "))
new_c = node("c6")
new_c.next = c4.next
c4.next = new_c


start = c1

while(start.next != None):
    print(start)
    start = start.next