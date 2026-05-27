# multilevel  Inheritance

class Employee: # level 1
    def __init__(self):
        print("Contructor of Employee ; ")

class Coder(Employee): # level 2
    def __init__(self):
        super().__init__() # it will costructor of parents class 
        print("Contructor of coder ; ")

class Programmer(Coder): # level 3 
    def __init__(self):
        super().__init__() # it will costructor of parents class 
        print("Contructor of programmer ; ")
    

p = Programmer() 

