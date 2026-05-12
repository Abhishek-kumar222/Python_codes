def GoodDay(name,ending):
    print("Good Day," + name )
    print(ending)

GoodDay("Abhi","Thanks")
GoodDay("Anshika","Thanks")


# with return value
def GoodDay(name,ending):
    print("Good Day," + name )
    print(ending)
    return "done"

a = GoodDay("Abhi","Thanks")
print(a)