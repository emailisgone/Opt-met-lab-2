from imports import np
from objfunc import ObjectiveFunction

def f(x):
    return -1/8*(x[0]*x[1]-x[0]**2*x[1]-x[0]*x[1]**2)

def gradDescent(obj:ObjectiveFunction, x0, gamma, eps=1e-4, maxIter=10000):
    iter = 0
    x = x0.copy()
    points = [x0.copy()]
    
    while iter < maxIter:
        grad = obj.gradF(x)
        if np.linalg.norm(grad) < eps:
            break
        
        x = [x[j] - gamma * grad[j] for j in range(len(x))]
        points.append(x.copy())

        '''if iter%50==0:
            print(f"[{iter}]: x = {x}, f(x) = {f(x)}, func. calls = {obj.counter}")'''

        iter += 1

    fX = obj.f(x)
    
    return x, fX, iter, points