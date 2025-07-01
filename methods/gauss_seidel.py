import numpy as np

def solve(A, b, tol=1e-6, max_iter=50):
    n = len(b)
    x = np.zeros(n)
    steps = []
    errors = []
    for it in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            if np.isclose(A[i, i], 0):
                raise ValueError(f"Zero pivot encountered at row {i}.")
            sigma = sum(A[i,j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i,i]
        err = np.linalg.norm(x - x_old)
        steps.append(x.copy())
        errors.append(err)
        if err < tol:
            break
    return x, steps, errors
