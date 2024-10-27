from objfunc import ObjectiveFunction
from imports import np, plt
import math

def steepDescent(obj:ObjectiveFunction, x0, eps=1e-4, maxIter=200):
    iter = 0
    x = x0.copy()
    points = [x0.copy()]
    optimalGamma = 0
    while iter < maxIter:
        grad = obj.gradF(x)
        
        if np.linalg.norm(grad) < eps:
            break
        
        def objective(gamma):
            return obj.f([x[j] - gamma * grad[j] for j in range(len(x))])
        
        l, r = 0, 1
        tau = (math.sqrt(5)-1)/2
        L = r-l
        x1 = l+(1-tau)*L
        x2 = l+tau*L
        fx1 = objective(x1)
        fx2 = objective(x2)
        
        while (r-l) > eps:
            if fx1 < fx2:
                r = x2
                x2 = x1
                fx2 = fx1
                L = r-l
                x1 = l+(1-tau)*L
                fx1 = objective(x1)
            else:
                l = x1
                x1 = x2
                fx1 = fx2
                L = r-l
                x2 = l+tau*L
                fx2 = objective(x2)
                
        gammaOpt = (l+r)/2
        optimalGamma = gammaOpt
        
        x = [x[j]-gammaOpt*grad[j] for j in range(len(x))]
        points.append(x.copy())
        iter += 1
    
    print(optimalGamma)
    return x, obj.f(x), iter, points