set style fill pattern 4
set terminal png
set samples 1000
set xrange[-5.000000:5.000000]
set yrange[-15:15]
set output "Simpson38.png"
plot x>= -5.000000 && x<= 5.000000 ? (3*1.6666667/8)*((x*sin(x))+3*((x+1.6666667)*sin(x+1.6666667))+3*((x+2*(1.6666667))*sin(x+2*(1.6666667)))+((x+3*(1.6666667))*sin(x+3*(1.6666667)))+((x+3*(1.6666667))*sin(x+3*(1.6666667)))+3*((x+4*(1.6666667))*sin(x+4*(1.6666667)))+3*((x+5*(1.6666667))*sin(x+5*(1.6666667)))+4*((x+6*(1.6666667))*sin(x+6*(1.6666667)))): 0/0 with filledcurve y1=0 title 'Regra de Simpson 3/8', 0 lc 0, x*sin(x)
