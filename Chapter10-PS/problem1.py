# create a class for storing few information 
class programmer:

    def __init__(self,name,age,salary,address,company):
      self.name = name
      self.age = age
      self.salary = salary
      self.address = address
      self.company = company


Abhi = programmer("Abhishek",22,100000,"jabalpur","Microsoft")
Sandeep = programmer("Sandeep",30,160000,"Hydrabad","Microsoft")
Abhinav = programmer("Abhinav",25,120000,"pune","Microsoft")

print(Abhi.name,Abhi.age,Abhi.salary,Abhi.address,Abhi.company)
print(Abhinav.name,Abhinav.age,Abhinav.salary,Abhinav.address,Abhinav.company)
print(Sandeep.name,Sandeep.age,Sandeep.salary,Sandeep.address,Sandeep.company)