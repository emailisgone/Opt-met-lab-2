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
from imports import datetime, math, np, sp, plt
from objfunc import ObjectiveFunction
from gradDescent import gradDescent
from steepDescent import steepDescent
from simplex import simplex
from test import SimplexOptimizer
from scipy.optimize import minimize

print(f"{datetime.now()}")

'''obj = ObjectiveFunction()
res1 = obj.gradF([0.5, 0.7])
res2 = obj.f([0.3, 0.3])
print(str(res1) + " " + str(res2))
print(obj.counter)

obj.reset()
res3 = obj.f([0, 0])
print(res3)
print(obj.counter)'''

obj = ObjectiveFunction()
point = [0.3, 0.3]

a, b, c= gradDescent(obj, point, 1)
print(a)
print(b)
print(c)
print(obj.counter)

obj.reset()
print("----------------------[STEEP DESCENT]------------------------")
a, b, c= steepDescent(obj, point)
print(a)
print(b)
print(c)
print(obj.counter)
obj.reset()
print("----------------------[SIMPLEX]------------------------")
'''a, b, c= simplex(obj, point, 2, 1.0, 0.5, 2.0, 0.5)
#simpleksu = SimplexOptimizer(obj)
#a,b,c=simpleksu.optimize(point)
print(a)
print(b)
print(c)
print(obj.counter)
obj.reset()
'''

'''x = minimize(obj.f, point, method='Nelder-Mead') -  the "true" simplex solution from the scipy lib
print(x.x)'''