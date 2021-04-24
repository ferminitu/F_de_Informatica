import re 
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
patron = "-(.*?)-"
a = re.findall(patron, string)

print(a)
for i in a:
    for i in i:
        print(i)