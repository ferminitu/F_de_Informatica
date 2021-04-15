#6) Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre
#cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

min_ing = int(input("Ingrese x cantidad de minutos: "))


h_dec = min_ing / 60
horas = int(h_dec)
minutos = int((h_dec - horas) * 60)

print(str(min_ing) + " minutos son " + str(horas) + " horas y " + str(minutos) + " minutos.")