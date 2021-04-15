import re
patron='[A-Za-z0-9]'
string='Hola como te va'
print(re.search(patron,string))