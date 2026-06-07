a = 89

def fun():
    global a  # changes local variable to global variabl
    a = 12
    print(a)

fun()
print(a)
