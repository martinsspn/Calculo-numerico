set style fill pattern 4
set terminal png
set samples 1000
set xrange[-5.000000:5.000000]
set yrange[-15:15]
set output "trapezioComposta.png"
plot x >= -5.000000 && x <= 5.000000 ?  (1.66666667/2)*(x*sin(x) + 2*(x+1.66666667)*sin(x+1.66666667) + 2*(x+2*1.66666667)*sin(x+2*1.66666667) + 2*(x+3*1.66666667)*sin(x+3*1.66666667) + 2*(x+4*1.66666667)*sin(x+4*1.66666667) + 2*(x+5*1.66666667)*sin(x+5*1.66666667) + (x+6*1.66666667)*sin(x+6*1.66666667)) : 0/0 with filledcurve y1=0 title 'Regra do Trapezio Composta', 0 lc 0, x*sin(x)
