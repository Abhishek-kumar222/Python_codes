# celsius to fahrenhiet using function


def convert(cel):
   fehre = (((9/5)*cel)+32)
   return fehre


cel = int(input("Enter Celsius value : "))
print(f"fehrenhiet Value of {cel}'C : ",convert(cel),"F" )
