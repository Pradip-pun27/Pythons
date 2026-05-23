# *args = Takes more than 1 arguments as parameter in the form of tuples.
def fun(*args):
    print(args[2])

fun("a",1,True)
# **kwargs = Takes more than  1 keyword arguments as parameter in the form of dictionary. 
def func(**kwargs):
    print(kwargs["e"])

func(d="Ram",e= 7)
# Arbitrairy arguments and Arbitrairy keyword argument in a combine.
def fx(*arg,**kwarg):
    print(str(arg[0])+ "," +str(kwarg["a"]))

fx("Rabi",1,a= "Man", b = 3.14)


    
# One function taking argument as another function.
def _cal_(funct,arg1,arg2): #funct and mul are sane but of different name.
    return funct(arg1,arg2)


def mul(x,y):
    return x *y

res = _cal_(mul,9,10)
print(res)
 


