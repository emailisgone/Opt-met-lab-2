from imports import np

def f(x):
    x1, x2 = x
    return -1/8*(x1*x2*(1-x1-x2))

def gradF(x):
    x1, x2 = x
    return [-1/8*(x2-2*x1*x2-x2**2), -1/8*(x1-2*x1*x2-x1**2)]