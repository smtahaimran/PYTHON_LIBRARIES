# PYTHON_LIBRARIES

## Project Overview

**Title**: PYTHON_LIBRARIES
**Libraries**: `NUMPY,PANDAS,MATPLOTLIB,SEABORN`

This repository contains hands-on practice with essential Python libraries used in data analysis and visualization. The focus is on building a strong foundation by working with the following libraries:

 ## Libraries Covered
### NumPy

- Understanding data storage
- Working with different dimensions (0D, 1D, 2D...)
- Using .ndim to check the number of dimensions
- Assigning dimensions using ndmin
- Performing basic arithmetic operations
- Slicing and reshaping arrays


```python

import numpy as np
# NUMPY LIBRARY
lst=np.array([4,9,6,7])
print(lst)
#.....................................
lst1=np.array(4)  #0D
lst2=np.array([4,9,6,7])  #1D
lst3=np.array([[7,9,7,5],[3,2,6,7]])  #2D
print(lst1.ndim)
print(lst2.ndim)
print(lst3.ndim)
#......................................
lst4=np.array([4,8,7,9])
print(lst4[1]+lst4[2])   # FOR ADDITION
#......................................
lst5=np.array([4,5,6,7])
print(lst5[2:4])   #FOR SLICINHG
#......................................

```




### Pandas

- Creating and displaying Series and DataFrames
- Setting custom indexes
- Importing/exporting CSV files
- Exploring data using .head() and .tail()

```python

import pandas as pd
#........................................
a=["Ali","Ahmed","Saad","Haris","Zain"]
pt=pd.Series(a)
print(pt)
#.........................................
name=["Ali","Ahmed","Saad","Haris","Zain"]
pt=pd.Series(name,index=["a","b","c","d","e"])
print(pt)
#.......................................
# Data Frame
data={
    "Name":["Ali","Ahmed","Zain","Haris","Saad"],
    "age":[20,22,23,19,27],
    "city":["Lahore","Islamabad","Karachi","Lahore","Sialkot"],
}

print(pd.DataFrame(data))

#.......................................
# From CSV
df=pd.read_csv("C:/Users/A.N.T/Desktop/PYTHON P1/Sheet.csv")
print(df.to_string())
# Top 5
print(df.head(5))
# Below 5
print(df.tail(5))
#.........................................
```


### Matplotlib

- Creating basic plots and line graphs
- Customizing lines, points, and markers for clarity
  ![MATPLOTLIB](Figure_1.png)


### Seaborn

Enhancing data visualizations with aesthetically pleasing and informative graphs

### Objective
The goal of this project is to develop a solid understanding of data handling and visualization techniques using Python. This foundational knowledge is key for further exploration into data science and analytics.



## Project Structure

### 1. Database Setup
![ERD](https://github.com/najirh/Library-System-Management---P2/blob/main/library_erd.png)






### 3. CTAS (Create Table As Select)

- **Task 6: Create Summary Tables**: Used CTAS to generate new tables based on query results - each book and total book_issued_cnt**

```sql
CREATE TABLE book_issued_cnt AS
SELECT b.isbn, b.book_title, COUNT(ist.issued_id) AS issue_count
FROM issued_status as ist
JOIN books as b
ON ist.issued_book_isbn = b.isbn
GROUP BY b.isbn, b.book_title;
```


- **LinkedIn**: [Connect with me professionally](https://www.linkedin.com/in/najirr)

Thank you for your interest in this project!
