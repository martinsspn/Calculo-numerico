set xrange [-5: 5]
set grid
set xzeroaxis ls -1
set yzeroaxis ls -1
plot 300 - ((0.25*32.17)/0.1)*x + (((0.25**2)*32.17)/0.1**2)*(1 - 2.71828182846**((-0.1*x)/0.25)), "ptsQ3.pts"
