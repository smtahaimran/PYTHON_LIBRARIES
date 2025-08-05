import pandas as pd

#........................................

 a=["Ali","Ahmed","Saad","Haris","Zain"]
 pt=pd.Series(a)
 print(pt)

#........................................
#.........................................

 name=["Ali","Ahmed","Saad","Haris","Zain"]
 pt=pd.Series(name,index=["a","b","c","d","e"])
 print(pt)

#.......................................
# Data Frame
#.......................................

 data={
     "Name":["Ali","Ahmed","Zain","Haris","Saad"],
     "age":[20,22,23,19,27],
     "city":["Lahore","Islamabad","Karachi","Lahore","Sialkot"],
 }

 print(pd.DataFrame(data))

#.......................................
# From CSV
#.......................................

df=pd.read_csv("C:/Users/A.N.T/Desktop/PYTHON P1/Sheet.csv")
print(df.to_string())

# Top 5
print(df.head(5))

# Below 5
print(df.tail(5))

#.........................................
