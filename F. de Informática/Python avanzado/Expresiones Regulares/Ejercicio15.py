import re
mail = "ferminiturriaga@icloud.com"
patron = "(\W|^)[^(()<>@,;:%]*(@)((yahoo|hotmail|gmail).com)(\W|$)"
if re.search(patron, mail) is not None:
    print("Su mail es valido")
else:
    print("Su mail es invalido")