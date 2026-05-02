import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.min(arr, axis=0))
print(np.max(arr, axis=1))