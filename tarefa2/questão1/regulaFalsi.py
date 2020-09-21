def regulaFalsi(a, b):
    c = 0
    for i in range(0, 20):
        c = b - (f(b)*(b-a))/(f(b) - f(a))
        if ((f(a) > 0 and f(c) > 0) or (f(a) < 0 and f(c) < 0)):
            a = c
        else:
            b = c
    return c

def f(x):
    return x**3-1.7*(x**2)-12.78*x-10.08

arq = open("ptsRegulaFalsi.pts", "w")
arq.write(str(regulaFalsi(-2.2, -1.9)) + " 0\n")
arq.write(str(regulaFalsi(-1.5, 1)) + " 0\n")
arq.write(str(regulaFalsi(5, 1)) + " 0\n")
