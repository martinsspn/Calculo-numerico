set xzeroaxis
set yzeroaxis
set yrange [-4:5.5]
set xrange [-4:5.5]
plot x**3 - 1.7*x*x - 12.78*x - 10.08 title "função", "ptsNewtonRaphson.pts" title "aprox. Newton-Raphson", "ptsSecante.pts" title "aprox. Secante" ls 7, "ptsRegulaFalsi.pts" title "aprox. Regula Falsi" ls 8
