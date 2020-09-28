from copy import deepcopy
import numpy as np

def elimGauss(A, B, n):
    A1 = deepcopy(A)
    B1 = deepcopy(B)
    for k in range(n):
        for i in range(k+1, n):
            m = A1[i][k]/A1[k][k]
            A1[i][k] = 0
            for j in range(k+1, n):
                A1[i][j] = A1[i][j] - m*A1[k][j]
            B1[i]  = B1[i] - m*B1[k]
    return A1, B1

def elimGaussPiv(A, B, n):
    A1 = deepcopy(A)
    B1 = deepcopy(B)
    for k in range(n):
        #pivoteamento:
        pivo = A1[k][k]
        l_pivo = k
        for i in range(k+1, n):
            if abs(A1[i][k]) > pivo:
                pivo = A1[i][k]
                l_pivo = i
        if pivo == 0:
            break
        if l_pivo != k:
            for j in range(n):
                troca = A1[k][j]
                A1[k][j] = A1[l_pivo][j]
                A1[l_pivo][j] = troca
            troca = B1[k]
            B1[k] = B1[l_pivo]
            B1[l_pivo] = troca
        #Eliminacao
        for i in range(k+1, n):
            m = A1[i][k] / A1[k][k]
            A1[i][k] = 0
            for j in range(k+1, n):
                A1[i][j] = A1[i][j] - m*A1[k][j]
            B1[i] = B1[i] - m*B1[k]
    return A1, B1

def resolutionElim(A, B, n):
    X = [0.0]*n
    X[n-1] = B[n-1]/A[n-1][n-1]
    for i in range(n-1, 0, -1):
        soma = 0.0
        for j in range(i+1, n):
            soma = soma + A[i][j]*X[j]
        X[i] = (B[i] - soma)/A[i][i]
    return X


def vetResiduo(A, B, X, n):
    r = [0.0]*n
    AX = [0.0]*n
    for i in range(n):
        soma = 0.0
        for j in range(n):
            soma += A[i][j]*X[j]
        AX[i] = soma
    for i in range(n):
        r[i] = B[i] - AX[i]
    return r

def refinamento(A, B, n):
    op = int(input("Digite o número de iterações a ser realizadas para o refinamento: "))
    while True:
        op1 = int(input("Digite 1 para realizar sem pivotamento e 2 para realizar com pivotamento: "))
        if op1 == 1:
            Arf, Brf = elimGauss(A, B, n)
            Xref = resolutionElim(Arf, Brf, n)
            Ar, Br = elimGauss(A, vetResiduo(A, B, Xref, n), n)
            Y = resolutionElim(Ar, Br, n)
            for i in range(op-1):
                Ar, Br = elimGauss(A, vetResiduo(A, B, Y, n), n)
                Y = resolutionElim(Ar, Br, n)
            break
        elif op1 == 2:
            Arf, Brf = elimGauss(A, B, n)
            Xref = resolutionElim(Arf, Brf, n)
            Ar, Br = elimGaussPiv(A, vetResiduo(A, B, Xref, n), n)
            Y = resolutionElim(Ar, Br, n)
            for i in range(op-1):
                Ar, Br = elimGaussPiv(A, vetResiduo(A, B, Y, n), n)
                Y = resolutionElim(Ar, Br, n)
            break
        else:
            print("comando inválido!")
    ref = [0.0]*n
    for i in range(n):
        ref[i] = Y[i] + Xref[i]
    print("Refinamento X: ")
    return ref

arquivo = input("digite o nome do arquivo de teste com a extencao: ")
arq = open(arquivo, "r")
n = arq.readline()
n = int(n[:-1])
A = [0.0]*n
B = [0.0]*n
for i in range(n):
    A[i] = [0.0]*n    
    l = arq.readline()
    linha = l.split(" ")
    if linha[-1] == "\n":
        linha.remove(linha[-1])
    for j in range(len(linha)):
        if linha[j] == linha[-1]:
            B[i] = float(linha[j])
        else:
            A[i][j] = float(linha[j])


#MENUU
while True:
    x = int(input("MENU\n1 - Realizar eliminação de Gauss sem pivotamento parcial\n2 - Realizar eliminação de Gauss com pivotamento parcial\n3 - realizar refinamento\nDigite sua opção: "))
    if x == 1:
        As, Bs = elimGauss(A, B, n)
        print(As)
        print(Bs)
        print("Resolução sem pivotamento parcial: ")
        print("A = ", As)
        print("B =  ", Bs)
        print("Resolução do sistema linear (X) =  ", resolutionElim(As, Bs, n))
        print("Vetor resíduo sem pivotamento parcial: ", vetResiduo(A, B, resolutionElim(As, Bs, n), n)) 
        break
    elif x == 2:
        Apiv, Bpiv = elimGaussPiv(A, B, n)
        print("Resolução com pivotamento parcial: ")
        print("A = ", Apiv)
        print("B = ", Bpiv)
        print("Resolução do sistema linear (X) = ", resolutionElim(Apiv, Bpiv, n))
        print("Vetor residuo com pivotamento partical: ", vetResiduo(A, B, resolutionElim(Apiv, Bpiv, n), n))
        break
    elif x == 3:
        fim = refinamento(A, B, n)
        print(fim)
        print("Norma do refinamento: " + str(np.linalg.norm(fim)))
        break
