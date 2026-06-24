import numpy as np

print("--- 1. Creating Basic Arrays & Attributes ---")
# Creating a 1D Array from a list
list_1d = [1, 2, 3, 4, 5]
arr_1d = np.array(list_1d)
print("1D Array:", arr_1d)
print("Rank (Dimensions):", arr_1d.ndim)  # ndim represents the rank
print("Shape:", arr_1d.shape)
print("Data Type:", arr_1d.dtype)
print("-" * 40)

# Creating a 2D Multi-Dimensional Array
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_2d = np.array(list_2d)
print("2D Array:\n", arr_2d)
print("Rank (Dimensions):", arr_2d.ndim)
print("Shape (Rows, Columns):", arr_2d.shape)
print("Data Type:", arr_2d.dtype)
print("-" * 40)


print("\n--- 2. Built-in Array Creation Functions ---")

# numpy.fromiter() - Creating an array from an iterable (like a string)
text_var = "Avishkarana"
arr_from_iter = np.fromiter(text_var, dtype='U1')
print("Array from iterable (string):\n", arr_from_iter)

# numpy.arange() - Evenly spaced values in an interval
arr_range = np.arange(1, 11, 2, dtype=np.int32)
print("Array using arange (1 to 10, step 2):\n", arr_range)

# numpy.linspace() - Evenly spaced numbers over a specified interval
arr_linspace = np.linspace(0, 10, 5)
print("Array using linspace (5 elements between 0 and 10):\n", arr_linspace)

# numpy.empty() - Uninitialized array containing random placeholder values
arr_empty = np.empty([2, 3], dtype=np.int32)
print("Array using empty (placeholder data):\n", arr_empty)

# numpy.ones() - Array completely filled with 1s
arr_ones = np.ones([3, 3], dtype=np.int32)
print("Array using ones:\n", arr_ones)

# numpy.zeros() - Array completely filled with 0s
arr_zeros = np.zeros([2, 4], dtype=np.int32)
print("Array using zeros:\n", arr_zeros)