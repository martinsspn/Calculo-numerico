set xrange [-25: 25]
set grid
set xzeroaxis ls -1
set yzeroaxis ls -1
plot x**2 + 25600/(((240/sqrt(900 - x**2)*x)/30) - x)**2 - 20**2, "ptsSecante.pts"
