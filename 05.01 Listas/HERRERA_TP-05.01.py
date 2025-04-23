# EJERCICIO 1

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

# EJERCICIO 2

del_1_al_5 = [1, 2, 3, 4, 5]
print(del_1_al_5[3])


# EJERCICIO 3

lista_vacia = []

lista_vacia.append("Franco")
lista_vacia.append("Leonel")
lista_vacia.append("Herrera")

print(lista_vacia)


# EJERCICIO 4

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)


# EJERCICIO 5

"""
Elimina el valor mas grande de la lista y luego la muestra por pantalla.
En este caso, la lista resultante seria: [8, 15, 3, 7]
"""


# EJERCICIO 6

numeros = list(range(10, 31, 5))
print(numeros[0:2])


# EJERCICIO 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "ferrari"
autos[2] = "BMW"

print(autos)


# EJERCICIO 8

dobles = []

for n in range(5, 16, 5):
    dobles.append(n * 2)

print(dobles)


# EJERCICIO 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# A
compras[2].append("jugo")

# B
compras[1][1] = "tallarines"

#C
compras[0].remove("pan")

#D
print(compras)


# EJERCICIO 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)