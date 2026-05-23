import numpy as np
arr=np.array([1,2,3,4])
cp = arr.copy()
vw=arr.view()
print(f"vw doesn't own the data cuz this returned : {vw.base}")
print(f"cp own the data cuz this returned : {cp.base}")
# Any changes made to copy doesn't affect original array and vice-versa
cp[3]=3
print(cp)
print(arr)
# Any changes made to view affects original and vice-versa
vw[3]=9
print(vw)
print(arr)