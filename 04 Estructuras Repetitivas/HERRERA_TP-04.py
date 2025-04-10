import random

# TRABAJO PRACTICO 4: Estructuras Repetitivas

# EJERCICIO 1

for x in range(101):
    print(x)

# EJERCICIO 2

num_ingresado = input("Ingrese un numero entero: ")
i = 0
contador = 0

while i < len(num_ingresado):
    contador+= 1
    i+= 1

print(f"Cantidad de digitos: {contador}")

# EJERCICIO 3

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = 0

for i in range(num1 + 1, num2):
    suma+= i

print(f"Suma de los numeros en el rango dado: {suma}")


# EJERCICIO 4

num_ingresado = int(input("Ingrese un numero entero: "))
suma = 0

while num_ingresado != 0:

    suma += num_ingresado
    num_ingresado = int(input("Ingrese numero entero a sumar o cero para terminar: "))

print(f"La suma de los numeros ingresados es: {suma}")


# EJERCICIO 5

num_aleatorio = random.randint(0, 9)
num_ingresado = int(input("Adivine el numero entero secreto: "))
cant_intentos = 1

while num_aleatorio != num_ingresado:
    cant_intentos += 1
    num_ingresado = int(input("Error! Ingrese otro numero: "))

print(f"Correcto! Cantidad de intentos: {cant_intentos}")


# EJERCICIO 6

for x in range(98, 0, -2): # SE EXCLUYE EL 100 PORQUE EL ENUNCIADO DICE COMPRENDIDOS ENTRE, POR LO QUE ENTIENDO QUE NO SE DEBEN INCLUIR EL 0 NI EL 100
    print(x)


# EJERCICIO 7

num_ingresado = int(input("Ingrese un numero entero positivo: "))
suma = 0

for x in range(0, num_ingresado): # AL IGUAL QUE EN EL EJERCICIO ANTERIOR NO QUEDA CLARO SI DEBE INCLUIRSE EL NUMERO INGRESADO POR EL USUARIO. SE DECIDE EXCLUIRLO.
    suma += x

print(f"La suma de todos los numeros comprendidos entre 0 y {num_ingresado} es: {suma}")


# EJERCICIO 8

cant_num_ingresados = 0
cant_pares          = 0
cant_impares        = 0
cant_positivos      = 0
cant_negativos      = 0

while cant_num_ingresados < 100:

    num_ingresado = int(input("Ingrese un numero entero: "))
    cant_num_ingresados += 1

    if num_ingresado % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1

    if num_ingresado >= 0:
        cant_positivos += 1
    else:
        cant_negativos += 1

print(f"Cantidad de números pares: {cant_pares}")
print(f"Cantidad de números impares: {cant_impares}")
print(f"Cantidad de números positivos: {cant_positivos}")
print(f"Cantidad de números negativos: {cant_negativos}")


# EJERCICIO 9

cant_num_ingresados = 0
suma_num_ingresados = 0

while cant_num_ingresados < 5:

    num_ingresado = int(input("Ingrese un numero entero: ")) # PIDO UN NUMERO ENTERO
    suma_num_ingresados += num_ingresado                     # SUMO EL NUMERO ENTERO INGRESADO
    cant_num_ingresados += 1                                 # SUMO 1 A LA CANTIDAD DE NUMEROS INGRESADOS

print(f"La media de los numeros ingresados es: {suma_num_ingresados / 5}")


# EJERCICIO 10

num_ingresado = input("Ingrese un numero: ")
num_invertido = ""

for x in range(len(num_ingresado)-1, -1, -1):
    
    num_invertido += num_ingresado[x]

print(num_invertido)