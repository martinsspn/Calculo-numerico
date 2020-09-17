def secante(x, y):
    #x = Xn
    #y = Xn-1
    for i in range(0, 5):
        aux = x
        x = (y*f(x) - x*f(y))/(f(x) - f(y))
        y = aux
    return x

def f(x):
    return x**3 - 1.7*(x**2) - 12.78*x - 10.08

arq = open("ptsSecante.pts", "w")
arq.write(str(secante(-3, -3.2)) + " 0\n")
arq.write(str(secante(-1.4, -1.5)) + " 0\n")
arq.write(str(secante(3, 2)) + " 0\n")
