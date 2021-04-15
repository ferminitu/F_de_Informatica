# Desafio III: Desafío III: Probá las lineas anteriores y anotate
# para qué sirve cada uno de los métodos y funciones.
saludo = "Hola mundo"
len(saludo)
saludo.upper()
saludo.lower()
saludo.count('o')
saludo.replace('o','a')

print(saludo)
print(len(saludo))
print(saludo.upper())
print(saludo.lower())
print(saludo.count('o'))
print(saludo.replace('o','a'))

# Desafio IV: Vimos que el método replace nos permite reemplazar un caracter por otro de un string dado,
# ¿pero nos dejará reemplazar un segemento más largo? Probá hacer saludo.replace("mundo", "terricolas")
print(saludo.replace('mundo','terricolas'))

# Desafio VI: Construí una función que nos permita calcular cuántos termos de 1000ml
# llenos consumiremos para un ronda dada (es decir una cantidad de personas dada).
def mate(personas):
    return int(1000/((personas)*30))
print(mate(10))

# Desafio VII: Hacer una def _vaquita_ que nos permita dividir
# los costos de una docena de facturas entre cierta cantidad de comensales
def vaquita(costos, comensales):
    return costos / comensales

print(vaquita(200,4))
