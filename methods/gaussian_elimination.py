import numpy as np

def solve(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = len(b)
    steps = []
    for k in range(n-1):
        if np.isclose(A[k, k], 0):
            raise ValueError(f"Zero pivot encountered at row {k}.")
        for i in range(k+1, n):
            factor = A[i,k] / A[k,k]
            A[i,k:] -= factor * A[k,k:]
            b[i]    -= factor * b[k]
            steps.append((A.copy(), b.copy()))
    x = np.zeros(n)
    for i in reversed(range(n)):
        if np.isclose(A[i, i], 0):
            raise ValueError(f"Zero pivot encountered at row {i} during back substitution.")
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
    return x, steps
