set xrange [-5: 5]
set grid
set xzeroaxis ls -1
set yzeroaxis ls -1
plot ((64*(x*2))/((x**2) - (2(8*x/(((400-(x*2))(1/2))))+ (64(x*2)/(400-(x**2))))) - 900 + (x*2)
