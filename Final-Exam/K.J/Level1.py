class Student:
    
    def __init__(self, name = 'No Name'):
        self.__name = name
        self.__subject_list = []
    
    def __str__(self):
        return f'{self.name}'
    
    def add(self,subject):
        self.__subject_list.append(subject)
    def drop(self,subject):
        for subject_number,subj in enumerate(self.__subject_list):
            # print('ffffffffff')
            # print(subj,subject)
            # print('zzzzzzzzzzz')
            if subj.name == subject.name:
                self.__subject_list.pop(subject_number)
    def show(self):
        print(self)
        for subj in self.__subject_list:
            print(subj)
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newname):
        self.__name = newname
        
class Subject:
    def __init__(self, code = 'No Code', name = 'No Name', credit = 'No Credit'):
        self.__name = name
        self.__code = code
        self.__credit = credit
    
    def __str__(self):
        return f'{self.code}, {self.name}, {self.credit}'
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newname):
        self.__name = newname
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,newcode):
        self.__code = newcode
    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,newcredit):
        self.__credit = newcredit
    
John = Student()
print(John)
John.name = 'John'
Kevin = Student('Kevin')
print(Kevin)
Python = Subject()
Python.code = '01219114'
Python.name = 'Python'
Python.credit = 3
print(Python)
Math = Subject('011230111','Math', 3)
print(Math)