class Function:
    name = "Math's function" # class' attribute

    def __init__(self,num):
        self.n=num # instance's attribute
    
    # Instance method
    def Mul(self, n):
        for i in range(n+1):
            print(f"{i} * {n} = {i*n}")
    
    # Class method
    @classmethod
    def class_method(cls,new_name):
        cls.name=new_name
        return cls.name
    
    # Static method
    @staticmethod
    def addn(a,b):
        return a+b

f = Function(3)
f.Mul(10)
print(Function.name)
f.class_method('Fx')#changing the value of 'name' class' attribute of a Function named class. 
print(Function.name)
print(f.addn(9,2))