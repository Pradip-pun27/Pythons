class person: # creating a parent class
    def __init__(self,fname,lname): # In-built function
        self.firstname = fname
        self.lastname = lname
    def Full_name(abc): # User-build function
        print(f"{abc.firstname} {abc.lastname}")
class boy(person): # creating a child class
    pass
a= boy("Ravi","kumar")
a.Full_name()

class human:
    def __init__(self,nam,ag):
        self.name = nam
        self.age = ag
    def printname(self):
        print(self.name,self.age)

class man(human):
    def __init__(self,nam,ag,loca):
        self.location = loca
        super().__init__(nam,ag)
    def wlcm(self):
        print(self.name,self.age,self.location)

b= man("Anu",16,"Nepal")
b.printname()
b.wlcm()
