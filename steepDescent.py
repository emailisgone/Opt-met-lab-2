from objfunc import ObjectiveFunction
from imports import np
from scipy.optimize import minimize_scalar

def steepDescent(obj:ObjectiveFunction, x0, eps=1e-4, maxIter=1000):
    i = 0
    x = x0.copy()
    
    while i < maxIter:
        grad = obj.gradF(x)
        
        if sum(g**2 for g in grad)**0.5 < eps:
            break
        
        def line_objective(gamma):
            return obj.f([x[j] - gamma * grad[j] for j in range(len(x))])
        
        res = minimize_scalar(line_objective, method='brent')
        gammaOpt = res.x
        
        x = [x[j]-gammaOpt*grad[j] for j in range(len(x))]
        i += 1
    
    return x, obj.f(x), i