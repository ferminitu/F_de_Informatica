# Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa 
# y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la 
# tabla:

# Zona	Ubicación	Costo/kg
# 1	América del Sur	10.00 dólares
# 2	América Central	15.00 dólares
# 3	América del Norte	18.00 dólares
# 4	Europa	24.00 dólares
# 5	Asia	30.00 dólares

# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística 
# y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega



gramos = int(input("Ingrese el peso en gramos:"))
if gramos < 5000:
    zona = int(input("ingrese la zona:\n1 América del Sur\n2 América Central\n3 América del Norte\n4 Europa\n5 Asia\n"))
    if zona == 1:
        print("$" + str(10 * (gramos/1000)))
    elif zona == 2:
        print("$" + str(15 * (gramos/1000)))
    elif zona == 3:
        print("$" + str(18 * (gramos/1000)))
    elif zona == 4:
        print("$" + str(24 * (gramos/1000)))
    elif zona == 5:
        print("$" + str(30 * (gramos/1000)))
else:
    print("Su paquete fue rechazado")