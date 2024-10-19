from objfunc import ObjectiveFunction

def simplex(obj:ObjectiveFunction, x0, n, alpha, beta, gamma, nu, eps=1e-4, maxIter=1000):
    def create_simplex(x0, alpha):
        simplex = [x0]
        for i in range(n):
            point = x0.copy()
            point[i] += alpha
            simplex.append(point)
        return simplex

    def calculate_centroid(simplex, exclude_index):
        centroid = [sum(point[i] for j, point in enumerate(simplex) if j != exclude_index) / n 
                    for i in range(n)]
        return centroid

    simplex = create_simplex(x0, alpha)
    
    i = 0
    for _ in range(maxIter):
        i+=1
        simplex.sort(key=lambda x: obj.f(x))
        
        xl, xg, xh = simplex[0], simplex[-2], simplex[-1]
        
        xc = calculate_centroid(simplex, -1)
        
        xr = [2 * xc[i] - xh[i] for i in range(n)]
        f_xr = obj.f(xr)
        
        if obj.f(xl) <= f_xr < obj.f(xg):
            simplex[-1] = xr
            continue
        
        if f_xr < obj.f(xl):
            xe = [gamma * xr[i] + (1 - gamma) * xc[i] for i in range(n)]
            if obj.f(xe) < f_xr:
                simplex[-1] = xe
            else:
                simplex[-1] = xr
            continue
        
        xk = [beta * xh[i] + (1 - beta) * xc[i] for i in range(n)]
        if obj.f(xk) < obj.f(xh):
            simplex[-1] = xk
            continue
        
        x1 = simplex[0]
        for i in range(1, n + 1):
            simplex[i] = [x1[j] + nu * (simplex[i][j] - x1[j]) for j in range(n)]
        
        if max(abs(obj.f(simplex[i]) - obj.f(simplex[0])) for i in range(1, n + 1)) < eps:
            break
    
    best_point = min(simplex, key=obj.f)
    return best_point, obj.f(best_point), i