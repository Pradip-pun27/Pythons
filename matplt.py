import matplotlib.pyplot as plt
import matplotlib
import numpy as np

x= np.array([1,2])
y= np.array([10,20])

plt.plot(x,y,"o--g")
plt.title("Simple Graph from matplotlib")
plt.xlabel("x- Value")
plt.ylabel("Y- Value")
plt.show()

print(matplotlib.__version__)

# Generator object
# gen=(i for i in range(19))
# print(type(gen))