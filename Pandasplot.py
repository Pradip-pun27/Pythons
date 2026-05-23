import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('W3SchoolData.csv')
# df.plot()
# plt.show()
print(df.corr())
print(df.info())
print(df)