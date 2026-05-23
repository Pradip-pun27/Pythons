# Using __str__() function.
class Person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def __str__(self):
        return f"{self.name} {self.age}"
p1=Person("Ranbir",10);
print(p1);

#Object method.
class Person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def Fun(abc):
        print("Hello I am "+abc.name)
p1=Person("Ranbir",10);
p1.Fun();

#Modifying the object's property.
class Person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def Fun(abc):
        print("Hello I am "+abc.name)
p1=Person("Ranbir",10);
p1.age=40;
print(p1.age);

#Deleting the object's property.
class Person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def Fun(abc):
        print("Hello I am "+abc.name)
p1=Person("Ranbir",10);
del p1.age;
print(p1.age);