import json
from pprint import pprint
with open('playastenerife.json') as datos:
	data=json.load(datos)

colores=[]
cantcolor=[]

for i in data["listado"]:
	color=i["ows_ColorArena"]
	if color not in colores:
		colores.append(color)
		cantcolor.append(0)

cuenta=len(colores)

for i in data["listado"]:
	color=i["ows_ColorArena"]
	for num in xrange(1,cuenta+1):
		if color == colores[num-1]:
			cantcolor[num-1]=cantcolor[num-1]+1

for num in xrange(1,cuenta+1):
	print colores[num-1],cantcolor[num-1]
