class Person: #Old Java approach to getter and setter method
    def __init__(self,name,age):
        self.__n=name
        self.__a=age
    def get_age(self):
        return self.__a
    def set_age(self,new_age):
        if (isinstance(new_age,int) and new_age>0):
            self.__a=new_age
        else:
            print("Age can't neither be other than  number and  nor be <0")


p1=Person("ram",11)
print(p1.get_age())
p1.set_age(21)
print(p1.get_age())

#New Python's approach to getter and setter method
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            print("Name must be a non-empty string")
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            print("Age must be a positive integer")

# Example usage
p1 = Person("ram", 11)
print(p1.name)  # Access name using property (getter)
print(p1.age)   # Access age using property (getter)
p1.name = "shyam"  # Update name using property (setter)
p1.age = 21        # Update age using property (setter)
print(p1.name)     # Print updated name
print(p1.age)      # Print updated age

#use of strip
n="xxxRam!xx"
print(n)
print(n.strip('x'))