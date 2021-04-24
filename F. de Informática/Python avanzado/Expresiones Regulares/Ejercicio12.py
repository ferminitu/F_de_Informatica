import re 
texto = "Python_programming_: a high-level general-purpose programming language."
patron = "[-\s_:]"
print(re.sub(patron, "|", texto))