import numpy as np
arr = np.array([1,2,3])
print(arr.dtype)   # int64 (or int32 depending on system)

#changing of dtype
arr = np.array([1,2,3], dtype=float) #this will change data type
print(arr.dtype)   # float64