#vehicle class with model,regno,color
#printing the reference can get an address ........object at the address

#we will give 2 string method,common ayi kodukanda code kodkuka
#each object address can replace by string....return il 2 values kodkan +operator kodukkanam(string concatenation)

class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def printv(self):
        print(self.model,self.color,self.regno)

    def __str__(self):
        return self.model+self.color

ve=Vehicle("KTM","KL12AE3456","Black")
ve.printv()
print(ve)