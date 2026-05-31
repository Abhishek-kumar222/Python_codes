# Error ko handale karne ke liye

try:
    a = int(input("Enter any number : "))
    print(a)

except ValueError as v:  # type of error value error
    print(v)

except Exception as e: # program crash nhi hoga kaha galat h wo batayega
    print(e)

print("thank you ! ")