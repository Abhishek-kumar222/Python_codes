# erroe raise karne ke liye
try:
 a = int(input("Enter a "))
 b = int(input("Enter b "))
 print(int(a/b))

except ZeroDivisionError as z:
  print("Zerodivision Error : ")
   