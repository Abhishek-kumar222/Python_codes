
# # before classmethod decorator

# class Employee:
#     a=2
#     def show(self):
#         print(self.a)
  
# e = Employee()
# e.a = 45
# e.show()

# After classmethod decorator

class Employee:
    a=2
    @classmethod  # it will help to print class attributes
    def show(cls):
        print(cls.a)
  
e = Employee()
e.a = 45
e.show()