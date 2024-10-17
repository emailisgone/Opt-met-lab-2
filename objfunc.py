class ObjectiveFunction:
    counter = 0

    def __init__(self):
        pass

    def f(self, x):
        ObjectiveFunction.counter += 1
        x1, x2 = x
        return -1/8*(x1*x2-x1**2*x2-x1*x2**2)

    def gradF(self, x):
        ObjectiveFunction.counter += 1
        x1, x2 = x
        return [-1/8*(x2-2*x1*x2-x2**2), -1/8*(x1-2*x1*x2-x1**2)]
    
    def reset(self):
        ObjectiveFunction.counter = 0