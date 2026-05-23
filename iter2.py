class Myfun:
    def __init__(self,start,end):
        self.inital = start;
        self.final  = end;
    def __iter__(self):
        return self;

    def __next__(self):
        if self.inital >=self.final:
            raise StopIteration;
        else:
            current = self.inital;
            self.inital += 2;
            return current;
        
num = Myfun(2,10) 

for i in num:
    print(i);
 
