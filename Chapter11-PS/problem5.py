# Write a class Vector representing a vector of n dimensions. Overload the + operator and * operator which calculates the sum and the dot product of them.
class vector :
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def show(self):
        print(f"{self.i}i + {self.j}j +{self.k}k")

    def add(self,v2):
        a = (self.i + v2.i)
        b = (self.j + v2.j)
        c = (self.k + v2.k)
        print(f"The sum of vector is : {a}i + {b}j + {c}k")

    def mul(self,v2):
        m = (self.i * v2.i)
        n = (self.j * v2.j)
        o = (self.k * v2.k)
        print(f"The multiplay of vector is : {m}+{n}+{o} : {m+n+o}")


v1 = vector(2,4,6)
v2 = vector(1,3,5)
v1.show()
v2.show()

vector.add(v1,v2)
vector.mul(v1,v2)