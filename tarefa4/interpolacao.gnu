set xrange[-1:8];
set yrange[-2:5];
set grid;
plot  ((89*x**3 - 849*x**2 + 1762*x + 420)/420) title "Interpolação polinomial de Newton", ((89*x**3 - 849*x**2 + 1762*x + 420)/420) title "interpolação polinomial de Lagrange", 1+x title "parte 1 int. linear"  , 7 - 2*x title "part 2 int. linear", (5*(x-4)/3)-1 title "parte 3 int. linear" , "pontos.pts" title "Pontos"
