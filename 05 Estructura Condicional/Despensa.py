leche = int(input("Cuantas Leches lleva el cliente? "))

esJubilado = input("El cliente es Jubilado? (Si/No) ")

if esJubilado.upper() == "SI":
    jubilado = True
else:
    jubilado = False

if jubilado:
    if leche > 12 and leche <= 24:
        total = leche * 1000 * 0.8
    elif leche > 24:
        total = leche * 1000 * 0.75
    else:
        total = leche * 1000 * 0.9
else:
    if leche > 12 and leche <= 24:
        total = leche * 1000 * 0.9
    elif leche > 24:
        total = leche * 1000 * 0.85
    else:
        total = leche * 1000

print("El Total a pagar es: ", total)