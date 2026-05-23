a = "Ram"
myit = iter(a)
print(next(myit))
print(next(myit))
print(next(myit))

class num:
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        if self.n<=10:
             z = self.n
             self.n +=1
             return z
        else:
            raise StopIteration

       
myn = num()
itr= iter(myn)
for i in itr:
    print(i)
print(myn)



class car:
    def move(self):
        print("Run")
class plane:
    def move(elf):
        print("Fly")
car1 = car()
plane1 = plane()
for i in (car1,plane1):
    i.move()
