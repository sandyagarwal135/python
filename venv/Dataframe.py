import pandas as pd
import pyodbc
import numpy as np
from pandas import read_csv





 # conm=pyodbc.connect()
 # aa=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-SAMMYOC\MSSQLSERVER1;DATABASE=test;Trusted_Connection=yes')
connSqlServer = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                               server='DESKTOP-SAMMYOC\MSSQLSERVER1',
                               database='test',
                               uid='sa',pwd='Welcome1@3')
cur=connSqlServer.cursor()

aa='Insert into Test(Name) VAlues(''342432'')'
cur.execute(aa)
cur.commit()
# for driver in pyodbc.drivers(aa):

    # print(driver)
# dFrameEmt = pd.DataFrame(read_csv('../../retail/oil1.csv'))
# dFrameEmt.columns=["Date","Price"]
#
# # print(dFrameEmt)
# avgprice= dFrameEmt.loc[:,"Price"].mean()
# print(avgprice)
#
# print(dFrameEmt.query("Price in [93.14,92.97] and Price > @avgprice "))


# dFrameEmt.columns=["Date","Price"]
# # print(dFrameEmt[["Price","Date"]].iloc[:20,0:2])
# dFrameEmt["EuroPrice"]=dFrameEmt[["Price"]]*10
# print(dFrameEmt)dFrameEmt
# dFrameEmt.drop("Price" , axis=1, inplace=True)
# print(dFrameEmt)
# dFrameEmt.append(dFrameEmt.iloc[-1])
# # print(dFrameEmt.loc[:10,'Price':'EuroPrice'])
# # with open("../FutureBookList/file.txt") as file:
# #    data = file.read()
#
# # array1 = np.array([10,20,30])
# # seri=pd.Series(array1)
# # print(seri)
# # dFramefromnp = pd.DataFrame(array1)
# # print(dFramefromnp)
# # array2 = np.array([100,200,300])
# # array3 = np.array([-10,-20,-30, -40])
# # dFramefromnp = pd.DataFrame([array1,array2,array3] )
# # print(dFramefromnp)
# # dFramefromnp = pd.DataFrame([array1,array2,array3],columns=[ 'A', 'B', 'C', 'D'] )
# # print(dFramefromnp)
# # dFramefromnp = pd.DataFrame([array1,array2,array3],index=[1,22,33],columns=[ 'A', 'B', 'C', 'D'] )
# # print(dFramefromnp)
# #
# listDict = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]
# dFlistDict=pd.DataFrame(listDict)
# print(dFlistDict)
# #
# dictForest = {'State': ['Assam', 'Delhi', 'Kerala']}
# se= pd.DataFrame(dictForest)
# print(se)
# dictForest = {'State': ['Assam', 'Delhi', 'Kerala'],
#               'GArea': [78438, 1483, 38852] ,
#               'VDF' : [2797, 6.72,1663]}
# dFrameForest= pd.DataFrame(dictForest)
# print(dFrameForest)
#
# seriesA = pd.Series([1,2,3,4,5],
#                     index = ['a', 'b', 'c', 'd', 'e'])
# seriesB = pd.Series ([1000,2000,-1000,-5000,1000],
#                      index = ['a', 'b', 'c', 'd', 'e'])
# seriesC = pd.Series([10,20,-10,-50,100],
#                     index = ['z', 'y', 'a', 'c', 'e'])
# col1=['AA','BB','CC','DD','EE','YY','ZZ']
# dFrame6 = pd.DataFrame([seriesA,seriesB,seriesC])
# print(dFrame6)
# # print(dFrame6.info())
# # print(dFrame6.describe())
# # print(dFrame6.describe(include='all'))
# # print(dFrame6.isna().sum())
# # print(dFrame6(['a'],columns=['a']))
#
# # dictForest = {'State': ['Assam', 'Delhi', 'Kerala'],
# #               'GArea': [78438, 1483, 38852] ,
# #               'VDF' : [2797, 6.72,1663]}
# # dFrameForest= pd.DataFrame(dictForest)
# # print(dFrameForest[['State','GArea']].iloc[0:1])
#
