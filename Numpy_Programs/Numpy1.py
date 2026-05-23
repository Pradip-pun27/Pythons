import numpy as np
# print(np.array.__doc__)
# print(np.__version__)
# print(np.mat.__doc__)
arr = np.array([1,2,3,4])
print(type(arr))
ar0= np.array(11)# 0-D array
ar1= np.array([1,4,2,4])  # 1-D array
ar2=np.array([[1,2,3],[4,5,6]]) # 2-D array
ar3=np.array([ [[1,2],[4,3]] , [[3,4],[4,5]] ]) # 3-D array
print(f"The Dimension of ar0 is {ar0.ndim}")
print(ar1.ndim)
print(ar2.ndim)
print(ar3.ndim)
# Creating an array of one's wished dimension
array = np.array([1,2,3,4],ndmin=4)
print(f"{array} is of {array.ndim}th Dimension")

#Print from 1 to 6(Exclusive) with 2 step( 2 skips)
n_par=np.arange(1,6,2)
print(n_par)

# To create 1-D and 2-D array with zeros as elements and also same for np.ones(size)
n_par0=np.zeros(4)
n_par1=np.zeros((2,3))
# print(n_par1)

# Creating empty 2*3 array and will hold garbage values at first we can initialize the values later to that places
emp = np.empty((2,3))
# emp[1,2]=1023
# print(emp)

#Creating an array of one's wish and filling values also there
wish_array= np.full((2,2),7)
# print(wish_array)
import numpy as np

# 3x3 identity matrix
arr1 = np.eye(3)
# print("eye(3):\n", arr1)

# 4x4 identity matrix
arr = np.identity(4)
# print("identity(4):\n", arr)

# 4 evenly spaced numbers between 0 and 10 (inclusive by default)
arr14 = np.linspace(0, 10,4)
print("linspace(0, 10):", arr14)



