# if elif else ladder

age = int(input("Enter your age : "))

if(age>=18):
    print("You are adult ")

elif(age<0):
    print("You Entered invaid age ")

elif(age==0):
    print("You are entering zero which is not a valid age ")
else:
    print("You are child ")