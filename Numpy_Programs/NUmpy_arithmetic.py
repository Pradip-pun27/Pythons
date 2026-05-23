import numpy as np
arr = np.array([1,2,3,4])

print(arr**2)
# print(arr+2)
# print(arr-1)
# print(arr*2)
# print(arr/2)
print(np.sqrt(arr)) #others methods are also a/v like round,ceil,floor and can access like this : np.ceil()
print(np.pi)
radii =np.array([1,2,3])
print(np.pi *radii**2)

#Element wise operation
a1=np.array([1,2,3])
a2=np.array([2,3,4])
print(a1 * a2)
# print(a1 ==1)
a1[a1 <2]=0
print(a1)