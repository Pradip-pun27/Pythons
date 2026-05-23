class Number:
    def __init__(self,start,end):
        self.s=start
        self.e=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.s <= self.e:
            values = self.s
            self.s += 1
            return values
        else:
            raise StopIteration

n1 = Number(1,109)
iterator=iter(n1)
print(next(iterator))
print(next(iterator))
for n in iterator:
    print(n,end=" ")



