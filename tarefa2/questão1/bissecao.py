def bissecao(a, b, TOL):
    i = 1 
    N = 500
    fa = a**3 - 1.7*a**2 - 12.27*a - 10.08
    while (i <= N):
        p = a + (b-a)/2
        fp = p**3 - 1.7*p**2 - 12.27*p - 10.08
        if((fp == 0) or ((b-a)/2 < TOL)):
            return p;
        i = i+1
        if(fa*fp>0):
            a = p
            fa = fp
        else:
            b = p

arq = open("ptsBissecao.pts", "w")
erro = 0.000000005
arq.write(str(bissecao(-2.2, -2, erro)) + " " + "0\n")
arq.write(str(bissecao(-1.10, -0.9, erro)) + " " + "0\n")
arq.write(str(bissecao(4.65, 4.90, erro)) + " " + "0\n")
