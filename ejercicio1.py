import json
from pprint import pprint
with open('playastenerife.json') as datos:
	data=json.load(datos)

zona=raw_input("Dime una zona: ")

for i in data["listado"]:
	if i["ows_Zona"] == zona:
		print i["ows_LinkTitle"]
