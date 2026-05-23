class Animal:
    def __init__(self,name):
        self.n=name
    def speak(self):
        print("Meow Meow")

class Dog(Animal):
    def speak(self):
        print("Bark Bark")
class Cat(Animal):
    pass
d1=Dog("Tommy")
print(d1.n)
c1=Cat("Jerry")
print(c1.n)
c1.speak()
d1.speak()
