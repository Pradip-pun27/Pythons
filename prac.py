a,b,c="Ram",1,True
print(a,b,c,sep="\n")

list1=[1,2,3]
x,y,z=list1 #Unpacking the list
print(x,y,z)

loveLiveLaugh="Hello World" #Camelcase variable 
print(loveLiveLaugh)

ILoveYou="What's up" #Pascalcase variable 
print(ILoveYou)

Shake_my_head = " All first class" #Snakecase variable 
print(Shake_my_head)

#lambda function
ans=lambda p,q,r:max(p,q,r)
print(ans(2,4,3))

#OOp in Python
class Boy:
    name = "Ram" 
    age = 15
    def info(self):
        print(f"{self.name} is {self.age} years old.")
d= Boy()
e=Boy()
e.name="Laxman"
e.age=11
d.info()
e.info()

class Girl:
    def __init__(self,na,ag):
        print("Yo")
        self.name = na
        self.age = ag
    def info1(self):
            print(f"{self.name} is {self.age} years old.")
f= Girl("Sita",14)
g=Girl("Rita",18)
f.info1()
g.info1()

class Person():
    def __init__(self,nam,agg):
        self.name= nam
        self.age = agg
    def __str__(abc):
        return f"{abc.name} ({abc.age})"
h= Person("Krish",3)
print(h)

