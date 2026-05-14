class Employee:
    language = "Python" # this is class attributes
    salary = 1200000

Abhi = Employee() 
Abhi.language = "Java" # instane attributes
print(Abhi.language,Abhi.salary)

# instance attributes has more preferance than class attributs java wil print
