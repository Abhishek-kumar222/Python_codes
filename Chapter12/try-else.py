# Error ko handale karne ke liye

try:
    a = int(input("Enter any number : "))
    print(a)

except Exception as v:  # type of error value error
    print(v)

else:
    print("i am inside else : ") # try chalega tabhi else chalega nhi to nhi chalega

