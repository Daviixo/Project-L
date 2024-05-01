# Ejemplos de variables en Python
entero = 10
flotante = 3.14
cadena = "Hola, mundo!"
lista = [1, 2, 3, 4, 5]
lista2 = ["Luigui", "David", "Ricardo"]
tupla = (1, "dos", 3.0)
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# Print por cada elemento de diferentes formas

#print('Entero: ' + entero)
print('Entero:', entero)
print(f'Entero: {entero}')

print(f'\nFlotante o float: {flotante}')

print(f'\nCadena o String: {cadena}')

print(f'\nElemento 0 de la lista: {lista[0]}')

# Usando for para imprimir una lista completa

print('-- Imprimiendo una lista --')

for n in lista:
    print(f'\nEl elemento {n} es: {n}')

print(f'\nImprimiendo la lista completa: {lista}')

print(f'\nImprimiendo la tupla completa: {tupla}')

# Usando for para imprimir la tupla

print('\n-- Imprimiendo una tupla --')

for n in tupla:
    print(f'El elemento {n} es: {n}')

print(f'\n-- Imprimiendo un diccionario --')

print(f'Diccionario completo: {diccionario}')

# Imprimiendo un elemento especifico del diccionario

print(f'Diccionario: {diccionario["clave1"]}')

# num1 = input("Ingresa un numero:\n")
# num2 = int(input("Ingresa otro numero\n"))

# resultado = int(num1) + num2

# print(f'La suma de {num1} y {num2} es = {resultado}')

# num3 = int(input("Ingresa un numero:\n"))
# num4 = int(input("Ingresa otro numero\n"))

# resultado2 = num3 + num4

# print(f'Resultado: {resultado2}')

# name = str(input("Dame tu nombre:\n"))
# last_name = str(input("Dame tu apellido:\n"))

# nombre_completo = name + " " + last_name

# print(f'Mi nombre completo es: {name} {last_name}.')
# print(f'Mi nombre completo es:', nombre_completo)

variable_x = f"""Instrucciones:

Paso 1: x
Paso 2: y
Paso 3: z

{entero}

"""

print(variable_x)