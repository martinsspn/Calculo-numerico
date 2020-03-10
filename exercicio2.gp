set xrange[-6:6]
set xzeroaxis ls -1
set yzeroaxis ls -1
set grid
plot "pontos positivos.pts" with lp lc 3, "pontos negativos.pts" with lp lc 18, x*cos(x) + 1 lc 7
