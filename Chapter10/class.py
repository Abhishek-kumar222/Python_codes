# creating a class 
class Employee:
    language = "Python" # this is class attributes
    salary = 1200000

Abhi = Employee() # object creation

print(Abhi.language,Abhi.salary)
Abhi.name = "Abhishek"  # this is an object attributes or we can call instance attributes
print(Abhi.name,Abhi.language,Abhi.salary)

Anshika = Employee() # object creation
Anshika.name = "Anshika "

print(Anshika.name,Anshika.language,Anshika.salary)


# here name is a object attributes and language and salary are class attributes as they belongs to the class
