#7) Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión 
# por cada venta que realiza. Realizar un programa que devuelva el dinero
# que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes,
# teniendo en cuenta estas ventas y su sueldo base.


def sueldo_final(sueldo_base, ventas):
    comisiones = int((sueldo_base * 0.10) * ventas)
    sueldo = int(sueldo_base + comisiones)
    print("Comisión obtenidas: $" + str(comisiones) + "\nSueldo Final: $" + str(int(sueldo)))

sueldo_final(50000, 5)