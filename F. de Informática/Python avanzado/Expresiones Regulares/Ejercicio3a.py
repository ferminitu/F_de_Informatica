import re

def encontrar_patron(string):
    patron = 'he*'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

print(encontrar_patron('a'))
print(encontrar_patron('h'))
print(encontrar_patron('he'))
print(encontrar_patron('heeeeee'))