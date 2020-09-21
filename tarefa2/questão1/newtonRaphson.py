def newthonRaphson(x):
    for n in range (0,100):
        x = x - ((x**3 - 1.7*(x**2) - 12.78*x - 10.08)/(3*x**2 - 3.4*x - 12.78))
    return x

arq = open("ptsNewtonRaphson.pts", "w")
arq.write(str(newthonRaphson(-3)) + " 0\n")
arq.write(str(newthonRaphson(-1.5)) + " 0\n")
arq.write(str(newthonRaphson(4)) + " 0 \n")
