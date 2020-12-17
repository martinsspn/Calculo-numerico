arq = open("pesos.txt", "r")
n = arq.readlines()
xi = []
yi = []
for i in range(len(n)):
	xi.append(float(n[i].split()[0]))
	yi.append(float(n[i].split()[1]))


SumXi = 0
SumXi2 = 0
SumYi = 0
SumXiYi = 0
for i in range(len(n)):
	SumXi += xi[i]
	SumXi2 += xi[i]**2
	SumYi += yi[i]
	SumXiYi += xi[i]*yi[i]
print SumXi, SumXi2, SumYi, SumXiYi
