### EJERCICIO 1
print("Hola Mundo!")

### EJERCICIO 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

### EJERCICIO 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre + ' ' + apellido}, tengo {edad} años y vivo en {lugar_residencia}")

### EJERCICIO 4
radio = float(input("Ingrese el radio de un circulo: "))

area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio

print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

### EJERCICIO 5
segundos = int(input("Ingrese cantidad de segundos: "))
minutos = segundos//60
horas = minutos//60

print(f"Cantidad de horas equivalentes: {horas}")

### EJERCICIO 6
numero = int(input("Ingrese un numero: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

### EJERCICIO 7
num1 = int(input("Ingrese un numero distinto de cero: "))
num2 = int(input("Ingrese otro numero distinto de cero: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Division: {num1 / num2}")

### EJERCICIO 8
peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura

print(f"Su IMC es: {imc}")

### EJERCICIO 9
temp_celsius = float(input("Ingrese la temperatura en Celsius: "))
temp_fahrenheit = 9/5 * temp_celsius + 32

print(f"La temperatura en Fahrenheit es: {temp_fahrenheit}")

### EJERCICIO 10
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es: {promedio}")