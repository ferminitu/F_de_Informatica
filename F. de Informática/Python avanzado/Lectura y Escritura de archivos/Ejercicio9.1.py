import re
with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/frase_a.txt', "r") as texto:

    text = texto.read()
    palabras = text.split()
    print(palabras)
    lista = []
    print(len(text.split()))

for i in palabras:
    repeticiones = palabras.count(i)
    lista.append((repeticiones) / len(palabras))
    print(i)
    
for frecuencias in lista:
    print(frecuencias)
print("--------------------------------------")