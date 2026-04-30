# greatest of four num. 

num1 = int(input("Enter Number num1 : "))
num2 = int(input("Enter Number num2 : "))
num3 = int(input("Enter Number num3 : "))
num4 = int(input("Enter Number num4 : "))

if(num1>num2):
    if(num1>num3):
        if(num1>num4):
            print(f"{num1} is greater ")
        else:
            print(f"{num4} is greater " )
    elif(num3>num4):
        print(f"{num3} is greater ")
    else:
        print(f"{num4} is greater ")
elif(num2>num3):
        print(f"{num2} is greater ")
elif(num3>num4):
        print(f"{num3} is greater ")
else:
    print(f"{num4} is greater ")
     
# same output  but in different (short) code

if(num1>num2 and num1>num3 and num1>num4):
   print(f"{num1} is Greater")

if(num2>num1 and num2>num3 and num2>num4):
 print(f"{num2} is Greater")

if(num3>num2 and num3>num1 and num3>num4):
 print(f"{num3} is Greater")

if(num4>num2 and num4>num3 and num4>num1):
 print(f"{num4} is Greater")