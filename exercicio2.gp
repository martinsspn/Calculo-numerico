set xrange[-6:6]
set xzeroaxis ls -1
set yzeroaxis ls -1
set grid
plot "arquivo.pts" with lp, x*cos(x) + 1
