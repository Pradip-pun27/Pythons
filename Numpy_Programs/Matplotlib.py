import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df = pd.read_csv("data.csv")
# df.plot()
# plt.show()

xpoints = np.array([1,7,4,9])
ypoints=np.array([100,300,200,900])
plt.plot(xpoints,ypoints,'o:r')
plt.show()
