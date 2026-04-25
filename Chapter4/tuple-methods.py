


t = (1, 2, 2, 3)

t.count(2)   # 2
t.index(3)   # 3

#🔹 More Useful Operations with Tuples

#1. 🔸 Tuple Packing & Unpacking
t = (10, 20, 30)   # packing

a, b, c = t        # unpacking
print(a, b, c)     # 10 20 30
#👉 Very important for interviews!


# 2. 🔸 Nested Tuples
t = (1, (2, 3), (4, 5))
print(t[2][1])   # Output: 5  PRINT (t[outer index][fir uske ander ka index])


# 3. 🔸 Tuple Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)
# Output: (1, 2, 3, 4)


# 4. 🔸 Tuple Repetition
t = (1, 2)
print(t * 3)
# Output: (1, 2, 1, 2, 1, 2)


# 5. 🔸 Membership Operators
t = (1, 2, 3)
print(3 in t)     # True
print(2 not in t) # false


# 6. 🔸 Iteration
t = (10, 20, 30)
for i in t:
    print(i)

# 7. 🔸 Slicing
t = (0, 1, 2, 3, 4)
print(t[1:4])   # (1, 2, 3)


# 8. 🔸 Converting Tuple
t = (1, 2, 3)
l = list(t)     # tuple → list
t2 = tuple(l)   # list → tuple