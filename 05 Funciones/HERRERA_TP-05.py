import math

# EJERCICIO 1

def hola_mundo():
    print("Hola Mundo!")


# EJERCICIO 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


# EJERCICIO 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# EJERCICIO 4

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# EJERCICIO 5

def segundos_a_horas(segundos):
    return minutos_a_horas(segundos/60)

def minutos_a_horas(minutos):
    return minutos/60


# EJERCICIO 6

def tabla_multiplicar(numero):
    for n in range(1, 11):
        print(f"{numero} x {n} = {numero * n}")


# EJERCICIO 7

def operaciones_basicas(a, b):
    resultado_suma = f"Suma: {suma(a, b)}"
    resultado_resta = f"Resta: {resta(a, b)}"
    resultado_multiplicacion = f"Multiplicacion: {multiplicacion(a, b)}"
    resultado_division = f"Division: {division(a, b)}"

    tupla = (resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)
    return tupla

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "error. division por cero"


# EJERCICIO 8

def calcular_imc(peso, altura):
    return division(peso, altura ** 2)


# EJERCICIO 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# EJERCICIO 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# PROGRAMA PRINCIPAL

#1
hola_mundo()

#2
saludar_usuario("Franco")

#3
nombre_ingresado = input("Ingrese su nombre: ")
apellido_ingresado = input("Ingrese su apellido: ")
edad_ingresada = input("Ingrese su edad: ")
residencia_ingresada = input("Ingrese su residencia: ")

informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)

#4
radio = float(input("Ingrese el radio del circulo: "))

print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")

#5
segundos_ingresados = float(input("Ingrese una cantidad de segundos: "))

print(f"Cantidad de horas: {segundos_a_horas(segundos_ingresados)}")

#6
num_ingresado = int(input("Ingrese un numero: "))

tabla_multiplicar(num_ingresado)

#7
operaciones_basicas(7, 0)

#8
peso_ingresado = float(input("Ingrese su peso en kilogramos: "))
altura_ingresada = float(input("Ingrese su altura en metros: "))

print(f"Su IMC es: {calcular_imc(peso_ingresado, altura_ingresada)}")

#9
temp_en_celsius = float(input("Ingrese la temperatura en celsius: "))

print(f"La temperatura ingresada es {celsius_a_fahrenheit(temp_en_celsius)} en Fahrenheit")

#10
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

print(f"El promedio entre los números ingresados es: {calcular_promedio(num1, num2, num3)}")