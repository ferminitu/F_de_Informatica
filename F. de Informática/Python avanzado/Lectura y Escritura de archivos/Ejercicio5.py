import re

with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt') as f:
    f = f.read()
    f = re.sub("p", "p\n", f)
    with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/texto_a.txt', "w") as f1: 
        for line in f:
            f1.write(line)