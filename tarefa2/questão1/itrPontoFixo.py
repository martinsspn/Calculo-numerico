def itrPontoFixo(x, a):
    for i in range(100):
        x = x-a*(x**3 - 1.7*x*x - 12.78*x - 10.08)
    return x
arq = open("ptsItrPontoFixo.pts", "w")
arq.write(str(itrPontoFixo(-2.50, 0.005)) + " 0\n")
arq.write(str(itrPontoFixo(-1, 0.0005)) + " 0\n")
arq.write(str(itrPontoFixo(-0.7, 0.005)) + " 0\n")
arq.close()
