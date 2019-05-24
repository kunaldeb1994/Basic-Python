import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\Sagar computers\Documents\SQL.csv')
print(df.head())
# df1=pd.describe_option()
# print(df1)
Z=df.SALARY.describe() #.describe function is used to get all the statiscal data
print(Z)

#fillna function to add valuesin the new column
A=df.NET_SALARY.fillna(value=(df['SALARY']+df['HIKE']))
print(A)
S=pd.DataFrame(df)
print(S.describe())
print('-------------------------------------------------------------------------------')

#to understand series: can be related to tuple. is not used much.
S1=pd.Series(np.arange(1,8))
print(S1)

#to delete row wise use drop.index with [[]]
S11=S1.drop(S1.index[[4,5,1]]) #double[[]] is used to delete many no. of rows
print(S11)

S2=pd.Series([2,3,4,'D'],index=['p1','p2','p3','p4'])
print(S2)
print(S2['p1':'p4'])
print(S2[0:3])

#Dataframe=column based indexing + row based slicing
#data as list
df1=pd.DataFrame(['a','b','c'],columns=['name'])
print(df1)
#to delete a colum in pandas use drop function with axis=1
df11=df1.drop('name',axis=1)#where 1 is the axis number (0 for rows and 1 for columns.)
print(df11)

#data list with index
df2=pd.DataFrame(['a','b','c'],index=['p1','p2','p3']) #if column name is not given by default it takes as 0
print(df2)
df3=pd.DataFrame([['A',10],['B',23],['C',24]],index=['p1','p2','p3'],columns=['NAME','AGE'])
print(df3)
#when a age data is missing in produces NaN
df4=pd.DataFrame([['A',10],['B',23],['C']],index=['p1','p2','p3'],columns=['NAME','AGE'])
print(df4)
df41=df4.AGE.fillna(23) #to fill the nan value use fillna
print(df41)

#data with dictionary
dict1={'name':['A','B','C','D'],'age':[10,23,24,35]}
df5=pd.DataFrame(dict1)#here the data is list,so age doesnt come before name
print(df5)

#loc function is used for row based indexingse3
df52=df5.loc[df5['age']==10]
print(df52,'loc function-------------')
#to append a new row use append function
df51=df5.append({'name':'E','age':25},ignore_index=True)
print(df51)

dict2=[{'name':'A','age':12},{'name':'B','age':34},{'name':'c','age':24}]
df6=pd.DataFrame(dict2)#here the data is a dictionary,age comes before name
print(df6)
print(df6.dtypes)

#to know only the values of specific columns
df7=pd.DataFrame([[0,1,2,3,4,5],[11,12,13,14,15,16]],columns=['p1','p2','p3','p4','p5','p6'])
print(df7)
df71=pd.DataFrame()# empty dataframe is used to add
df71['p1']=df7['p1'] #in empty data frame the columns of df7 are used
df71['p2']=df7['p2']
df71['p6']=df7['p6']
print(df71)
df72=df71.loc[df7['p6']==5]
print(df72,'young khalifa')

'''agg stands for anti grain geometry'''
