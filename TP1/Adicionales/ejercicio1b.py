# -*- coding: utf-8 -*-
def creartxt():
	# Nombre del archivo, y tipo de permisos.
	archi=open('adicional1b.txt', 'w')
	# Cerramos el archivo
	archi.close()

def grabartxt():
	# Abrimos el archivo:
	archi=open('adicional1b.txt','a')
	archi.write('Pedro, 23 años, estudiante, dirección: 53 y 12\n')
	archi.write('Juana, 25 años, nacida en  Bolívar, teléfono: 4235999\n')
	archi.close()
	
creartxt()
grabartxt()
