from objfunc import ObjectiveFunction

class SimplexOptimizer:
    def __init__(self, obj:ObjectiveFunction, alpha=1, beta=0.5, gamma=2, nu=0.5, eps=1e-4, maxIter=1000):
        self.obj_func = obj  
        self.alpha = alpha  
        self.beta = beta  
        self.gamma = gamma  
        self.nu = nu  
        self.epsilon = eps
        self.max_iter = maxIter

    def optimize(self, initial_point):
        n = len(initial_point) 
        
        simplex = [initial_point]
        for i in range(n):
            new_point = initial_point.copy()
            new_point[i] += self.alpha  
            simplex.append(new_point)

        iteration = 0
        while iteration < self.max_iter:
            simplex.sort(key=lambda x: self.obj_func.f(x))
            best = simplex[0]
            worst = simplex[-1]
            second_worst = simplex[-2]

            centroid = [(sum([simplex[i][j] for i in range(n)]) - worst[j]) / n for j in range(n)]

            reflection = [centroid[j] + self.alpha * (centroid[j] - worst[j]) for j in range(n)]
            f_reflection = self.obj_func.f(reflection)

            if self.obj_func.f(best) <= f_reflection < self.obj_func.f(second_worst):
                simplex[-1] = reflection  
            else:
                if f_reflection < self.obj_func.f(best):

                    expansion = [centroid[j] + self.gamma * (reflection[j] - centroid[j]) for j in range(n)]
                    if self.obj_func.f(expansion) < f_reflection:
                        simplex[-1] = expansion
                    else:
                        simplex[-1] = reflection
                else:
                    contraction = [centroid[j] + self.nu * (worst[j] - centroid[j]) for j in range(n)]
                    if self.obj_func.f(contraction) < self.obj_func.f(worst):
                        simplex[-1] = contraction
                    else:
                        for i in range(1, len(simplex)):
                            simplex[i] = [best[j] + self.beta * (simplex[i][j] - best[j]) for j in range(n)]

            if all(abs(self.obj_func.f(simplex[0]) - self.obj_func.f(simplex[i])) < self.epsilon for i in range(1, len(simplex))):
                break

            iteration += 1

        return simplex[0], self.obj_func.f(simplex[0]), iteration