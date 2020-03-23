import math
h = 0.05
y = 1
x = 0
arq = open("pontos positivos.pts", "w")
arq2 = open("pontos negativos.pts", "w")
for i in range(100):
    y = -((math.cos(x) - (x*math.sin(x))) * h) + y 
    x = x-h
    arq2.write("%f %f\n" %(x, y)) 
y = 1
x = 0
arq.write("%f %f\n" %(x, y))
for i in range(100):
    y = (math.cos(x) - (x*math.sin(x))) * h + y
    x = x+h
    arq.write("%f %f\n" %(x, y))
arq.close()
arq2.close()
