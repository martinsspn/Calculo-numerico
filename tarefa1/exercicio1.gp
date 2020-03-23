set xrange [-1.5:2.5]
set grid
set xzeroaxis ls -1
set yzeroaxis ls -1
plot x**3 - 2*x*x - x + 2 title "funcao cubica", -2*x + 2 title "reta tangente em x = 1", "pontosCriticos.pts" title "pontos criticos", "1f(1).pts" title "1 f(1)", 0*x + -0.631130309441 title "reta tangente ao ponto critico 1", 0*x + 2.11261179092 title "reta tangente ao ponto critico 2"
