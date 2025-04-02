import random
from statistics import mode, median, mean

# EJERCICIO 1
# NOTA: El enunciado indica que la condicion es que el usuario sea mayor de 18 años, por lo que si se ingresa 18, no se va a considerar como mayor de edad

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")


# EJERCICIO 2

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# EJERCICIO 3

num_a_ingresar = int(input("Ingrese solo un numero par: "))

if num_a_ingresar % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


# EJERCICIO 4

edad2 = int(input("Ingrese su edad: "))

if edad2 < 12:
    print("Niño/a")
elif edad2 >= 12 and edad2 < 18:
    print("Adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Adulto/a joven")
elif edad2 >= 30:
    print("Adulto/a")


# EJERCICIO 5

contrasenia = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
long_contrasenia = len(contrasenia)

if long_contrasenia >= 8 and long_contrasenia <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# EJERCICIO 6

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")                 # MEDIA MAYOR QUE MEDIANA Y MEDIANA MAYOR QUE MODA
elif media < mediana and mediana < moda:
    print("Sesgo negativo")                 # MEDIA MENOR QUE MEDIANA Y MEDIANA MENOR QUE MODA
elif media == mediana and mediana == moda:
    print("Sin sesgo")                      # MEDIA IGUAL QUE MEDIANA Y MEDIANA IGUAL QUE MODA


# EJERCICIO 7

frase_ingresada = input("Ingrese una frase: ")

posicion_ultimo_caracter = len(frase_ingresada) - 1
ultimo_caracter = frase_ingresada[posicion_ultimo_caracter].lower() # OBTENGO EL ULTIMO CARACTER DE LA FRASE Y LO CONVIERTO A MINSUCULA

if ultimo_caracter == 'a' or ultimo_caracter == 'e' or ultimo_caracter == 'i' or ultimo_caracter == 'o' or ultimo_caracter == 'u':
    print(frase_ingresada + "!")
else:
    print(frase_ingresada)


# EJERCICIO 8

nombre = input("Ingrese su nombre: ")
print("1. Su nombre a mayusculas")
print("2. Su nombre a minusculas")
print("3. Su nombre solo con la primera letra mayuscula")
opcion_ingresada = input("Ingrese la opcion que desee: ")

if opcion_ingresada == "1":
    print(nombre.upper())
elif opcion_ingresada == "2":
    print(nombre.lower())
elif opcion_ingresada == "3":
    print(nombre.title())
else:
    print("La opcion ingresada es incorrecta")


# EJERCICIO 9

magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy fuerte")
elif magnitud_terremoto >= 7:
    print("Extremo")


# EJERCICIO 10

hemisferio = input("Ingrese en cual hemisferio se encuentra (N/S): ")
mes = input("Ingrese mes: ").lower()
dia = int(input("Ingrese dia: "))

if hemisferio.upper() == "S":

    if (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20)       or (mes == "febrero") or (mes == "enero"):     # VERANO
        print("El usuario se encuentra en verano")

    elif (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20)         or (mes == "abril")   or (mes == "mayo"):      # OTOÑO
        print("El usuario se encuentra en otoño")

    elif (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20)    or (mes == "julio")   or (mes == "agosto"):    # INVIERNO
        print("El usuario se encuentra en invierno")

    elif (mes == "septiembre" and dia >=21) or (mes == "diciembre" and dia <= 20) or (mes == "octubre") or (mes == "noviembre"): # PRIMAVERA
        print("El usuario se encuentra en primavera")

else:

    if (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20)       or (mes == "febrero") or (mes == "enero"):     # INVIERNO
        print("El usuario se encuentra en invierno")

    elif (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20)         or (mes == "abril")   or (mes == "mayo"):      # PRIMAVERA
        print("El usuario se encuentra en primavera")

    elif (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20)    or (mes == "julio")   or (mes == "agosto"):    # VERANO
        print("El usuario se encuentra en verano")
        
    elif (mes == "septiembre" and dia >=21) or (mes == "diciembre" and dia <= 20) or (mes == "octubre") or (mes == "noviembre"): # OTOÑO
        print("El usuario se encuentra en otoño")