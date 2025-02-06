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


# Creating NumPy arrays
sample_array = np.array([1, 2, 3])
print(f'***{sample_array.dtype}, {sample_array}')

ones = np.ones((2, 3))
print(ones, ones.dtype, type(ones))

zeros = np.zeros((2, 3))
print(zeros)

range_array = np.arange(0, 10, 2)
print(range_array)

random_array_1 = np.random.randint(0, 10, size=(3, 5))
print(random_array_1, random_array_1.size, random_array_1.shape)

random_array_2 = np.random.random((5, 3))
print(f'*** {random_array_2}, {random_array_2.shape}')

random_array_3 = np.random.rand(5, 3)
print(f'Rand#### {random_array_3}')

# Pseudo-Random Numbers
pseudo_random = np.random.seed(0)  # No matter what the number of seed is
random_number_4 = np.random.randint(10, size=(5, 3))
print(random_number_4, random_number_4.shape)
