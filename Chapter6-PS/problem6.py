# calculate the grade with markse of students

marks = int(input("Enter your marks : "))
if(marks>=90 and marks<=100):
   print("You are passed with A+ grade")

elif(marks>=80 and marks<=89):
   print("You are passed with A grade")

elif(marks>=70 and marks<=79):
   print("You are passed with B grade")

elif(marks>=60 and marks<=69):
   print("You are passed with C grade")

elif(marks>=50 and marks<=59):
   print("You are passed with D grade")

elif(marks>=0 and marks<=49):
   print("You are failed try againg next year")

else:
   print("Enter valid marks under 0 to 100 !")