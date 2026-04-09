import os
# Select the directory whose content you want to list
directory_path = '/'

# Use the os module to list the directory contents
contents = os.listdir(directory_path)

# print the contents of the directory
for item in contents:
    print (item)