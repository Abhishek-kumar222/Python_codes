# calculator 
import math
class Calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        print("the square is ",self.n**2)
    
    def cube(self):
        print("the cube is ",self.n**3)
        
    def squareRoot(self):
        print("the cube is ",self.n**1/2)

no = int(input("Enter no : "))
O = Calculator()
O.square(4)
O.cube()
O.squareRoot()
        