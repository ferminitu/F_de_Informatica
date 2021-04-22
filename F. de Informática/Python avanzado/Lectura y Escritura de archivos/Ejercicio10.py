import glob
import os

os.chdir(r"/Users/ferminiturriaga/Desktop/UCEMA/2021/F. de Informática/Repositorio_Informatica/Practicas/Practica 4")
print(os.getcwd())
files_list = glob.glob("*.txt")
print(files_list)

with open(r"Nuevo.txt", "a") as f:
    for file in files_list:
        with open(file, "r") as g:
            f.write(g.read())