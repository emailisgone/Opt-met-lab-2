from imports import np

def f(x):
    x1, x2 = x
    return -1/8*(x1*x2*(1-x1-x2))

def gradF(x):
    x1, x2 = x
    dfdx1 = -1/8*(x2-2*x1*x2-x2**2)
    dfdx2 = -1/8*(x1-2*x1*x2-x1**2)
    return np.array([dfdx1, dfdx2])