# variable type hint

age : int = 21 # variable ka datatype batane ke liye 

# function type hints
def greeting(name: str) -> str: # ye function strign return karega
    return f"hello ,{name} ! "

# usage
print(greeting("Abhishek"))

def sum(a:int,b:int)->int:
    return (a+b)
print(sum(2,4))