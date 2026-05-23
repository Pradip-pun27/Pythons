class Human:
    def __init__(self,name,age,address):
        self.n=name  #variable(Public)
        self._a=age #variable(Protected) single underscore as prefix, can access but discouraged
        self.__ad=address #variable(Private) double underscore as prefix, name mangled
h=Human('Ram',14,'Dang')
print(h.n)
print(h._a) # Discouraged
print(h._Human__ad) #This one also discouraged, Accessing protected and private varibales outside from the class is discouraged unless explicitly required