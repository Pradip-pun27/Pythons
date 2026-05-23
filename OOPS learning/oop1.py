# OOP starting
class Vehicle:
    def __init__(self,name,price):
        self.n=name
        self.p=price
        print("I'm here")
    def info(self):
        print(f"This is {self.n} and Price is {self.p} ")
    def extra_info(self,model):
        print(f"Model is {model}")

v1=Vehicle('Honda',1000000)
v1.info()
v1.extra_info('F51')