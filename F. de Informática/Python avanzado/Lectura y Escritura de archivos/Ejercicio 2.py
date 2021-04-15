import re

texto = open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt')

n = 0

while n <= 5:
    n +=1
    print(texto.readline())