#table of given number using function 
def table(num):
    for i in range(1,11):
        print(num*i)

num = int(input("Enter number : "))
table(num)