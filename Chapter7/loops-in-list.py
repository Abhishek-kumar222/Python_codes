fruts = ["Apple","Banana","graps","Orange","Papaya",1]
for frut in (fruts):
    print(frut)

i = 0 
while(i<len(fruts)):
    print(fruts[i])
    i=i+1

n = int(input("Enter n : "))
#for i in range(start , stop , step size)
for k in range(2 , n+1 , 2):
    print(k)