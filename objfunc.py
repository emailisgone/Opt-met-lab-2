class ObjectiveFunction:
    counter = 0

    def __init__(self):
        pass

    def f(self, x):
        ObjectiveFunction.counter += 1
        return -1/8*(x[0]*x[1]-x[0]**2*x[1]-x[0]*x[1]**2)

    def gradF(self, x):
        ObjectiveFunction.counter += 1
        return [-1/8*(x[1]-2*x[0]*x[1]-x[1]**2), -1/8*(x[0]-2*x[0]*x[1]-x[0]**2)]
    
    def reset(self):
        ObjectiveFunction.counter = 0