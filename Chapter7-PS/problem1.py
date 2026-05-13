# for the table of any no. given by user by for loop

n = int(input("Enter any number : "))
print(f"Table of {n} : ")
for i in range(n,(n*10+1),n):
    print(i)

# another way
for k in range(1,11):
    print(f"{n} X {k} = ",n*k)