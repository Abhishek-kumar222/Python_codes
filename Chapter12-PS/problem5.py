num = int(input("Enter any number : "))
table = [i*num for i in range(1,11) ] # using conprehension function
print(table)

with open ("store.txt", "a") as f:
    f.write(f"The table of {num} is {str(table)} \n")