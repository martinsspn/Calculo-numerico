set terminal png
set output "relacao.png"
plot -60.066083327 + 70.3336844377*x, "pesos.txt"
