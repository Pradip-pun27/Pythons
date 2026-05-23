class person:
    def __init__(self,fname,lname): # In-built function
        self.firstname = fname
        self.lastname = lname
    def Full_name(abc): # User-build function
        print(f"{abc.firstname} {abc.lastname}")
       
p1=person("Ram","magar")
p2= person("Sita","kc")
print(p1.firstname, p1.lastname)
print(p2.firstname,p2.lastname)
p2.Full_name()
p1.Full_name()


class human:
    def __init__(self,nam,ag):
        self.name = nam
        self.age = ag

    def __str__(jpt):
        return f"{jpt.name} is {jpt.age}"
    
h1=human("Rmaesh",14)
print(h1)
del h1.age
print(h1.age)
