class Employee:
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
    

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(self.name,self.language)

a = Employee()
b = Programmer()

b.show("Abhi",1200000)

print(b.name)