s = "Hello World"
print(s.lower())  # hello world
print(s.upper())  # HELLO WORLD

s = "  hello  "
print(s.strip())  # hello

s = "I like Java"
print(s.replace("Java", "Python"))  # I like Python

s = "apple,banana,mango"
print(s.split(","))  # ['apple', 'banana', 'mango']

lst = ["apple", "banana", "mango"]
print(", ".join(lst))  # apple, banana, mango

s = "hello world"
print(s.find("world"))  # 6

s = "python"
print(s.startswith("py"))  # True
print(s.endswith("on"))    # True

print("abc".isalpha())   # True
print("123".isdigit())   # True
print("abc123".isalnum()) # True

s = "hello world"
print(s.capitalize())  # Hello world
print(s.title())       # Hello World