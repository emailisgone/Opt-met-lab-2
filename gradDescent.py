from imports import np
from objfunc import ObjectiveFunction

def gradDescent(obj:ObjectiveFunction, x0, gamma, eps=1e-4, maxIter=1000):
    i = 0
    x = x0.copy()
    
    while i < maxIter:
        grad = obj.gradF(x)
        if np.linalg.norm(grad) < eps:
            break
        
        x = [x[j] - gamma * grad[j] for j in range(len(x))]
        i += 1

    fX = obj.f(x)
    
    return x, fX, i