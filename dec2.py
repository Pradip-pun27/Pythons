a = [1,2]
for i in a:
    print(i)
b= iter(a)
for j in b:
    print(j)

#Iterator in python
class Person():
    def __init__(self,a):
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <=10:
            res = self.a
            self.a +=1
            return res
        else:
            raise StopIteration


        
P1= Person(7)
P2 = Person(8)
it = iter(P1)
itt= iter(P2)
for i in it:
    print(i)


for j in itt:
    print(j)