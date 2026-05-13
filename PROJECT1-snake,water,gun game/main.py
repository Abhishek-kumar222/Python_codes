# Game - snake , water , gun 
'''
-1 for snake
0 for gun
1 for water  
'''

import random

computer = random.choice([-1,0,1])
yourstr = input("Enter your choise : ")
dict1 = {"s":-1,"w":1,"g":0}
dict2 = {-1 : "Snake",1:"Water",0:"Gun"}
you = dict1[yourstr]

print(f"You chose : {dict2[you]} \n Computer chose : {dict2[computer]}")
if(computer==you):
    print("It's Draw ! Play Again")
else:
    if(computer == -1 and you == 1):
        print("You Loss ! ")

    elif(computer == -1 and you == 0):
        print("You Win ! ")

    elif(computer == 1 and you == -1):
        print("You Win ! ")

    elif(computer == 1 and you == 0):
        print("You Loss ! ")

    elif(computer == 0 and you == 1):
        print("You Win ! ")

    elif(computer == 0 and you == -1):
        print("You Loss ! ")
    else:
        print("Somthing went wrong please try again ! ")