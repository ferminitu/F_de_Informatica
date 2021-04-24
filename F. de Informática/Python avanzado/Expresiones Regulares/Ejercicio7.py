import re 
string = input("Ingrese un texto:")
def letras_espacios_numeros(string):
    return not bool(re.search('[^(a-zA-Z0-9\s)]',string))
if letras_espacios_numeros(string):
    print("Este string contiene solo letras minusculas, mayusculas, espacios o numeros")
else:
    print("Este string no contiene solo letras minusculas, mayusculas, espacios o numeros")