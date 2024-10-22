from objfunc import ObjectiveFunction

def simplex(obj:ObjectiveFunction, x0, init_step=0.025, step_coeff=1.025, eps=1e-4, alpha=1, gamma=2, rho=0.5, sigma=0.5):
    dim = len(x0)
    pond = [x0]
    f_values = [obj.f(x0)]
    iter = 0
    
    for i in range(dim):
        x_temp = x0.copy()
        if x_temp[i] == 0:
            x_temp[i] = init_step
        else:
            x_temp[i] *= step_coeff
        pond.append(x_temp)
        f_values.append(obj.f(x_temp))
    
    while True:
        iter += 1
        #print(iter)
        sorted_indices = sorted(range(len(f_values)), key=lambda i: f_values[i])
        pond = [pond[i] for i in sorted_indices]
        f_values = [f_values[i] for i in sorted_indices]
        
        x_m = [sum([pond[i][j] for i in range(len(pond) - 1)]) / dim for j in range(dim)]
        
        x_r = [x_m[j] + alpha * (x_m[j] - pond[-1][j]) for j in range(dim)]
        y_r = obj.f(x_r)
        
        if f_values[0] <= y_r < f_values[-2]:
            pond[-1], f_values[-1] = x_r, y_r
        elif y_r < f_values[0]:
            x_e = [x_m[j] + gamma * (x_m[j] - pond[-1][j]) for j in range(dim)]
            y_e = obj.f(x_e)
            if y_e < y_r:
                pond[-1], f_values[-1] = x_e, y_e
            else:
                pond[-1], f_values[-1] = x_r, y_r
        else:
            x_c = [x_m[j] + rho * (pond[-1][j] - x_m[j]) for j in range(dim)]
            y_c = obj.f(x_c)
            if y_c < f_values[-1]:
                pond[-1], f_values[-1] = x_c, y_c
            else:
                for i in range(1, len(pond)):
                    pond[i] = [pond[0][j] + sigma * (pond[i][j] - pond[0][j]) for j in range(dim)]
                    f_values[i] = obj.f(pond[i])
        
        x_error = max([sum((pond[i][j] - pond[0][j]) ** 2 for j in range(dim)) ** 0.5 for i in range(1, len(pond))])
        y_error = abs(f_values[0] - f_values[-1])
        
        if x_error < eps and y_error < eps:
            break
    
    return pond[0], f_values[0], iter