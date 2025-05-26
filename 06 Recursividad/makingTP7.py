# EJERCICIO 1

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num_ingresado = int(input("Ingrese un numero entero: "))

# NO ESPECIFICA QUE ESTA PARTE DEBE HACERSE DE MANERA RECURSIVA
for i in range(1, num_ingresado + 1):
    print(f"El factorial de {i} es: {factorial(i)}")


# EJERCICIO 2

def fibonacci(n):
    # CASOS BASE
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num_fibonacci = int(input("Ingrese un numero entero: "))

# NO ESPECIFICA QUE ESTA PARTE DEBE HACERSE DE MANERA RECURSIVA
for i in range(1, num_ingresado + 1):
    print(fibonacci(i))


# EJERCICIO 3

def potencia_de_n(n, m):
    # CASO BASE: CUALQUIER NUMERO ELEVADO A 0 ES 1 
    if m == 0:
        return 1
    else:
        return n * potencia_de_n(n, m-1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese un exponente: "))

print(f"El resutado de {base} elevado a {exponente} es {potencia_de_n(base, exponente)}")


# EJERCICIO 4

def convertir_a_binario(decimal):
    # CASOS BASE
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return convertir_a_binario(decimal // 2) + str(decimal % 2)


# EJERCICIO 5

def es_palindromo(palabra):
    if len(palabra) == 0:
        return True
    elif len(palabra) == 1:
        return True # UNA PALABRA CON UNA SOLA LETRA ES SIEMPRE PALINDROMA
    elif palabra[0] == palabra[-1]: # SI LA PRIMER LETRA ES LA MISMA QUE LA ULTIMA ES PALINDROMA
        return es_palindromo(palabra[1:-1]) # ACHICO LA PALABRA
    else:
        return False


# EJERCICIO 6

def suma_digitos(n):
    if n < 10: # CASO BASE
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


# EJERCICIO 7

def contar_bloques(n):
    if n == 1: # CASO BASE
        return 1
    else:
        return n + contar_bloques(n-1)


# EJERCICIO 8

def contar_digito(numero, digito):
    if len(numero) == 0: # CASO BASE
        return 0
    elif numero[0] == str(digito):
        return 1 + contar_digito(numero[1:], digito)
    else:
        return contar_digito(numero[1:], digito)