import numpy as np
import pandas as pd
import timeit
import matplotlib
import matplotlib.pyplot as plt

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

ones = np.ones((2, 6))
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

# Viewing Arrays and Matrices
unique_number = np.unique(random_number_4)
print(unique_number)

a4 = np.random.randint(10, size=(2, 3, 4, 5))
print(a4)

# Get the first 4 number of the innermost arrays
print(f'$$$$$$$$$$$$$$$$ \n {a4[:, :, :2, :1]}')
print(a4[:, :, :2, :1].shape)


# Manipulating & Comparing Arrays
# Arithmetic

plus1 = a1 + ones
print(plus1)

plus2 = np.add(a1, ones)
print(plus2)

minus = a1 - ones
print(minus)

multiply1 = a1 * ones
print(multiply1)

multiply2 = a1.reshape(2, 3) * a2
print(multiply2)

divided1 = a1 / ones
print(divided1)

divided2 = a2 / a1.reshape(2, 3)
print(divided2)

# Numpy Modulo
divided3 = a1 % 2
print(divided3)

# Floor devision removes the decimals (rounds down)
floor_devision = a2 // a1.reshape(2, 3)
print(divided1)

square1 = a2 ** 2
print(square1)

square2 = np.square(a2)
print(square2)

expo = np.exp(a1)
print(expo)

log = np.log(a1)
print(log)

# Aggregation
listy_list = [1, 2, 3]
print(type(listy_list))

print(sum(listy_list))

print(sum(a1))
print(np.sum(a1))

# Use Python's methods sum() on Python datatypes
# Use Numpy's methods np.sum() on NumPy's arrays

massive_array = np.random.random(100000)
print(massive_array.size)

print(massive_array[:10])

python_time = timeit.timeit(
    lambda: sum(massive_array),
    number=100
)

numpy_time = timeit.timeit(
    lambda: np.sum(massive_array),
    number=100
)

print(f"Python sum: {python_time:.6f} seconds")
print(f"NumPy sum: {numpy_time:.6f} seconds")

print(np.mean(a2))
print(np.max(a2))

print(np.min(a2))
print(np.std(a2))

# Higher Variance = wider range of numbers
# Lower Variance = Lower range of numbers
print(np.var(a2))

# Standard deviation = square root of variance
print(np.sqrt(np.var(a2)))

# Demo of std and var
high_var_array = np.array([1, 100, 200, 300, 4000, 5000])
low_var_array = np.array([2, 4, 6, 8, 10])
print(np.var(high_var_array), np.var(low_var_array))
print(np.std(high_var_array), np.std(low_var_array))

print(np.mean(high_var_array), np.mean(low_var_array))

plt.hist(high_var_array)
plt.show()

plt.hist(low_var_array)
plt.show()


# Reshaping & Transposing
print(a2.shape)
print(a3.shape)
a2_reshape = a2.reshape(2, 3, 1)

print(a2_reshape * a3)

# Transpose = Switches the axis'
print(a2.T)
print(a2.T.shape)
print(a3.T)
print(a3.T.shape)

# Dot product
np.random.seed(0)
mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))
print(mat1.shape, mat2.shape)

# Element-wise multiplication
print(mat1 * mat2)

# Dot product
mat3 = np.dot(mat1, mat2.T)
print(mat3)
print(mat3.shape)


# Comparison Operators
bool_array1 = a1.reshape(2, 3) > a2
bool_array2 = a1.reshape(2, 3) >= a2
print(bool_array1.dtype, type(bool_array1))
bool_array3 = a1 > 5
print(bool_array3)
print(a1 == a1)
print(a1.reshape(2, 3) == a2)


# Sorting Arrays
random_array = np.random.randint(10, size=(3, 5))
print(np.sort(random_array))
print(np.argsort(random_array))
print(np.argmin(a1))
print(np.argmax(a1))
print(np.argmax(random_array, axis=0))
print(np.argmax(random_array, axis=1))
