import numpy as np
import pandas as pd

# DatatTypes amd Attributes
# NumPy 's main datatype is ndarray

a1 = np.array([1, 5, 9, 7, 4, 5])
print(a1)
type(a1)
print(a1.shape)
print(a1.dtype)

a2 = np.array([[2, 6.3, 9.8], [2, 7, 4.1]])
print(a2.shape)
print(a2.dtype)

a3 = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]
])
print(a3.shape)
print(a3.dtype)
print(a1.ndim, a2.ndim, a3.ndim)
print(a1.size, a2.size, a3.size)

# Create a DataFrame from a NumPy array
df = pd.DataFrame(a2)
print(df)


