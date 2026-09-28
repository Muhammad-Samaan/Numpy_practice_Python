"""
NUMPY PRACTICE NOTES
====================
A practical, beginner-friendly NumPy reference.

Each section is independent:
- It has its own NumPy import.
- It creates its own data.
- You can copy/run any section separately.

The comments explain what the topic is, why it is useful,
and what the important idea is.
"""


# ============================================================
# 01. CREATE AN ARRAY
# ============================================================
# An ndarray is NumPy's main data structure.
# Unlike a normal Python list, NumPy arrays are designed
# for fast numerical operations on many values at once.

import numpy as np

scores = np.array([75, 82, 90, 65])

print(scores)


# ============================================================
# 02. ARRAY PROPERTIES
# ============================================================
# These properties help you understand an array's structure:
# ndim  = number of dimensions
# shape = size of each dimension
# size  = total number of elements
# dtype = data type of the elements

# import numpy as np

scores = np.array([
    [75, 82, 90],
    [60, 70, 65],
    [88, 95, 92],
    [45, 55, 50]
])

print("Dimensions:", scores.ndim)
print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Data type:", scores.dtype)


# ============================================================
# 03. CREATE ARRAYS: zeros(), ones(), identity()
# ============================================================
# These functions create arrays with common starting values.
# zeros()     -> all zeros
# ones()      -> all ones
# identity()  -> 1s on the main diagonal and 0s elsewhere

# import numpy as np

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.identity(4))


# ============================================================
# 04. CREATE ARRAYS: arange() and linspace()
# ============================================================
# arange() creates values using a start/stop/step pattern.
# The stop value is normally NOT included.
#
# linspace() creates a chosen number of evenly spaced values.
# The end value is normally included.

# import numpy as np

print(np.arange(1, 10, 2))
print(np.linspace(1, 5, 8))


# ============================================================
# 05. INDEXING AND SLICING
# ============================================================
# Indexing gets specific values.
# Slicing gets a range of values.
# NumPy indexing starts at 0.

# import numpy as np

scores = np.array([
    [75, 82, 90],
    [60, 70, 65],
    [88, 95, 92],
    [45, 55, 50]
])

print("First student:", scores[0])
print("Student 3:", scores[2, :])
print("Subject 2:", scores[:, 1])
print("One value:", scores[2, 1])
print("First three values:", scores[0, :3])


# ============================================================
# 06. NEGATIVE INDEXING AND REVERSE SLICING
# ============================================================
# Negative indexes count from the end.
# [::-1] reverses an array along that dimension.

# import numpy as np

letters = np.array([
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
])

print("Last row:", letters[-1])
print("Reversed rows:")
print(letters[::-1])


# ============================================================
# 07. RESHAPE
# ============================================================
# reshape() changes the arrangement/shape of an array
# without changing the number of elements.
#
# Important: the old and new shapes must contain
# the same total number of elements.

# import numpy as np

a = np.arange(1, 13)

print("Original:")
print(a)

b = a.reshape(3, 4)

print("Reshaped:")
print(b)
print("New shape:", b.shape)


# ============================================================
# 08. ELEMENT-WISE ARITHMETIC / VECTORIZATION
# ============================================================
# NumPy can perform calculations on an entire array
# without writing a loop.
#
# This is called vectorized/element-wise operation.

# import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)

# A scalar can also be applied to every element.
print(a + 10)
print(a * 10)


# ============================================================
# 09. AGGREGATIONS / STATISTICS
# ============================================================
# Aggregation reduces many values into a summary.
#
# Common functions:
# sum, mean, median, min, max, var, std

# import numpy as np

scores = np.array([51, 42, 63, 43, 85, 56, 74, 85, 92])

