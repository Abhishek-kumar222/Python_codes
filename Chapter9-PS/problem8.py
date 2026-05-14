# copy file
with open("log.txt") as f:
    content = f.read()

with open("copy_log.txt", "w") as c:
    c.write(content)