
def main():
 try:
    a = int(input("Enter any number : "))
    print(a)
    return

 except Exception as v:  # type of error value error
    print(v)
    return

 finally:
    print("i am inside finally : ") # function me use kiya jata h function break hone ke baad bhi execute hota h

main()