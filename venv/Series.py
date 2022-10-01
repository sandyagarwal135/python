import pandas as pd
import numpy as np
# s1=pd.Series()
# print(s1.empty)
# s1=pd.Series(Empty)
#
# b=[4,6,8,55]
# # s1=pd.Series(b)
# # print(s1)

# s1=pd.Series([4,6,8,55])
# print(s1)

#
# s1=pd.Series(['o','h','o'])
# print(s1)

# s1=pd.Series("So funny")
# print(s1)

# s1=pd.Series(["I","am","Sorry"])
# print(s1)
#
# nda=np.arange(2,22,1)
# print(nda)
# s1=pd.Series(nda)
# print(s1)

# s1=pd.Series(np.arange(2,22,2))
# print(s1)

# s1=pd.Series(np.linspace(3,12,4))
# print(s1)

# stu={'A':139,'B':239,'C':339,'D':439}
# s1=pd.Series(stu)
# print(s1)
#
# MedalsWon=pd.Series(10,index=range(0,1))
# s1=pd.Series(MedalsWon)
# print(s1)
#
# MedalsWon=pd.Series(range(1,6,1))
# s1=pd.Series(MedalsWon)
# print(s1)

# MedalsWon=pd.Series(15,['a','b'])
# s1=pd.Series(MedalsWon)
# print(s1)
#
# s1=pd.Series((48,np.NAN,88,55))
# print(s1)


# xx=[x for x in 'abcded']
# print(xx)
# s1=pd.Series(xx)
# print(s1)
# from pandas.tests.extension.conftest import data
#
# va=[4,6,8,55,88]
# san=['o','h','o','y','b']
# s1=pd.Series(va,san)
# print(s1)
# s1=pd.Series(data=va,index=san)
# print(s1)

#
# a=np.arange(9,13,2)
# s1=pd.Series(index=a,data=a*2,dtype=np.int64)
# print(s1)
#
# #a=np.arange(9,13,2)
# s1=pd.Series(index=a,data=a**2,dtype=np.int64)
# print(s1)

# val=['a','b']
# ind=np.array([6700,np.NaN])
# s1=pd.Series(index=ind,data=val)
# print(s1)

# val=['a','b']
# ind=np.array([6700,np.NaN])
# s1=pd.Series(index=ind,data=val)
# print(s1)


# val=[44.4,56.4]
# s1=pd.Series(data=val)
# print(s1)

# va=[4,6,8,55,88,77]
# san=['o','h','o','y','b',np.NaN]
#
# s1=pd.Series(data= san,index=va,name='myseries')
# print(s1)
# print(s1.values.itemsize)
# print(s1.name)
# print(s1.empty)
# print(s1.hasnans)
# print(s1.index)
# s1.index.name='indexo'
# print(s1.index.name)
# print(s1.values)
# print(s1.dtype)
# print(s1.shape)
# print(s1.nbytes)
# print(s1.ndim)




# san=['o','h','ot','y','b',np.NaN]
# s1=pd.Series(data= san,name='myseries')
# print(s1)
# print(s1[2])

# va=[4,6,8,55,88,77]
# san=['o','h','ot','y','b',np.NaN]
# s1=pd.Series(data= san,index=va, name='myseries')
# print(s1)
# print(s1[55])

#
# san=['o','h','ot','y','b',np.NaN]
# s1=pd.Series(data= san, name='myseries')
# print(s1)
# print(s1[:5:2])

# san=['o','h','ot','y','b',np.NaN]
# s1=pd.Series(data= san, name='myseries')
# s1[2]='rr'
# print(s1)


# san=['o','h','ot','y','b',np.NaN]
# s1=pd.Series(data= san, name='myseries')
# print(s1)
# print(s1[:5:2])
#
# s1[:5:2]='ff'
# print(s1)

# va=[4,6,8,55,88,77]
# san=['o','h','ot','y','b',np.NaN]
#
# s1=pd.Series(data= va,index=san, name='myseries')
# print(s1)
# s1.index=['oy','hh','oo','yy','bb','tt']
# print(s1)

# # --Demo
# va=[4,6,8,55,88,77,4,4]
# v1=[4,6,8,55,88,77,4,4]*2
# # print(v1)
# s1=pd.Series(data=va, name='myseries')
# a=(s1.values)
# print(s1+2)
# print(s1)

va=[4,6,8,55,88,77,4,4,4,4,4,4,4,3]
va1=[5,44,4,4,3,66,66,6]
s1=pd.Series(data=va, name='myseries')
s2=pd.Series(data=va1, name='myseries1')
print(s1+s2)

# va=[4,6,8]
# va1=[5,44,4]
# va1idx=['a','b','c']
#
# s1=pd.Series(data=va, name='myseries')
# s2=pd.Series(data=va1,index=va1idx, name='myseries1')
# print(s1+s2)
# print(s2)
#
# Population=[3333334,3432432436,83432434324]
# vaidx=['Pune','Mimbai','Bpl']
# AvgIncome=[3432435,432324344,342344]
# s1=pd.Series(data=Population,index=vaidx, name='Population')
# s2=pd.Series(data=AvgIncome,index=vaidx, name='AvgIncome')
# print(s2/s1)


# vaidx=['Pune','Mimbai','Bpl']
# AvgIncome=[3432435,432324344,342344]
# s2=pd.Series(data=AvgIncome,index=vaidx, name='AvgIncome')
# print(s2[s2>444444])


vaidx=['Pune','Mimbai','Bpl']
AvgIncome=[3432435,432324344,342344]
s2=pd.Series(data=AvgIncome,index=vaidx, name='AvgIncome')
print(s2.sort_values(ascending=False))