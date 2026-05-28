class Employee:
    # @property # method ko variable ki tarah use karega
    def name(self):
        return f"{self.fname} {self.lname}"
    
    # @name.setter # value set karega
    def name (self , value):
        self.fname = value.split(" ")[0] # value me value aai Abhi kumar split me list bani or     indexing ke hisaab se store ho gya
        self.lname = value.split(" ")[1]

e = Employee()
e.name = "Abhi Kumar"
print(e.name)  # without @property decorater = print(e.name())
