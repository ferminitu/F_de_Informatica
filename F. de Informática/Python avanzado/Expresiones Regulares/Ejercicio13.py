import re 
texto = "Python_programming: a high-level general-purpose programming language."
patron = "\W"

lista = re.findall(patron, texto)
primero = lista[0]
segundo = lista[1]

texto2= re.sub(":{1,2}", "_", texto)
print(re.sub(segundo, "_", texto2))