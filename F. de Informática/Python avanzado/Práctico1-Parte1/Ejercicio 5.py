#5) Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
print("Ingresa tres numeros")
n1=int(input())
n2=int(input())
n3=int(input())
promedio = (n1+n2+n3)/3
print(float('{:.2f}'.format(promedio)))