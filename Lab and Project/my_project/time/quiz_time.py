class Bus:
    route = dict
#    time type
    def __init__(self,name = ' ',bus_type = ' '):
        self.name = name
        self.route = [] 
        
class Route:

    def __init__(self,name=''):
        self.name = name
        self.name = []
    
    def show(self):
        for i in self.name:
            print(i)
        
        
    def menu(self):
        routemenu = str(input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ")).upper()
        if routemenu == 'A':
            pass
        elif routemenu == 'P':
            pass
        elif routemenu == 'R':
            pass
        elif routemenu == 'M':
            pass
        
    def Nroute(self,r):
        name = str(input("Enter route name : "))
        self.route[r].append([name])
        print(self.route[r])

class System:
    def __init__(self):
        pass

    def systemmenu(self):
        bigmenu = str(input("(n)ew Route, (s)how, (c)hoose, (q)uit : ")).upper()
        # print(bigmenu)
        r = -1
        if bigmenu == 'N':
            # print("N")
            return bigmenu
        elif bigmenu == 'S':
            print("S")
            pass
        elif bigmenu == 'C':
            print("C")
            route.menu(r)
            pass
        elif bigmenu == 'Q':
            print("Q")
            pass
        else:   print("ELSE")

r=0
system = System()
bus = Bus()
sysmenu = system.systemmenu()
print("HEY")
print(sysmenu)
if sysmenu == 'N':
    name = str(input("ENter route name : "))
    Route(name)
    Route.show()