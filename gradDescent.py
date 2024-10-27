from imports import np, plt
from objfunc import ObjectiveFunction

def gradDescent(obj:ObjectiveFunction, x0, gamma, eps=1e-4, maxIter=1000):
    iter = 0
    x = x0.copy()
    points = [x0.copy()]
    
    while iter < maxIter:
        grad = obj.gradF(x)
        if np.linalg.norm(grad) < eps:
            break
        
        x = [x[j] - gamma * grad[j] for j in range(len(x))]
        points.append(x.copy())
        iter += 1

    fX = obj.f(x)
    
    return x, fX, iter, points