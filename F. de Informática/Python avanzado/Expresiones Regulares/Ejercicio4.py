import re 
string = "La contraseña es abc_123"
patron = "(\w*)_(\w*)"
print(re.search(patron, string).group(0))
