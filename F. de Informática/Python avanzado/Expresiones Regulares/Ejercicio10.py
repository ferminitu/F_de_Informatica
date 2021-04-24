import re
string = "Hola soy &Fermin& y tengo @19@ años"
patron = "[@&](.*?)[@&]"
lista = re.findall(patron, string)
print(lista)

for i in lista:
    print(str(i) + str(re.search(i, string).span()))