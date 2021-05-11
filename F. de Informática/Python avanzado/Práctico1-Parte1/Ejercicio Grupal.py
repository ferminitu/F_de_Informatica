#Compra de una casa
#Determinar cuánto tiempo (meses) tomaría ahorrar la cantidad suficiente de dinero para pagar el depósito.
#Consideremos que se realiza una inversión con el dinero ahorrado con una ganacia del 4% anual.

#Datos y variables
#costo_total, porcentaje_deposito (25% costo total), cantidad_ahorrada(inicia en 0), sueldo_anual, g(ganacia 4% anual),
#porcentaje_ahorrado(% del sueldo), sueldo_mensual

costo_total = int(input("Ingrese el valor de la propiedad: "))
sueldo_anual = int(input("Ingrese su sueldo anual: "))
porcentajexmes = float(input("Ingrese la porporcion del sueldo que quiere ahorrar por mes: "))


porcentaje_deposito = costo_total / 4
cantidad_ahorrada = 0
tasa_interes = 0.04
tasa_mensual = tasa_interes / 12
sueldo_mensual = sueldo_anual / 12
ahorro_mensual= sueldo_mensual * porcentajexmes

#Formula interes compuesto = Monto Inicial *(1+r)**n periodos


r = 0.04/12
ahorros = 0
mes = 0
while ahorros <= porcentaje_deposito:
    mes += 1
    ahorros += ahorro_mensual 
    ahorros = ahorros * (1 + r)
    

print("\nDeposito: $" + str(int(porcentaje_deposito)))
print("Sueldo mensual: $" +str(int(sueldo_mensual)))
print("Ahorro por mes: $" +str(int(ahorro_mensual)))
print("Tasa mensual: " +str(tasa_mensual))

print("\nAhorros: $" +str(int(ahorros)))
print("Meses: " +str(mes))


print("En " + str(mes) + " meses lograrias ahorrar la suma de: $" + str(int(ahorros)) + ", alcanzando asi el total del deposito")

ganancia = ahorros - (ahorro_mensual*mes)
print("\nObtuviste una ganancia de: $"+str(int(ganancia)))