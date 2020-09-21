import math
def secante(x, y):
    #x = Xn
    #y = Xn-1
    for i in range(6):
        aux = x
        x = (y*f(x) - x*f(y))/(f(x) - f(y))
        y = aux 
    return x
def f(x):
    return x**2 + 25600/(((240/math.sqrt(900 - x**2)*x)/30) - x)**2 - 20**2

print("Valor de L aproximadamente: " + str(secante(5, 4)))

