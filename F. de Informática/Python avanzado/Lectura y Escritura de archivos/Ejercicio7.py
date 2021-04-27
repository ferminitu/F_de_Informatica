import re

with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt') as file:
    data = file.read().split()
    palabra_max = (max(data,key=len))
    print(palabra_max)
    print(len(palabra_max))    
    
    resultado=[palabra for palabra in data if len(palabra)==len(palabra_max)]
    print(resultado)