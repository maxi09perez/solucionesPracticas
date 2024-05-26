ancho = float(input("Ingrese el ancho de la pared (en metros): "))
alto = float(input("Ingrese el alto de la pared (en metros): "))
precio_por_metro_cuadrado = float(input("Ingrese el precio por metro cuadrado: "))

area_de_la_pared = ancho * alto

costo_de_mano_de_obra = area_de_la_pared * precio_por_metro_cuadrado

print("El costo de la mano de obra para pintar la pared es: ", costo_de_mano_de_obra)