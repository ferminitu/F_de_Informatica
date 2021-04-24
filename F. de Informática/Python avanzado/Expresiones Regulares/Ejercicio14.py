import re 
texto = "Python_programming:\na high-level general-purpose programming language\t."
patron = "[\s]"
print(texto)
print(re.sub(patron, ";", texto))