import re
with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt') as texto:
    lista = []
    for i in texto:
     lista.append(i)

print(lista[-5:])
for i in lista[-5:]:
    print(i)



