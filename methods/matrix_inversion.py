import numpy as np

def solve(A, b):
    A = A.astype(float)
    try:
        A_inv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        raise ValueError("Matrix A is singular and cannot be inverted.")
    x = A_inv.dot(b)
    steps = [(A, b, A_inv)]
    return x, steps
