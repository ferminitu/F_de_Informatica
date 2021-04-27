with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/frase_b.txt') as texto:
    text = texto.read()
    palabras = text.split()
    print(len(palabras))

    lista_palabras_unicas = []
    for i in palabras:
        if i not in lista_palabras_unicas:
            lista_palabras_unicas.append(i)

    print(lista_palabras_unicas)
    
    suma = 0
    for i in lista_palabras_unicas:
        repeticiones =len(re.findall(i, text))
        frecuencia = float('{:.4f}'.format(repeticiones / len(palabras)))
        print("La frecuencia de " + "'" +str(i) +"'"+ " es: " + str(frecuencia)) 
        
        suma += frecuencia

print(suma)