import numpy as np

A = np.arange(1, 101).reshape(10, 10)

print("Prime Rows:\n", A[[1, 2, 4, 6]])

B = A.copy()
B[:, 1::2] = B[::-1, 1::2]
print("\nAlternate Columns Reversed:\n", B)

C = A.copy()
np.fill_diagonal(C, 0)
print("\nDiagonal Replaced with 0:\n", C)

border_sum = A[0].sum() + A[-1].sum() + A[1:-1, 0].sum() + A[1:-1, -1].sum()
print("\nBorder Sum =", border_sum)

print("\n90° Clockwise Rotation:\n", np.rot90(A, -1))