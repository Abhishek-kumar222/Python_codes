# find word "python present in log.txt file or not"

with open("log.txt") as f:
    content = f.read()
if("python" in content):
    print("yes")
else:
    print("no")
