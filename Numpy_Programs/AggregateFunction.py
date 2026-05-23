import numpy as np

arr = np.array([[1,2,3],
                [3,4,1],
                [5,6,9]])
# print(arr.sum())
print(np.sum(arr))
print(np.mean(arr)) # np.std(), np.var(),np.min(),np.max()
print(np.argmax(arr)) # Returns the index where the max number lies
