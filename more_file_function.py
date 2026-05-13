f = open("file.txt")

# # for all lines
# lines = f.readlines() # returns list  of multiple line which is present in file.txt file
# print(lines,type(lines))

# for single line
line1 = f.readline() # returns single line which is present in file.txt file
print(line1,type(line1))

line2 = f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))