# find greatest of three number using function 
def greatest(a,b,c):
    # a = int(input("Enter Number "))
    # b = int(input("Enter Number "))
    # c = int(input("Enter Number "))
    if(a>b and a>c):
        print(f" {a} is greater ")
    elif(b>a and b>c):
        print(f" {b} is greater ")
    else:
        print(f" {c} is greater ")

a = int(input("Enter Number "))
b = int(input("Enter Number "))
c = int(input("Enter Number "))
greatest(a,b,c) # with perameter 