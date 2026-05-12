def fect(n):
    if(n==1 or n==0):
        return 1
    return n*fect(n-1)

n=int(input("Enter number : "))
print(fect(n))