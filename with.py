# open the file in read mode using with statement 
with open("file.txt") as f:

  data= f.read()  # READ THE FILE
  print(data)
# now we dont have need to close the file 