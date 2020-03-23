set xrange[-6:6]
set yrange[-6:6]
plot 1 + x -(3*x**3)/6 + (5*x**5)/120 -(7*x**7)/5040 + (9*x**9)/362880 title "f(x) = 1 + x -3x³/3! + 5x⁵/5! - 7x⁷/7! + 9x⁹/9!", x*cos(x) + 1 title "f(x) = xcos(x) + 1"
