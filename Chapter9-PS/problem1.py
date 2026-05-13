f = open("poem.txt")
content = f.read()
if("how" in content):
    print("The word how is present in the content ")
else:
    print("The word how is not present in the content ")
f.close()