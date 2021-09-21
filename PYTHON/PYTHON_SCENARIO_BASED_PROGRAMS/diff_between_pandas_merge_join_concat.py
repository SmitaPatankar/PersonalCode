import pandas as pd

data1 = {'key1':['k0','k1'], 'name' :['mark','juli'],'city':['New York','Paris']}
data2 = {'key1':['k1','k2'],'name' :['john','alex'],'city':['London','Tokyo']}

df1 = pd.DataFrame(data1,index = [0,1],columns=['key1','city','name'])
df2 = pd.DataFrame(data2,index=[1,2],columns=['key1','city','name'])

print("---------DF1--------------")
print(df1)

print("---------DF2--------------")
print(df2)

print("--------------MERGE outer--------------")
print("as per common column value")
print(df1.merge(df2,on="key1", how="outer"))

print("--------------JOIN outer--------------")
print("as per index")
print(df1.join(df2, how="outer", lsuffix="_"))

print("--------------CONCAT axis 0--------------")
print("vertical + on 2 or more items")
print(pd.concat([df1,df2],axis=0))

print("--------------CONCAT axis 1--------------")
print("horizontal on index + on 2 or more items")
print(pd.concat([df1,df2],axis=1))
