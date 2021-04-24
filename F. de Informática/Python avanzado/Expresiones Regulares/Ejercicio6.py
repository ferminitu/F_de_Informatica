import re
lista_strings = ["martes", "película", "Kubrik","buena"]
frase = "El otro día vi una película de Nolan y estuvo muy buena"

for i in lista_strings:
    patron = i
    if re.search(patron, frase) is not None:
        print("La palabra",r"'",i,r"'","se encuentra en la frase dada")
    else:
        print("La palabra",r"'",i,r"'" ,"no se encuentra en la frase dada")