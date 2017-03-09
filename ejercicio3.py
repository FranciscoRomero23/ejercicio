#-*- coding:utf-8 -*-

import json
from pprint import pprint
with open('playastenerife.json') as datos:
	data=json.load(datos)


zona=raw_input("Dime una zona: ")
color=raw_input("Dime un color: ")
playas=[]
for i in data["listado"]:
        if i["ows_Zona"] == zona and i["ows_ColorArena"] == color:
		playas.append(i["ows_LinkTitle"])

cantidad=len(playas)

if cantidad > 0:
	print "Existen playas que coinciden con tales caracteristicas:"
	for num in xrange(1,cantidad):
		print "-",playas[num]
