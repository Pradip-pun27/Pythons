from numpy import random
import numpy as np
arr=np.array([1,2,3,4,5])
# random.shuffle(arr) #It will modify the original array(arr)
# print(arr)
print(random.permutation(arr)) # It won't modify original array but return new array
print(arr)