'''
Kokia turėtų būti stačiakampio gretasienio formos dėžė, kad vienetiniam paviršiausplotui jos tūris būtų maksimalus?

1. Suprogramuokite gradientinio nusileidimo, greičiausiojo nusileidimo ir deformuojamo simplekso algoritmus.
2. Laikant kintamaisiais dėžės priekinės ir galinės sienų plotų sumą, šoninių sienų plotų sumą, viršutinės ir apatinės sienų plotų sumą, aprašykite vienetinio dėžės paviršiaus ploto reikalavimą ir dėžės tūrio pakelto kvadratu funkciją.
3. Iš vienetinio paviršiaus ploto reikalavimo išveskite vieno iš kintamojo išraišką per kitus.
4. Aprašykite tikslo funkciją f(X) taip, kad optimizavimo uždavinys būtų formuluojamas be apribojimų: min f(X).
5. Išveskite ir aprašykite tikslo funkcijos gradiento funkciją.
6. Apskaičiuokite tikslo ir gradiento funkcijų reikšmes taškuose X0= (0,0), X1=(1,1) ir Xm= (5/10, 7/10).
7. Minimizuokite suformuluotą uždavinį naudojant suprogramuotus optimizavimo algoritmus pradedant iš taškų X0, X1 ir Xm.
8. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius priklausomai nuo pradinio taško.
9. Vizualizuokite tikslo funkciją ir bandymo taškus.
'''
from imports import datetime, math, np, sp, plt, scp
from objfunc import ObjectiveFunction
from gradDescent import gradDescent
from steepDescent import steepDescent
from simplex import simplex

print(f"{datetime.now()}\n")

obj = ObjectiveFunction()
point = [0,0]
gamma = 0.3 # Gammas to analyze: 0.001, 0.003, 0.01, 0.03, 0.1, 0.3

a, b, c = gradDescent(obj, point, gamma)
print(f"Minimum point: {a}")
print(f"Value @ min. point: {b}")
print(f"nit: {c}")
print(f"nfev: {obj.counter}")

obj.reset()
print("----------------------[STEEP DESCENT]------------------------")
a, b, c = steepDescent(obj, point)
print(f"Minimum point: {a}")
print(f"Value @ min. point: {b}")
print(f"nit: {c}")
print(f"nfev: {obj.counter}")

obj.reset()
print("----------------------[SIMPLEX SciPy]------------------------")
print(scp.optimize.minimize(obj.f, point, method='Nelder-Mead'))

obj.reset()
print("----------------------[SIMPLEX CUSTOM]------------------------")
a, b, c = simplex(obj, point)
print(f"Minimum point: {a}")
print(f"Value @ min. point: {b}")
print(f"nit: {c}")
print(f"nfev: {obj.counter}")

obj.reset()