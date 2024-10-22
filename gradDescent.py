from imports import np
from objfunc import ObjectiveFunction

def gradDescent(obj:ObjectiveFunction, x0, gamma, eps=1e-4, maxIter=1000):
    iter = 0
    x = x0.copy()
    
    while iter < maxIter:
        grad = obj.gradF(x)
        if np.linalg.norm(grad) < eps:
            break
        
        x = [x[j] - gamma * grad[j] for j in range(len(x))]
        iter += 1

    fX = obj.f(x)
    
    return x, fX, iter

def gradTest(obj: ObjectiveFunction, x0, gamma, eps=1e-4, maxIter=1000):
    """
    Basic gradient descent following the algorithm from slides:
    1. i = 0
    2. x_{i+1} = x_i - γ∇f(x_i)
    3. if gradient is small enough (||∇f(x_i)|| < ε), stop; else i = i + 1 and go to step 2
    
    Args:
        obj: ObjectiveFunction instance with f(x) and gradF(x) methods
        x0: Initial point (list of coordinates)
        gamma: Learning rate (γ)
        eps: Convergence threshold (ε)
        maxIter: Maximum number of iterations
    
    Returns:
        x_next: Final point found
        f_next: Function value at final point
        i: Number of iterations
    """
    # 1. i = 0
    i = 0
    x_current = x0.copy()  # Make a copy to not modify the input
    
    while i < maxIter:
        # Calculate gradient at current point
        gradient = obj.gradF(x_current)
        
        # Check if gradient is small enough
        gradient_norm = sum(g**2 for g in gradient)**0.5  # ||∇f(x_i)||
        if gradient_norm < eps:
            break
            
        # 2. x_{i+1} = x_i - γ∇f(x_i)
        x_next = [x_current[j] - gamma * gradient[j] for j in range(len(x_current))]
        
        # Update current point
        x_current = x_next
        
        # 3. i = i + 1
        i += 1
    
    # Calculate final function value
    f_next = obj.f(x_current)
    
    return x_current, f_next, i