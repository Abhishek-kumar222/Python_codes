# multiple Inheritance

class Employee: #parent class
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(name,salary)

class Coder: #parent class
    def getLang(self,lang):
       self.lang = lang
       print(lang)
    

class Programmer(Employee,Coder): # child class
    pass


b = Programmer() # object of child class

b.show("Abhi",1200000) # accesing the method of parents class
b.getLang("python") # same
