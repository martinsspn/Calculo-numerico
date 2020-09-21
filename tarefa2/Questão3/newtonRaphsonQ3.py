def newthonRaphson(t):
    while True:
        t = t - (s(t)/sd(t))
        if s(t) <= 0.000001 and s(t) >= -0.000001:
            return t

def s(t):
    return 300 - ((0.25*32.17)/0.1)*t + (((0.25**2)*32.17)/0.1**2)*(1 - 2.71828182846**((-0.1*t)/0.25))

def sd(t):
    return -80.425 + 80.425*2.71828182846**(-0.1*t/0.25)

print (newthonRaphson(1))
