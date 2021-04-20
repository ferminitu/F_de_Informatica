import re

texto = open('/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt','r')

text = texto.read()
palabras = text.split()
print(len(palabras))

lista_palabras_unicas = []
for i in palabras:
    if i not in lista_palabras_unicas:
        lista_palabras_unicas.append(i)

print(lista_palabras_unicas)
    

for i in lista_palabras_unicas:
    print(re.findall(i, text))
    repeticiones =len(re.findall(i, text))
    frecuencia = float('{:.4f}'.format(repeticiones / len(palabras)))
    print("La frecuencia de " + "'" +str(i) +"'"+ " es: " + str(frecuencia))