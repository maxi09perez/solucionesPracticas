alumnos = int(input("Ingrese cantidad de alumnos: "))
suma = 0
cont = 1
while cont <= alumnos:
    nota = int(input("Ingrese nota del alumno " + str(cont)+": "))
    if nota >= 0 and nota <= 10:
        suma += nota
        cont += 1

promedio = suma / alumnos

if promedio > 8:
    print("El promedio es elevado con:", promedio)
elif promedio >= 6:
    print("El promedio es aceptable con:", promedio)
else:
    print("El promedio es bajo con:", promedio)