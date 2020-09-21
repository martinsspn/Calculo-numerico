set xzeroaxis
set yzeroaxis
set yrange [-4:5.5]
set xrange [-4:5.5]
plot x**3 - 1.7*x*x - 12.78*x - 10.08 title "função", "ptsBissecao.pts" title "aprox. Bissecao", "ptsItrPontoFixo.pts" title "aprox. Itr Ponto Fixo" ls 7
