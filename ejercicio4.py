import json
from pprint import pprint
with open('playastenerife.json') as datos:
	data=json.load(datos)


nombre=raw_input("Dime el nombre de una playa: ")

for i in data["listado"]:
        if i["ows_LinkTitle"] == nombre:
		zona=i["ows_Zona"]
		direccion=i["ows_Direccion"]
		color=i["ows_ColorArena"] 
		oleaje=i["ows_TipoOleaje"]
		print "La playa por la que preguntas se encuentra en la zona",zona,"de Tenerife, en la direccion",direccion,",tiene la arena de color",color,"y su oleaje es",oleaje
