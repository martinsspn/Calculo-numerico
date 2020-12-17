arq = open("barcos.txt", "r")
n = arq.readlines()
xi = []
yi = []
for i in range(len(n)):
	xi.append(float(n[i].split()[0]))
	yi.append(float(n[i].split()[1]))

SumXi0 = 0
SumXi1 = 0
SumXi2 = 0
SumXi3 = 0
SumXi4 = 0
SumYi = 0
SumYiXi = 0
SumYiXi2 = 0
for i in range(len(n)):
	SumXi0 += 1
	SumXi1 += xi[i]
	SumXi2 += xi[i]**2
	SumXi3 += xi[i]**3
	SumXi4 += xi[i]**4
	SumYi += yi[i]
	SumYiXi += xi[i]*yi[i]
	SumYiXi2 += ((xi[i])**2)*yi[i]
print SumXi0, SumXi1, SumXi2, SumYi
print SumXi1, SumXi2, SumXi3, SumYiXi
print SumXi2, SumXi3, SumXi4, SumYiXi2