import numpy as np

def solve(A, b, tol=1e-6, max_iter=50):
    n = len(b)
    x = np.zeros(n)
    steps = []
    errors = []
    D = np.diag(A)
    if np.any(np.isclose(D, 0)):
        raise ValueError("Zero found on diagonal of matrix A.")
    R = A - np.diagflat(D)
    for it in range(max_iter):
        x_new = (b - R.dot(x)) / D
        err = np.linalg.norm(x_new - x)
        steps.append(x_new.copy())
        errors.append(err)
        if err < tol:
            break
        x = x_new
    return x_new, steps, errors
