from numpy import random
r = random.randint(100,size=(7,2))
print(r)

x=random.choice([3,4,8,9,7],size=(6,4))
print(x)

y=random.rand(3,2)
print(y) #Print the  matrix of size 3 x 2 containing random float number from 0-1 

ran = random.choice([1,2,3,4,5,6],p=[0.1,0.3,0.2,0.3,0.1,0.0,],size=(400))
print(ran)