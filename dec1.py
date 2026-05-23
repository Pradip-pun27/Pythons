def __deco__(fx):
    def mod():
        print("Ram")
        fx()
        print("Babal")
    return mod

def hello():
    print("K cha")

arb = __deco__(hello)
arb()
print(type(arb),arb)
print(dir())
