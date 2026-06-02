# erroe raise karne ke liye

a = int(input("Enter a "))
b = int(input("Enter b "))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero ")
else:
    print(int(a/b))