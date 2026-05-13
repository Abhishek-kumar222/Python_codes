# spam message detected 

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Write your message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This commment is a spam ")
else:
    print("not a spam ")
