from imports import plt, np
from objfunc import ObjectiveFunction

def graph(obj:ObjectiveFunction, initialPoint, points, methodId):
    match methodId:
        case 1:
            methodName = 'Gradientinio nusileidimo optimizacijos kelias'
        case 2:
            methodName = 'Greičiausio nusileidimo optimizacijos kelias'
        case 3:
            methodName = 'Simplekso optimizacijos kelias'

    x = np.linspace(-0.5, 1.5, 100)
    y = np.linspace(-0.5, 1.5, 100)
    X, Y = np.meshgrid(x, y)

    Z = np.zeros_like(X)
    for i in range(len(x)):
        for j in range(len(y)):
            Z[i,j] = obj.f([X[i,j], Y[i,j]])

    plt.figure(figsize=(10, 8))
    plt.contour(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)
    plt.colorbar(label='Objektinės funkcijos reikšmė')
    
    if methodId==1 or methodId==2:
        points = np.array(points)
        plt.scatter(initialPoint[0], initialPoint[1], color='red', marker='o', s=100, label='Nulinis taškas')
        plt.plot(points[:,0], points[:,1], 'r.-', alpha=0.5, label='Optimizacijos kelias')
        plt.scatter(points[-1,0], points[-1,1], color='green', marker='*', s=200, label='Minimumo taškas')
        
    elif methodId == 3:
        plt.scatter(initialPoint[0], initialPoint[1], color='red', marker='o', s=100, label='Nulinis taškas')
        
        for i, triangle in enumerate(points):
            alpha = max(0.1, 1 - i/len(points)) 
            triangle = np.array(triangle)
            plt.plot([triangle[0,0], triangle[1,0], triangle[2,0], triangle[0,0]], 
                    [triangle[0,1], triangle[1,1], triangle[2,1], triangle[0,1]], 
                    'b-', alpha=alpha)
        
        final_triangle = np.array(points[-1])
        plt.scatter(final_triangle[0,0], final_triangle[0,1], color='green', 
                   marker='*', s=200, label='Minimumo taškas')
        
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{methodName}')
    plt.legend(loc=2)
    plt.grid(True, alpha=0.3)
    plt.show()

        
    

