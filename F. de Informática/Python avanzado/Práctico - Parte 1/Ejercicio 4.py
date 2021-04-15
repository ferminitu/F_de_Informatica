#4) Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
print("Escribi tu nombre y tus dos apellidos ")
n=input("Escribi tu nombre: ")
ap=input("Escribi tu apellido: ")
ap1=input("Escribi tu 2do apellido: ")
print(n[0].upper()+n[1:] +" "+ ap[0].upper()+ap[1:] +" "+ ap1[0].upper()+ap1[1:])