# Python program for
# Creation of Arrays
import numpy as np

# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n", arr)

# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)


                        #############################

# Python program to demonstrate
# indexing in numpy array
import numpy as np

# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print("Array with first 2 rows and"
      " alternate columns(0 and 2):\n", sliced_arr)

# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print("\nElements at indices (1, 3), "
      "(1, 2), (0, 1), (3, 0):\n", Index_arr)


            ############################


# Python program to demonstrate
# basic operations on single array
import numpy as np

# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])

# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])

# Adding 1 to every element
print("Adding 1 to every element:", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array "
      "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)


            #########################

# Python Program to create
# a data type object
import numpy as np

# Integer datatype
# guessed by Numpy
x = np.array([1, 2])
print("Integer Datatype: ")
print(x.dtype)

# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0])
print("\nFloat Datatype: ")
print(x.dtype)

# Forced Datatype
x = np.array([1, 2], dtype=np.int64)
print("\nForcing a Datatype: ")
print(x.dtype)



# import numpy as np
#
# a_1d = np.arange(3)
# print(a_1d)
# # [0 1 2]
#
# a_2d = np.arange(12).reshape((3, 4))
# print(a_2d)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
#
# a_3d = np.arange(24).reshape((2, 3, 4))
# print(a_3d)
# # [[[ 0  1  2  3]
# #   [ 4  5  6  7]
# #   [ 8  9 10 11]]
# #
# #  [[12 13 14 15]
# #   [16 17 18 19]
# #   [20 21 22 23]]]
