import math

def trapezioComposta(a, b, n):
	h = (b-a)/n
	resultado = 0
	x0 = a
	x1 = a+h
	for i in range(n):
		resultado += (h/2)*(f(x0) + f(x1))
		x0 = x1 
		x1 = x1 + h
	return resultado

def f(x):
	return x*math.sin(x)

print(trapezioComposta(-5.0, 5.0, 5))
print(trapezioComposta(-5.0, 5.0, 10))
print(trapezioComposta(-5.0, 5.0, 100))
