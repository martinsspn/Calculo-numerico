import math

def simpson13(a, b): #Regra de 1/3 de Simpson
	h = ((b-a)/(2))
	return (h/3) * (f(a) + 4*f(a+h) + f(b))

def simpson38(a, b): #Regra de 3/8 de Simpson
	h = ((b-a)/3)
	x1 = a+h
	x2 = x1 + h
	return ((3*h)/8) * (f(a) + 3*f(x1) + 3*f(x2) + f(b))

def f(x):
	return x*math.sin(math.radians(x))

print("regra um terco de simpson: " + str(simpson13(-5.0, 5.0)))
print("regra tres oitavos de simpson: " + str(simpson38(-5.0, 5.0)))
