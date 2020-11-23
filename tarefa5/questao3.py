import math

def trapezioComposta(a, b, k):
	n = 6*k + 1 # numero de pontos
	h = (b-a)/(n-1) # n-1 = numero de sub-intervalos
	resultado = 0.0
	x0 = a
	x1 = a+h
	for i in range(6*k):
		resultado += (h/2)*(f(x0) + f(x1))
		x0 = x1 
		x1 = x1 + h
	return resultado

def simpson13(a, b, k): #Regra de 1/3 de Simpson
	n = 6*k + 1
	h = ((b-a)/(n-1))
	resultado = 0.0
	x0 = a
	x1 = a+h
	x2 = x1+h
	y = 0
	for i in range(3*k):
		resultado += (h/3) * (f(x0) + 4*f(x1) + f(x2))
		x0 = x2
		x1 = x0+h
		x2 = x1+h
	return resultado

def simpson38(a, b, k): #Regra de 3/8 de Simpson
	n = 6*k+1
	h = ((b-a)/(n-1))
	resultado = 0.0
	x0 = a
	x1 = a+h
	x2 = x1 + h
	x3 = x2 + h
	for i in range(2*k):
		resultado += (3*h/8) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3))
		x0 = x3
		x1 = x0+h
		x2 = x1+h
		x3 = x2+h
	return resultado

def f(x):
	return x*math.sin(x)


def analiticF(x):
	return 2*(math.sin(x) - (5*(math.cos(5))))

k = int(input("digite o valor de k: "))
print("Regra do trapezio composta com k = " + str(k) + " => " + str(trapezioComposta(-5.0, 5.0, k)))
print("Regra um terco de simpson com k = " + str(k) + " => " + str(simpson13(-5.0, 5.0, k)))
print("Regra tres oitavos de simpson com k = " + str(k) + " => " + str(simpson38(-5.0, 5.0, k)))
print("Resolucao analitica: " + str(analiticF(5)))
