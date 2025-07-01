import numpy as np

def validate_solution(A, x, b, tol=1e-6):
    return np.allclose(A.dot(x), b, atol=tol)
