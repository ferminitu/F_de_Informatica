#Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada 
# alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar 
# se deben mostrar los siguientes datos:

# La edad máxima de todos los alumnos.
# Los alumnos que tengan la edad máxima


# Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
#  distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores
#   serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre
#    y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media 
#    obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.

alumnos = []
dic={}
nombres=[]
n = 0

while 1:
    cant=int(input("Introduce la cantidad de alumnos a ingresar: "))
    while n<cant:
        n+=1
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre not in nombres:
            nombres.append(nombre)

            nota = int(input("Ingrese la nota: "))
            if nota>0:
                dic[nombre]=[nota]

                nota = int(input("Ingrese la nota: "))
                if nota >0:
                    dic[nombre].append(nota)
                    while nota>0:
                        nota = int(input("Ingrese la nota: "))
                        if nota>0:
                            dic[nombre].append(nota)                
                alumnos.append(dic)
                dic={}
                
        else:
            print("Error alumno ya existente")
    n=0


    for alumno in alumnos:
        for key in alumno.keys():
            print("El promedio de " + str(key) + " es: " + str(float('{:.2f}'.format((sum(alumno[key]) / len(alumno[key]))))) )