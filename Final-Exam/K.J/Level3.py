class Student:
    
    def __init__(self, name = 'No Name'):
        self.__name = name
        self.__subject_list = []
    
    def __str__(self):
        return f'# {self.name}'
    
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
        
run = True
student_list = []
subject_list = []



while run:
    # a = input()
    try:
        choose = str(input('(s)tudent, s(u)bject, (q)uit: ')).upper()
        # print((choose not in ['S','U','B']))
    except (choose not in ['S','U','B']):
        print('Incorrect Menu')
    
    if choose == 'S' or choose == 's':
        while True:
            try:
                pick = str(input('(a)dd a student, (s)how students, (b)ack: ')).upper()
            except pick not in ['A','S','B']:
                print('Incorrect Menu')
            
            if pick == 'A':
                new_student = str(input('Enter a student name: '))
                student_list.append(Student(new_student))
            
            elif pick == 'S':
                for studen in student_list:
                    print(studen)
            
            elif pick == 'B':
                break
                
            else:
                print("Incorrect Menu")

    elif choose == 'U':
        while True:
            try:
                pick2 = str(input('(a)dd a subject, (s)how subjects, (b)ack: ')).upper()
            except pick2 not in ['A','S','B']:
                print('Incorrect Menu')
            # try:
            #     pick = str('(a)dd a subject, (s)how subjects, (b)ack: ').upper()
            # except pick not in ['A','S','B']:
            #     print('Incorrect Menu')
                
            if pick2 == 'A':
                
                subcode = input('Enter the subject code: ')
                subname = str(input('Enter the subject name: '))
                subcredit = input('Enter the subject credit: ')
                subject_list.append(Subject(subcode,subname,subcredit))
            
            elif pick2 == 'S':
                for subj in subject_list:
                    print(subj)
            
            elif pick2 == 'B':
                break
        
            else:
                print("Incorrect Menu")
            
            
            
    elif choose == 'Q':
            print('Bye')
            run = False
    
    else:
        print('Incorrect Menu')
            
                