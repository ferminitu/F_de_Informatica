with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/frase_a.txt') as f:
    with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/frases.txt', "w") as f1:
        for line in f:
            f1.write(line)

 
with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/frase_b.txt') as f2:
        with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/frases.txt', "a") as f1:
            f1.write("\n\n")
            for line in f2:
                f1.write(line)