import pandas as pd #import Pandas with alias pd -identifier
import numpy as np

a1=np.ar

# sales=[0,5,100,5,518]
# series1=pd.Series(sales)
# print(series1)
# series1=pd.Series(sales,name='yearsale')
# print(series1)
# items=['a', 'b', 'c', 'd', 'e']
# series1=pd.Series(sales,index=items, name='yearsale')
# print(series1)
# series1=pd.Series(sales,index=items)
# print(series1)
# series1=pd.Series([0,5,100,5,518])
# print(series1)
# Filter
# mask=(series1 ==5) | (series1==100)
print(series1.loc[(series1 ==5) | (series1==100)]) # | trated as or
print(series1.loc[(series1 ==5) & (series1.index=='b')])  # & trated as or
# print(series1['b':'d'])
# print(series1.iloc[2])
# print(series1.iloc[1:3]) #n amd m-1
#
# # The .loc[] method is the preferred way to access values by their custom labels
# print(series1.loc['b'])
#
# sales=[0,5,100,5,518]
# items=['a', 'b', 'a', 'd', 'e']
# series2=pd.Series(sales,index=items,name="sale")
# print(series2['a'])
# series2.reset_index(drop=True)
# print(series2)
# seriesA = pd.Series([1,2,3,4,5], index =['a', 'b', 'c', 'd', 'e'])
# print(seriesA)
# seriesB = pd.Series([10,20,-10,-50,100],index = ['z', 'y', 'a', 'c', 'e'])
# print(seriesB)
#
# print(seriesA + seriesB)

# seriesAlph = pd.Series(np.arange(10,16,1))
# # index = ['a', 'b', 'c', 'd', 'e', 'f']
# seriesAlph.index = ['a', 'b', 'c', 'd', 'e', 'f']
# seriesAlph.name="range" #name attribute
# seriesAlph.index.name="rangeindex" #name attribute
# print(seriesAlph)

# oil=pd.read_csv("C:/retail/oil.csv")
#
# oil_array =np.array(oil["dcoilwtico"].iloc[1000:1100])
# print(oil_array)
# oil_series = pd.Series(oil_array, name="oil_prices")
# dates = pd.Series(oil["date"]).iloc[1000:1100]
# oil_series.index = dates
# print(oil_series)
#
# # Mean of first 10 prices
#
# print(oil_series.iloc[:10].mean())
# print(oil_series.iloc[-10:].mean())
# oil_series.loc["2017-01-01":"2017-01-07"].reset_index(drop=True)
# print(oil_series)

# seriesCapCntry = pd.Series(['NewDelhi', 'WashingtonDC', 'London', 'Paris'],
# index=['India', 'USA', 'UK', 'France'])
# print(seriesCapCntry)
# print(seriesCapCntry['India'])
# print(seriesCapCntry[1])
# # seriesCapCntry.index=[10,20,30,40]
# print(seriesCapCntry)
# print(seriesCapCntry['India' : 'France'])
# print(seriesCapCntry[1: 3])
# seriesNum = pd.Series([10,20,30])
# print(seriesNum[1])
#
#
# dict1 = {'India': 'NewDelhi', 'UK':'London', 'Japan': 'Tokyo'}
# print(dict1) #Display the dictionary
# print(dict1["UK"])
# print(dict1[1])
# series8 = pd.Series(dict1)
# print(series8) #Display the series
# series1 = pd.Series([10,20,30]) #create a Series
# print(series1) #Display the series
#
# series2 = pd.Series(["Kavi","Shyam","Ravi"], index=[3,5,1])
# print(series2) #Display the series
#
# series2 = pd.Series([2,3,4],index=["Feb","Mar","Apr"])
# print(series2) #Display the series
# # Creation of Series from NumPy Arrays
#
# array1 = np.array([1,2,3,4])
# series3 = pd.Series(array1)
# print(series3)
#
# # To convert list in to series
# import pandas as pd
# import numpy as np
# a=[0,22,32,4,5,6]
# rollno=pd.Series(a)
# # print(rollno,type(rollno))
# # print(rollno.values.mean())
# # print(rollno.mean())
# # print(rollno.index)
# # print(rollno.values)
# # rollno.index=[10,20,30,40,50,60]
# # print(rollno)
# # rollno.name='Roll number'
# # print(rollno.name)
# # print(rollno.dtype)
# #
# # # Type conversionty
# # # --Convert into float
# # rollno_in_float=rollno.astype("float")
# # print(rollno_in_float)
# rollno_in_float=rollno.astype("float").sum()
# print(rollno_in_float)
# #
# # # --Convert into bool zero will retuen "false" and not zero will return "true"
# # rollno_in_float=rollno.astype("bool")
# # print(rollno_in_float)
# #
# # # --Convert into string
# # rollno_in_float=rollno.astype("string")
# # print(rollno_in_float)
# #
# # # --Convert into datetime64
# # rollno_in_float=rollno.astype("datetime64")
# # print(rollno_in_float)
# #
# # # --Convert into datetime64
# # rollno_in_float=rollno.astype("datetime64")
# # print(rollno_in_float)
#
# # --Convert into object
# rollno_in_object=rollno.astype("object")
# print(rollno_in_object)
#
# # x=pd.Series(['a','b','c']).astype("int") # Not possible
#
# oil=pd.read_csv("C:/retail/oil.csv")
# print(oil)
# # oil_array =np.array(oil["dcoilwtico"].iloc[1000:1100])
# # print(oil_array)
#
# # create a DataFrame from the oil file, drop missing values
# oil = pd.read_csv("C:/retail/oil.csv").dropna()
# print(oil)
# # # Grab 100 rows of oil prices
# oil_array = np.array(oil["dcoilwtico"].iloc[1000:1100])
# print(oil_array)
# dates = pd.Series(oil["date"]).iloc[1000:1100]
# oil_series = pd.Series(oil_array, name="oil_prices")
# oil_series.index = dates
# print(oil_series)
# # print(f"Name: {oil_series.name}")
# # print(f"dtype: {oil_series.dtype}")
# # print(f"size: {oil_series.size}")
# # print(f"index: {oil_series.index}")
#
# # Custom index
# sale=[33,55,67,888,88]
# index=["rose","banana","apple","pineapple","orange"]
# sale_series = pd.Series(sale, index,name="sales")
# print(sale_series)