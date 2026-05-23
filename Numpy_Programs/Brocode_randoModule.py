import numpy as np
rng = np.random.default_rng()
print(rng.integers(1,92, size =(2,4)))

arr = np.array([1,2,3,4])
rng.shuffle(arr)
print(arr)

num = rng.choice(arr,size =2)
print(num)