class Employee:
    language = "Python" # this is class attributes
    salary = 1200000
    def getInfo(self):
       print(self.language) # self is self perameter
    
    def gm(self):# we have to pass self parameter  even we have to print single line of code
        print("Good Morning!")

    @staticmethod # jis function me hume object ka kamm nhi hota waha static method use karte h
    def greet(): 
        print("this is static method!")

Abhi = Employee() 
Abhi.language = "Java" # instane attributes
# Abhi.getInfo() # == Employee.getInfo(Abhi)
Employee.getInfo(Abhi)
Abhi.gm() # both calling way are same
Abhi.greet()

# print(Abhi.language,Abhi.salary)