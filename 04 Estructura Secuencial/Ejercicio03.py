equi = input("Ingrese nombre de equipo: ")

pg = int(input("Cuantos Partidos gano? "))
pe = int(input("Cuantos Partidos empato? "))
pp = int(input("Cuantos Partidos perdio? "))

suma = pg + pe + pp

puntos = pg*3 + pe

print("El Club", equi, "sumo la cantidad de", puntos, "en", suma, "fechas.")