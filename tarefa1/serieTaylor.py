import math
x = 0
for k in range(10):
    if k%2 != 0:
        y = (-1)**((k-1)/2) * k* math.cos(x) + (-1)**((k+1)/2) * x * math.sin(x)
    else:
        y = (-1)**(k/2) * k * math.sin(x) + (-1)**(k/2) * x * math.cos(x)
    print y
