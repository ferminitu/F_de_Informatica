import re

texto = open('/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt','r')

text = texto.read()
palabras = text.split()

print('La cantidad de palabras en el texto son: ', len(palabras))