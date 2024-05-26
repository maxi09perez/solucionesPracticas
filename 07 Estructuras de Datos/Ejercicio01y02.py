#Ejercicio 1

lista = []

for i in range(10):
    nombre = input("Ingrese nombre "+str(i+1)+": ")
    lista.append(nombre)

print(lista)

#Ejercicio 2

lista.pop(2)
lista.pop()
lista.sort()

print(lista)