import pandas as pd
import numpy as np

# Dict = {'Student':['San','Raj','Ram'], 'Marks':[20,30,40],'Games':['Cricket','Hockey','Football']}
# dFlistDict=pd.DataFrame(Dict)
# print(dFlistDict)

# Dict = {'Student':['San','Raj','Ram'], 'Marks':[20,30,40],'Games':['Cricket','Hockey','Football']}
# dFlistDict=pd.DataFrame(Dict,index=['I','II','III'])
# print(dFlistDict)

#21
# Dict21 = {'Section':['A','B','C'], 'Contri':[2330,5530,5540]}
# dFlistDict21=pd.DataFrame(Dict21)
# print(dFlistDict21)


# people= {'sale':{'name':'Rohit','age':'30','Sex':'Male'}
#         ,'Mkt':{'name':'Rohana','age':'33','Sex':'Female'}
# }
# dFlistDict21=pd.DataFrame(people)
# print(dFlistDict21)

# Sales= {'Yr1':{'Qtr1':4324,'Qtr2':32434,'Qtr3':32434}
#         ,'Yr2':{'Qtr1':32434,'Qtr2':23434,'Qtr3':3244}
# }
# dFlistDict22=pd.DataFrame(Sales)
# print(dFlistDict22)

# collection1={'Yr1':1500,'Yr2':2500}
# collection2={'Yr1':2500,'Yr2':3500,'Nil':0}
# collection={1:collection1,2:collection2}
# dFlistDict22=pd.DataFrame(collection)
# print(dFlistDict22)

#
# Yr1={'Qtr1':4324,'Qtr2':32434,'Qtr3':32434}
# Yr2={'A':32434,'B':23434,'Qtr4':3244}
# DisSale={1:Yr1,2:Yr2}
# dFlistDict22=pd.DataFrame(DisSale)
# print(dFlistDict22)


# Toppera={'RollNo':4324,'Name':'Sandeep','Marks':98}
# Topperb={'RollNo':4325,'Name':'Sanjay','Marks':99}
# Topperc={'RollNo':4326,'Name':'Rajendra','Marks':77}
#
# DisSale=[Toppera,Topperb,Topperc]
# dFlistDict22=pd.DataFrame(DisSale)
# print(dFlistDict22)
# Sales= {'Yr1':{'Qtr1':4324,'Qtr2':32434,'Qtr3':32434}
#         ,'Yr2':{'Qtr1':32434,'Qtr2':23434,'Qtr3':3244}
# }
# dFlistDict22=pd.DataFrame(Sales)
# print(dFlistDict22)

# From 2D  array

# narr=np.array([[1,23,4],[3,4,6]],np.int32)
# dFlistDict22=pd.DataFrame(narr)
# print(narr)
# narr=np.array([[1,23,4],[3,4,6]],np.int32)
# dFlistDict22=pd.DataFrame(narr,columns=['One','Two','THree'],index=['A','B'])
# print(dFlistDict22)

# listDict = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]
# dFlistDict=pd.DataFrame(listDict)
# print(dFlistDict)
# #

# Creating a dictonary from 2D dic and series
# val=[4,6,8,55,88]
# Ser1=pd.Series(val)
# print(Ser1)
#
# san=['o','h','o','y','b']
# Ser2=pd.Series(san)
# print(Ser2)
#
# Dic1={1:val,2:san}
# dFlistDict=pd.DataFrame(Dic1)
# print(dFlistDict)

# 29

# Staff=[20,36,44]
# Salary=[2783334,36324324,3242444]
# Dict={'Staff':Staff,'Sal':Salary}
# Ser1=pd.DataFrame(Dict)
# print(Ser1)

# Dict = {'Student':['San','Raj','Ram'], 'Marks':[20,30,40],'Games':['Cricket','Hockey','Football']}
# dFlistDict=pd.DataFrame(Dict,index=['I','II','III'])
# print(dFlistDict.index)
# print(dFlistDict.columns)
# print(dFlistDict.axes)
# print(dFlistDict.dtypes)
# print(dFlistDict.size)
# print(dFlistDict.shape)
# print(dFlistDict.values)
# print(dFlistDict.empty)
# print(dFlistDict.ndim)
# print(dFlistDict.transpose())
# print(dFlistDict.count(axis='index'))

# a=np.array([['24','36'],['Sandeep','Meenal'],['M','F']])
# Ser1=pd.DataFrame(a)
# print(Ser1)

# Population, Hospital, School
# aa=[['34324324','KEM','MKNS'],['34324','Nuri','DPS'],['34324324','Ruby','Modal'],['34324','ABC','DonBosco']]
# df=pd.DataFrame(aa,columns=['Population','Hospital','School'],index=['Pune','Indore','Bhopal','Mumbai'])
# # print(df.loc[['Indore','Bhopal'],['Population','Hospital']])
# df.Population[1]=5555
# print(df)
# print(df.Population[1])
# print(df.loc[1:2, ['Population','Hospital']])
# print(df.Population['Pune'])
# print(df[['Population']])
# print(df[['Population','Hospital']])
# print(df.loc["Indore":"Mumbai",:])
# print(df.loc["Pune":"Bhopal",:])
#  print(df.loc[:,"Population":"Hospital"])
#  print(df.loc["Pune":"Bhopal","Population":"Hospital"])
# print(df.at["Pune","Population"])
# print(df.iat[0,0])
 # print(df.loc[0:2,['Population','Hospital']])
# print(df.loc[1:2, ['Population','Hospital']])


# data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata',
#                                'Mahindra', 'Maruti', 'Hyundai',
#                                'Renault', 'Tata', 'Maruti'],
#                      'Year': [2012, 2014, 2011, 2015, 2012,
#                               2016, 2014, 2018, 2019],
#                      'Kms Driven': [50000, 30000, 60000,
#                                     25000, 10000, 46000,
#                                     31000, 15000, 12000],
#                      'City': ['Gurgaon', 'Delhi', 'Mumbai',
#                               'Delhi', 'Mumbai', 'Delhi',
#                               'Mumbai', 'Chennai',  'Ghaziabad'],
#                      'Mileage':  [28, 27, 25, 26, 28,
#                                   29, 24, 21, 24]})
# print(data)
# # print(data.loc[[1,4], ['Brand','Year','Mileage']])
# print(data.loc[[4,6], ['Kms Driven','City']])



# print(data.loc[[1,4], ['Year','Mileage']])
# print(data[2: 5])
# print(data.loc[[0,1,5], ['Year','Mileage']])
# print(data.loc[[0,1,5], ['Year','Mileage']])
# print(data.iloc[2: 5])
# print(data.Brand)
# print(data.iloc[2: 5, ['City','Mileage']])
# print(data.loc[2: 5, 'City','Mileage'])
# print(dFrameEmt.loc[:10,'Price':'EuroPrice'])
# print(data.Brand[2])
#
aa=[[33,133],[44,-33]]
df=pd.DataFrame(aa,columns=['C1','C2'],index=['R1','R2'])
df['New']=99
df['New1']=[199,33]
df.at['R3',:]=160
print(df)
# df.at['R4',:]=[199,33]
print(df)
del df['C1']
print(df)
df=df.drop(['R1'])
print(df)
# print(df>0)


# print(df['C2']>10)