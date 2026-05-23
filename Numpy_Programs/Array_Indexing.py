import numpy as np
arr = np.array([[1,2,3],[3,4,5]])
print(arr[1,-1])
arr1=np.array([[[1,2,7],[3,4,9]],[[1,2,3],[3,4,5]]])
print(arr1[0,1,2]) # Accessing the 3-D Array element
ar1=np.array([1,3,5,7,9,11,13])

#Array slicing
newar1=ar1[1:4:2]#fetching the elements of 1-D array (from 1th index upto 3rd index with jump of 2 elements
print(newar1)
#Slicing 2-D Array
print(arr[0:2,2])#Fetching 0 and 1st index of 2-D array with 2th index only
print(arr[1,0:]) #Fetching all elements of 2nd position of 2-D array
print(arr[0:2,:])

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print(arr.dtype)
