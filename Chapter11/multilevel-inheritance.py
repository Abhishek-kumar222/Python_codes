# multilevel  Inheritance

class Employee: # level 1
    a=1

class Coder(Employee): # level 2
    b=2
    

class Programmer(Coder): # level 3 
    c=3
    

p = Programmer() 
print(p.a + p.b + p.c)

