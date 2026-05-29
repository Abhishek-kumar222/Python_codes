# Create a class 2DVector and use it to create another class representing a 3D vector.

class twoDvector:
    def __init__(self ,i,j):
        self.i=i
        self.j=j
           
    def show(self):
        print(f"the twodvector is : {self.i}i + {self.j}j") 


class threeDvector(twoDvector):
    def __init__(self ,i,j,k):
        super().__init__(i,j)
        self.k=k
       
    def show(self):
        print(f"the twodvector is : {self.i}i + {self.j}j + {self.k}k") 
 
 
o1 = twoDvector(1,2)
o2 = threeDvector(1,2,3)
o1.show()
o2.show()
