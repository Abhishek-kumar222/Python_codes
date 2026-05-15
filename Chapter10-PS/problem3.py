# Train status
from random import randint 
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"The ticket is booked in train no = {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train {self.trainNo} is runnig !")

    def getFare(self, fro,to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,555)}")

t = Train(12399)
t.book("Delhi","Hydrabad")
t.getFare("Delhi","Hydrabad")
t.getStatus()
