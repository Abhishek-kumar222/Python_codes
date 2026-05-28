class Number:

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n #self.n.__add__other.n


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

#     2 + 5          =     2.__add__5  means ineteger ko add kar rha h 
# "abhi" + "kumar"   = abhi.__add__ means same operator string ko bhi add kar rha h  