import glob
import os

os.chdir(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos')
print(os.getcwd())
files_list = glob.glob("*.txt")
print(files_list)

with open(r'/Users/ferminiturriaga/Desktop/UCEMA/2021/F_de_Informatica/F. de Informática/Python avanzado/Lectura y Escritura de archivos/Nuevo.txt', "a") as f:
    for file in files_list:
        with open(file, "r") as g:
            f.write(g.read())
            f.write("\n")