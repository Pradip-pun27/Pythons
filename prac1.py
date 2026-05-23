class Books:
    def __init__(self,na,pr):
        self.name = na
        self.price = pr

    def __str__(self2):
        return f" {self2.name} ({self2.price})"

    def Printinfo(self1):
        print("The name and price of a book is on this way")
        return self1.name,self1.price


B1 = Books("Physics",10000)
print(B1)
a = B1.Printinfo()
print(a)
print(B1)

class Num:
    
    def __iter__(self):
        self.number = 4
        return self
    def __next__(self):
        var = self.number
        self.number += 1
        return var
n = Num()
it = iter(n)
b = it.__next__()
print(b)



         