import re

texto1 = open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt')

lineas = texto1.readlines()
contador = 0
print(lineas)

for i in lineas:
    if re.search('^[^M]', i) is not None:
        contador +=1
        
        
print(contador)
