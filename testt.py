#import pandas as pd
#df = pd.read_csv("C:/Users/Owner/Downloads/data.csv")
#print(df.to_string())  #use to_string() to print the entire DataFrame.
#print(pd.options.display.max_rows)   #maximum returned rows:
#pd.options.display.max_rows = 9999
#print(df.head(10)) #first 10
#print(df.head())  #first 5
#print(df.tail())   #last 5
#print(df.info())   # about the data

#DATA CLEANING
        ##Empty Cells

# the dropna() method returns a new DataFrame, 
# and will not change the original.

#new_df = df.dropna()  
#print(new_df.to_string())

#If you want to change the original DataFrame,
# use the inplace = True argument:
#df.dropna(inplace = True)
#print(df.to_string())

# Replace NULL values with the number 130:
#df.fillna(130, inplace = True)  

        ##Data in wrong format

#df['Date'] = pd.to_datetime(df['Date'])
#print(df.to_string())
#Remove rows with a NULL value in the "Date" column:
#df.dropna(subset=['Date'], inplace = True)
 
          ##Wrong data

#Set "Duration" = 45 in row 60
#df.loc[60, 'Duration'] = 45
#print(df.to_string())

#Loop through all values in the "Duration" column.
#for x in df.index:
 # if df.loc[x, "Duration"] > 120:
  #  df.loc[x, "Duration"] = 60  #if 120s ih bol replace 60

#Delete rows where "Duration" is higher than 120:
#for x in df.index:
  #if df.loc[x, "Duration"] > 120:
   # df.drop(x, inplace = True)
 
             ##Duplicates   

#Returns True for every row that is a duplicate, 
# othwerwise False:
#print(df.duplicated())

#Remove all duplicates:
#df.drop_duplicates(inplace = True)


#Relationship between the columns:
#print(df.corr())

#PLOT
#import pandas as pd
#import matplotlib.pyplot as plt
#df = pd.read_csv('C:/Users/Owner/Downloads/data.csv')
#df.plot()
#plt.show()

#df.plot(kind='bar', x='Duration', y='Calories')
#plt.show()

#df["Duration"].plot(kind = 'hist')
#plt.show

##DATA TYPES
#str --converts the specified value into a string. x = "Hello World"  ',", ''',"""
#int-- integer number.  x=5
#float--real numbers 
#complex-- x = 1j
#list--x = ["apple", "banana", "cherry"]   ordered, changeable
#tuple--x = ("apple", "banana", "cherry")   ordered and unchangeable. use , in 1 item
#range--x = range(6)  /returns a sequence of numbers/
#dict--x = {"name" : "John", "age" : 36}   key:value pairs. cannot 2 value in a key/ordered*, changeable and do not allow duplicates./
#set--x = {"apple", "banana", "cherry"}   unordered, so you cannot be sure in which order the items will appear.
#frozenset--x = frozenset({"apple", "banana", "cherry"}) 
#bool  --x = True
#	bytes--x = b"Hello"
#	bytearray--x = bytearray(5)
#	memoryview--x = memoryview(bytes(5))
#NoneType--x = None

        ##COUNTPLOT