print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Variance:", np.var(scores))
print("Standard deviation:", np.std(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Index of minimum:", np.argmin(scores))
print("Index of maximum:", np.argmax(scores))


# ============================================================
# 10. AXIS
# ============================================================
# axis tells NumPy which direction to perform an operation.
#
# axis=0 -> down the rows -> one result per column
# axis=1 -> across the columns -> one result per row

# import numpy as np

scores = np.array([
    [75, 82, 90],
    [60, 70, 65],
    [88, 95, 92],
    [45, 55, 50]
])

print("Average of each subject:", scores.mean(axis=0))
print("Average of each student:", scores.mean(axis=1))

print("Subject totals:", scores.sum(axis=0))
print("Student totals:", scores.sum(axis=1))


# ============================================================
# 11. BOOLEAN MASKING
# ============================================================
# A condition creates a True/False mask.
# Using that mask with the array filters the values.
#
# Example:
# scores > 80 -> True where the score is above 80.

# import numpy as np

scores = np.array([51, 42, 63, 43, 85, 56, 74, 85, 92])

mask = scores > 80

print("Mask:", mask)
print("Scores above 80:", scores[mask])
print("Scores above 80:", scores[scores > 80])


# ============================================================
# 12. MULTIPLE CONDITIONS
# ============================================================
# Use:
# & -> AND
# | -> OR
# ~ -> NOT
#
# Put each condition inside parentheses.

# import numpy as np

ages = np.array([18, 22, 15, 30, 25, 12])

print("Between 20 and 30:", ages[(ages > 20) & (ages < 30)])
print("Under 18 OR over 25:", ages[(ages < 18) | (ages > 25)])


# ============================================================
# 13. MODIFY VALUES USING A MASK
# ============================================================
# Boolean masks can also be used to change selected values.
# Here, scores at or below 50 are replaced with 0.

# import numpy as np

grades = np.array([51, 42, 63, 43, 85, 56, 74, 85, 92])

grades[grades <= 50] = 0

print(grades)


# ============================================================
# 14. BROADCASTING
# ============================================================
# Broadcasting allows compatible arrays/shapes to work together
# without manually repeating the smaller data.
#
# It is heavily used in data science and machine learning.

# import numpy as np

scores = np.array([
    [75, 82, 90],
    [60, 70, 65],
    [88, 95, 92]
])

bonus = np.array([5, 10, 2])

print(scores + bonus)


# ============================================================
# 15. WHERE
# ============================================================
# np.where() can:
# 1. Find positions where a condition is True.
# 2. Choose one value when True and another when False.

# import numpy as np

scores = np.array([
    [75, 82, 90],
    [60, 70, 65],
    [88, 95, 92],
    [45, 55, 50]
])

# Positions where scores are greater than 90.
positions = np.where(scores > 90)
print("Positions:", positions)

# Label each score as Pass/Fail.
result = np.where(scores >= 50, "Pass", "Fail")
print(result)


# ============================================================
# 16. ANY AND ALL
# ============================================================
# any() -> True if at least one value satisfies the condition.
# all() -> True only if every value satisfies the condition.

# import numpy as np

scores = np.array([75, 82, 90])

print("Any score above 85:", np.any(scores > 85))
print("All scores above 50:", np.all(scores > 50))


# ============================================================
# 17. SORTING
# ============================================================
# sort() returns values in sorted order.
# argsort() returns the indexes that would sort the array.
#
# argsort() is useful when you want to sort related data
# using the same ordering.

# import numpy as np

scores = np.array([70, 90, 60, 80])
names = np.array(["Ali", "John", "Sara", "Zain"])

sorted_scores = np.sort(scores)
order = np.argsort(scores)

print("Sorted scores:", sorted_scores)
print("Sorting indexes:", order)
print("Names in score order:", names[order])
print("Scores in score order:", scores[order])


# ============================================================
# 18. UNIQUE VALUES AND COUNTS
# ============================================================
# np.unique() removes duplicate values.
# return_counts=True also tells you how often each value appears.

# import numpy as np

scores = np.array([80, 90, 80, 70, 90, 90, 60])

values, counts = np.unique(scores, return_counts=True)

print("Unique values:", values)
print("Counts:", counts)


# ============================================================
# 19. CONCATENATE, VSTACK AND HSTACK
# ============================================================
# These functions combine arrays.
#
# concatenate() -> join along a chosen axis
# vstack()      -> stack vertically
# hstack()      -> stack horizontally

# import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Concatenate rows:")
print(np.concatenate((a, b), axis=0))

print("Concatenate columns:")
print(np.concatenate((a, b), axis=1))

print("Vertical stack:")
print(np.vstack((a, b)))

print("Horizontal stack:")
print(np.hstack((a, b)))


# ============================================================
# 20. TRANSPOSE
# ============================================================
# Transpose swaps rows and columns.
# A shape such as (2, 3) becomes (3, 2).

# import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original:")
print(a)

print("Transpose:")
print(a.T)


# ============================================================
# 21. COPY VS VIEW
# ============================================================
# A view can share the same underlying data with the original.
# A copy creates independent data.
#
# This difference matters because changing a view can change
# the original array too.

# import numpy as np

a = np.array([10, 20, 30, 40])

view = a[1:]
view[0] = 99

print("Original after changing view:", a)

copy = a[1:].copy()
copy[0] = 500

print("Original after changing copy:", a)
print("Copy:", copy)


# ============================================================
# 22. FLATTEN AND RAVEL
# ============================================================
# Both convert a multi-dimensional array into 1D.
#
# flatten() -> returns a copy
# ravel()   -> returns a view when possible

# import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = a.flatten()
raveled = a.ravel()

print("Flatten:", flat)
print("Ravel:", raveled)


# ============================================================
# 23. NEWAXIS / EXPAND_DIMS
# ============================================================
# These add a dimension without changing the actual data.
# This is useful for controlling shapes and broadcasting.

# import numpy as np

a = np.array([10, 20, 30])

column = a[:, np.newaxis]
row = a[np.newaxis, :]
expanded = np.expand_dims(a, axis=1)

print("Original shape:", a.shape)
print("Column shape:", column.shape)
print("Row shape:", row.shape)
print("Expanded shape:", expanded.shape)


# ============================================================
# 24. RANDOM NUMBERS AND SHUFFLING
# ============================================================
# NumPy's random generator is useful for simulations,
# sampling, shuffling data and machine-learning workflows.

# import numpy as np

rng = np.random.default_rng()

print("Random floats:", rng.random(5))
print("Random integers:", rng.integers(1, 101, size=(3, 3)))

data = np.array([1, 2, 3, 4, 5])
rng.shuffle(data)

print("Shuffled data:", data)


# ============================================================
# 25. FLIP
# ============================================================
# np.flip() reverses the order of values.
# You can flip the whole array or choose an axis.

# import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Flip everything:")
print(np.flip(a))

print("Flip rows:")
print(np.flip(a, axis=0))

print("Flip columns:")
print(np.flip(a, axis=1))


# ============================================================
# 26. NUMERICAL FUNCTIONS / UFUNCS
# ============================================================
# NumPy provides fast mathematical functions that work
# element-by-element on arrays.
#
# These are commonly called universal functions (ufuncs).

# import numpy as np

a = np.array([1.45, 2.465, 3.0, 4.345, 5.0, 8.787])

print("Square root:", np.sqrt(a))
print("Absolute value:", np.abs(a))
print("Rounded to 2 decimals:", np.round(a, 2))
print("Ceiling:", np.ceil(a))
print("Floor:", np.floor(a))
print("Exponential:", np.exp(a))
print("Log:", np.log(a))


# ============================================================
# 27. ASTYPE
# ============================================================
# astype() converts an array to another data type.
# This is useful when preparing data for calculations
# or machine-learning models.

# import numpy as np

a = np.array([1, 2, 3])

print("Original dtype:", a.dtype)

b = a.astype(float)

print("New dtype:", b.dtype)
print(b)


# ============================================================
# 28. KEEPdims
# ============================================================
# keepdims=True keeps the reduced dimension after an
# aggregation. This is useful when you need compatible
# shapes for later calculations.

# import numpy as np

scores = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Without keepdims:", scores.sum(axis=1))
print("With keepdims:", scores.sum(axis=1, keepdims=True))


# ============================================================
# 29. NONZERO
# ============================================================
# np.nonzero() returns the indexes/positions where a
# condition is True.
#
# Boolean masking gives you the values.
# nonzero() gives you their positions.

# import numpy as np

scores = np.array([10, 25, 5, 40, 15])

positions = np.nonzero(scores > 20)

print("Positions:", positions)
print("Values:", scores[scores > 20])


# ============================================================
# 30. SEARCHSORTED
# ============================================================
# searchsorted() finds where a value should be inserted
# to keep a sorted array in order.
#
# The array must already be sorted.

# import numpy as np

a = np.array([10, 20, 30, 40])

position = np.searchsorted(a, 25)

print("Insert 25 at index:", position)


# ============================================================
# 31. LINEAR ALGEBRA: DOT PRODUCT
# ============================================================
# The dot product combines corresponding values and sums
# the results. It is important in mathematical and ML operations.

# import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Dot product:", np.dot(a, b))
print("Dot product using @:", a @ b)


# ============================================================
# 32. MATRIX MULTIPLICATION VS ELEMENT-WISE MULTIPLICATION
# ============================================================
# *  -> multiplies matching elements.
# @  -> performs matrix multiplication.
#
# These are NOT the same operation.

# import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Element-wise multiplication:")
print(A * B)

print("Matrix multiplication:")
print(A @ B)


# ============================================================
# 33. MATRIX INVERSE
# ============================================================
# np.linalg contains NumPy's linear-algebra tools.
# inv() calculates the inverse of a suitable square matrix.
#
# You do not need deep matrix theory yet; just recognize
# this as a basic linear-algebra operation.

# import numpy as np

matrix = np.array([
    [4, -10],
    [3, 2]
])

inverse = np.linalg.inv(matrix)

print("Original matrix:")
print(matrix)

print("Inverse:")
print(inverse)


# ============================================================
# 34. MATRIX MULTIPLICATION WITH SHAPES
# ============================================================
# For A @ B, the inner dimensions must match.
#
# Example:
# (100, 10) @ (10, 5) -> (100, 5)
#
# This idea is important when you later study machine learning.

# import numpy as np

X = np.ones((100, 10))
W = np.ones((10, 5))

Y = X @ W

print("X shape:", X.shape)
print("W shape:", W.shape)
print("Y shape:", Y.shape)


# ============================================================
# 35. SPLITTING ARRAYS
# ============================================================
# Splitting divides an array into smaller arrays.
# array_split() is flexible and can handle uneven splits.

# import numpy as np

a = np.arange(1, 11)

parts = np.array_split(a, 3)

for part in parts:
    print(part)


# ============================================================
# 36. ARRAY DATA TYPE CONVERSION
# ============================================================
# NumPy arrays normally contain values of one common dtype.
# dtype can be specified when creating an array or changed
# later with astype().

# import numpy as np

integers = np.array([1, 2, 3], dtype=np.int32)
floats = integers.astype(np.float64)

print("Integer array:", integers, integers.dtype)
print("Float array:", floats, floats.dtype)


# ============================================================
# 37. SAVE AND LOAD NUMPY ARRAYS
# ============================================================
# .npy stores one NumPy array.
# .npz can store multiple arrays.
#
# This is useful when you want to save numerical data
# and load it again later.

# import numpy as np

a = np.array([10, 20, 30, 40])

np.save("my_array.npy", a)

loaded = np.load("my_array.npy")

print("Loaded array:", loaded)


# ============================================================
# 38. FIXED-SIZE ARRAY CONCEPT
# ============================================================
# NumPy arrays are designed for numerical computation with
# a defined structure. They are not meant for repeatedly
# growing like Python lists.
#
# If you need to build a collection dynamically, a Python list
# is usually more suitable. Convert it to NumPy later.

# import numpy as np

values = []

for number in range(1, 6):
    values.append(number)

array = np.array(values)

print("Python list:", values)
print("NumPy array:", array)


# ============================================================
# 39. SMALL REALISTIC PRACTICE: STUDENT SCORES
# ============================================================
# This combines the main NumPy skills:
# indexing, axis, statistics, masking, broadcasting,
# where(), reshape() and array properties.

# import numpy as np

scores = np.array([
    [75, 82, 90],
    [60, 70, 65],
    [88, 95, 92],
    [45, 55, 50]
])

print("Shape:", scores.shape)
print("Student 3:", scores[2, :])
print("Subject 2:", scores[:, 1])
print("Student averages:", scores.mean(axis=1))
print("Subject averages:", scores.mean(axis=0))
print("Highest score:", scores.max())
print("Scores above 80:", scores[scores > 80])
print("Positions above 90:", np.where(scores > 90))
print("With +5 bonus:")
print(scores + 5)
print("Reshaped:")
print(scores.reshape(2, 6))
