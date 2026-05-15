# chaecking after creating instance attributes class attributes change not

class Demo:
    a = 4

O = Demo()
print(O.a) # prints class attributes becaouse instance attribute is no present
O.a=5
print(O.a)# prints instance attributes becaouse instance is present
print(Demo.a) # prints the class attributes 

# and the answer is no class attribute did not change call with class name