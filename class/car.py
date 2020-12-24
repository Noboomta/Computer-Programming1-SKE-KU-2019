class Car():
    
    def __init__(self, brand = '_', model = '_', price = 0):
        self.brand = brand
        self.model = model
        self.price = price
        
    def __str__(self):
        return f"Brand: {self.brand} , Model: {self.model} , Price: {self.price}"

class Car2():
    
    def __init__(self, brand = '_', model = '_', price = 0):
        self.__brand = brand
        self.__model = model
        self.__price = price
        
    def __str__(self):
        return f"Brand: {self.__brand} , Model: {self.__model} , Price: {self.__price}"
    
    @property
    def brand(self):
        self.__brand  
    @brand.setter
    def brand(self,newbrand):
        self.__brand = newbrand
        
    @property
    def model(self):
        self.__model    
    @brand.setter
    def model(self,newmodel):
        self.__model = newmodel
        
    @property
    def price(self):
        self.__price     
    @price.setter
    def price(self,newprice):
        self.__price = newprice
    
def compare(a,b):
    print(a)
    print(b)

car1 = Car()
print(car1)
car1.brand = "Toyota"
print(car1)
car1.model = "Vios"
car1.price = 500000
print(car1)
car2 = Car("BMW","X3",3500000)
print(car2)
car2.price = 2000000
print(car2)

car1 = Car("Nissan","Tiida",450000)
car2 = Car("Totoya","Vios",400000)
car3 = Car("BMW","X3",3400000)
compare(car3,car1)
compare(car1,car2)

