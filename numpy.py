import numpy as np

arr = (np.arange(1, 21) ** 2 + 1).reshape(4, 5)

print("Original Matrix:")
print(arr)
print("\nRelationship:")
print("Each element = n^2 + 1")

double_arr = arr * 2

print("\nTwice the Original Matrix:")
print(double_arr)

modified = arr.copy()
modified[modified % 5 == 0] = -1

print("\nModified Matrix:")
print(modified)

count = np.sum(arr % 5 == 0)

print("\nNumbers Replaced:", count)