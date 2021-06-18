# Ejercicio 1
# Dadas las clases 'Perro' y 'Gato', responder:

# a) cuales son sus estados

# b) cuales son sus interfaces

# c) ¿Comparten interfaz?

# d) ¿Son polimórficas?

# a) Estado de Perro: [alimento, caricias]
#    Estado de Gato: [alimento, caricias]

# b) Interfaz Perro: [energia, comer, alimento, acariciar, estaDebil, pasear]
#    Interfaz Gato: [energia, comer, caricias, acariciar, estaDebil]

# c) Comparten su interfaz, pero no completamente. Hay algunos mensajes (metodos) que ambos entienden, pero otros que no.

# d) Polimorficas: 
#    Primer requisito, compartir interfaz [Cumplido]
#    Segundo requisito, clase externa que interactue con estas clases a traves de la interfaz que comparten [NO cumplen]
#    Por lo tanto, estas clases NO son polimorficas.