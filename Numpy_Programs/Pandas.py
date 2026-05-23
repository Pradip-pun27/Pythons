import pandas as pd
# nums= [1,2,4,9]
# s= pd.Series(nums,index=['a','b','c','d'])
# print(s)

# calories ={'day1':330, 'day2':340,'day3':310}
# S= pd.Series(calories)
# print(S)

data ={
    "calories":[100,300,420,510],
    "duration":[40,10,30,80]
}
df=pd.DataFrame(data)
print(df.loc[[0,1]])

# df= pd.read_csv("data.csv")
# print(df.to_string())