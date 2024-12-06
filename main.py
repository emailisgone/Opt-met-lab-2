from imports import datetime, math, np, sp, plt, scp
from objfunc import ObjectiveFunction
from plotfunc import graph
from gradDescent import gradDescent
from steepDescent import steepDescent
from simplex import simplex

print(f"{datetime.now()}\n")

obj = ObjectiveFunction()
point = [0.5,0.7]
gamma = 0.3 # Gammas to analyze: 0.001, 0.003, 0.01, 0.03, 0.1, 0.3

a, b, c, points = gradDescent(obj, point, gamma)
print(f"Minimum point: {a}")
print(f"Value @ min. point: {b}")
print(f"nit: {c}")
print(f"nfev: {obj.counter}")

#graph(obj, point, points, 1, gamma)

obj.reset()
print("----------------------[STEEP DESCENT]------------------------")
a, b, c, points = steepDescent(obj, point)
print(f"Minimum point: {a}")
print(f"Value @ min. point: {b}")
print(f"nit: {c}")
print(f"nfev: {obj.counter}")

#graph(obj, point, points, 2, 0, [0,20])

obj.reset()
print("----------------------[SIMPLEX SciPy]------------------------")
print(scp.optimize.minimize(obj.f, point, method='Nelder-Mead'))

obj.reset()
print("----------------------[SIMPLEX CUSTOM]------------------------")
a, b, c, points = simplex(obj, point)
print(f"Minimum point: {a}")
print(f"Value @ min. point: {b}")
print(f"nit: {c}")
print(f"nfev: {obj.counter}")

#graph(obj, point, points, 3)

obj.reset()