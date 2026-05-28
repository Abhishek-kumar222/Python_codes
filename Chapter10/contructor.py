class Employee:
    language = "Python" 
    salary = 1200000

    def __init__(self,name , lang, salary): # it is dunder method it called automaticaly
        print("This is constructor it will call autometically while cearting an object without calling ")
        self.name= name
        self.lang= lang
        self.salary= salary

    def getInfo(self):
       print(self.language) 
    
    def gm(self):
        print("Good Morning!")

    @staticmethod 
    def greet(): 
        print("this is static method!")

Abhi = Employee("Abhishek","CPP",120000) 
Abhi.language = "Java" 
Employee.getInfo(Abhi)
Abhi.gm() 
Abhi.greet()
print(Abhi.name,Abhi.salary,Abhi.lang)

