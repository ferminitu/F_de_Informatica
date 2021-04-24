import re
string = input("Ingrese un texto:")

lista = re.findall("\d", string)
for i in lista:
    print(int(i))