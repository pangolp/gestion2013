# -*- coding: utf-8 -*-
def creartxt():
	# Nombre del archivo, y tipo de permisos.
	archi=open('adicional1a.txt', 'w')
	# Cerramos el archivo
	archi.close()

def grabartxt():
	# Abrimos el archivo:
	archi=open('adicional1a.txt','a')
	archi.write('La Plata: Pedro Sanchez 23 años, Juan Tevez 23 años, Mario Scala 23 años\n')
	archi.write('Berisso: Marina Lopez 25 años, Maria Gimenez 20 años, Jose Trano 30 años\n')
	archi.write('Ensenada: Ariel Mango 18 años, Ulises Prio 28 años, Marta Perez 60 años\n')
	archi.close()
	
creartxt()
grabartxt()
