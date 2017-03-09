#-*- coding:utf-8 -*-

import json
from pprint import pprint
with open('playastenerife.json') as datos:
	data=json.load(datos)

print "Playas con descripcción en Español, Ingles y Aleman:"
print "----------------------------------------------------"
for i in data["listado"]:
	espanol=i["ows_DescripcionEspanol"] != ""
	ingles=i["ows_DescripcionIngles"] != ""
	aleman=i["ows_DescripcionAleman"] != ""
        if espanol and ingles and aleman:
		nombre=i["ows_LinkTitle"]
		print nombre
