name = "Abhishek"

shortName = name[0:5] # from index 0 to 4 tak print karega 5 inculde nhi hoga
print(shortName)
print(name[0])# we can print single charecter also

#negative slicing -> isme indexing peeche se -1 se start hoti h 
print(name[-4:-1]) # -1 include nhi hoga 
# or change into positive indexing  
print(name[4:7]) # its for this perticular string


print(name[:7]) # is same as print(name[0:7]) 
print(name[1:]) # is same as print(name[1:8]) 