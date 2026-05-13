# conversion inches to cms using function

def inch_to_cm(inch):
    cm = (2.54*inch)
    return cm


inch = int(input("Enter value in inch : "))
print(f"{inch} inches is equls to : ",inch_to_cm(inch),"CentiMeters")