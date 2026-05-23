import numpy as np
arr = np.array([[1,2,3],[8,5,9]])
print(arr.shape)
print(arr.reshape(6))


ar=np.array([1,2,3,4,9,4,6,9,3,9])
s= np.sort(ar) #Sorting(Ascending)
print(s)
print(np.where(ar==9)) # Searching

#Filtering
new_arr=np.array([1,4,5,3,8,9])
n=[]
for num in new_arr:
    if(num%2==1):
        n.append(True)
    else:
        n.append(False)
print(n)
print(new_arr[n])