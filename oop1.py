
class Myclass():
     a = 14;
m1=Myclass();
print(m1.a);

# Using __init__() Function in order to assign values for object's attributes and methods
class Person():
    def __init__(self,nam,age):
        self.nam=nam;
        self.age=age;
p1=Person("Ranbir",10);#Instance or objects of class named Person.
p2=Person("Anupam",12);#Instance or objects of class named Person.
print(p1.nam+ " is "+str(p1.age)+" years old.");
print(p2.nam,p2.age);





