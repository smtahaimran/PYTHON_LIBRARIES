import numpy as np

# NUMPY LIBRARY

lst=np.array([4,9,6,7])
print(lst)
#.......................

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

#........................................

