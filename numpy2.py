import numpy as np

A = np.random.randint(1, 501, 1000)

perfect_squares = np.sum(np.sqrt(A) == np.floor(np.sqrt(A)))
print("Perfect Squares:", perfect_squares)

primes = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                   53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                   113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                   181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                   317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
                   397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                   463, 467, 479, 487, 491, 499])
print("Prime Numbers:", np.isin(A, primes).sum())

B = A.astype(float)
B[B % 7 == 0] = np.sqrt(B[B % 7 == 0])
print("After Replacement:\n", B)

S = np.sort(A)
print("Largest Gap:", np.max(np.diff(S)))

C = np.cumsum(A)
print("Cumulative Sum:\n", C)

print("First Index:", np.argmax(C > 100000))