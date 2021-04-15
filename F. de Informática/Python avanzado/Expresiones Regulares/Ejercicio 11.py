import re

def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())

lista = ["Practica Python", "Practica C++", "Practica Fortran"]
dos_P(lista)