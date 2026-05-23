import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
ar1=np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
# for i in arr:
#     for j in i:
#         print(j)
for j in np.nditer(arr):
    print(j)

for index,num in np.ndenumerate(ar1):
    print(f"{index} : {num}")

for ans in np.nditer(arr[:,::2]):
    print(ans)

