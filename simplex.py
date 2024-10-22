from objfunc import ObjectiveFunction

def simplex(obj:ObjectiveFunction, x0, initStep=0.025, stepCoeff=1.025, eps=1e-4, alpha=1, gamma=2, rho=0.5, sigma=0.5, maxIter=200):
    n = len(x0)
    pond = [x0]
    fVals = [obj.f(x0)]
    iter = 0
    
    # Creating the other initial points to make n+1 angled figure (triangle in this case)
    for i in range(n):
        xTemp = x0.copy()
        if xTemp[i] == 0:
            xTemp[i] = initStep
        else:
            xTemp[i] *= stepCoeff
        pond.append(xTemp)
        fVals.append(obj.f(xTemp))
    
    # Main loop
    while True and iter < maxIter:
        iter += 1

        # Sort in ascending order, where pond[0] - best value(f(pond[0] the smallest = closest to minimum)), pond[-1] - worst
        sortedInd = sorted(range(len(fVals)), key=lambda i: fVals[i])
        pond = [pond[i] for i in sortedInd]
        fVals = [fVals[i] for i in sortedInd]
        
        # Establishing centroid by averaging coordinates of other points
        x_m = [sum([pond[i][j] for i in range(len(pond) - 1)]) / n for j in range(n)]
        
        # Creating a reflection of the worst point (highest f(pond[-1]) OR furthest from minimum point)
        x_r = [x_m[j] + alpha * (x_m[j] - pond[-1][j]) for j in range(n)]
        y_r = obj.f(x_r)
        
        # If the reflected point’s function value < second-worst point BUT >= the best point, the worst point is -> reflected point
        if fVals[0] <= y_r < fVals[-2]:
            pond[-1], fVals[-1] = x_r, y_r
        # If the reflected point > best point, an expansion point x_e is established
        elif y_r < fVals[0]:
            x_e = [x_m[j] + gamma * (x_m[j] - pond[-1][j]) for j in range(n)]
            y_e = obj.f(x_e)
            if y_e < y_r:
                pond[-1], fVals[-1] = x_e, y_e
            else:
                pond[-1], fVals[-1] = x_r, y_r
        # If the reflected point < the second-worst point, a contraction point x_c is established. If the contraction improves the worst point, the worst point = contraction point. Otherwise, the entire simplex is shrunk toward the best point (pond[0]).
        else:
            x_c = [x_m[j] + rho * (pond[-1][j] - x_m[j]) for j in range(n)]
            y_c = obj.f(x_c)
            if y_c < fVals[-1]:
                pond[-1], fVals[-1] = x_c, y_c
            else:
                for i in range(1, len(pond)):
                    pond[i] = [pond[0][j] + sigma * (pond[i][j] - pond[0][j]) for j in range(n)]
                    fVals[i] = obj.f(pond[i])
        
        # Precision check !!!!! Decided to handle both points separately here just INCASE
        xErr = max([sum((pond[i][j] - pond[0][j]) ** 2 for j in range(n)) ** 0.5 for i in range(1, len(pond))])
        yErr = abs(fVals[0] - fVals[-1])
        
        if xErr < eps and yErr < eps:
            break
    
    return pond[0], fVals[0], iter