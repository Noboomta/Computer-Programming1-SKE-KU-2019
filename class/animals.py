class animals():
    
    brain = True
    
    def __init__(self, leg, tail):
        self.leg = leg
        self.tail = tail
       
    def display(self):
        print(self.leg)
        print(self.tail)
        
    def __str__(self):
        # return super().__str__()
        return str(self.leg)
    
    @classmethod
    def update_brain(cls, con):
        cls.brain = con
    
    @classmethod
    def create_by_line(cls,line):
        leg, tail = line.split("-")
        return cls(leg, tail)
        
    @staticmethod
    def plus(a,b):
        return a+b

    @property
    def fname(self,name):
        self.__name = name
        
human = animals(2,0)
print(human.leg)

line = "2-False"
animals.create_by_line(line)

print(human)