# recursive function for sum of first n natural number 
def sum_natural(num):
   if(num==0):
      return 0
   
   return num+sum_natural(num-1)

num = int(input("Enter number : "))
print(f"Sum of first {num} natural number is : ",sum_natural(num))