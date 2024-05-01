# Ejemplos de operadores en Python
a = 10
b = 5

# Operadores aritméticos
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Operadores de comparación
igual = (a == b)
mayor_que = (a > b)
menor_que = (a < b)

# Operadores lógicos
y_logico = (a > 0) and (b > 0)
o_logico = (a > 0) or (b > 0)
negacion = not (a == b)

print(f'Suma: {suma}')

print(f'Resta: {resta}')

print(f'Multiplicacion: {multiplicacion}')

print(f'Division: {float(division)}')

print(f'Comparacion (igual): {igual}')

print(f'Comparacion (mayor que): {mayor_que}')

print(f'Comparacion (menor que): {menor_que}')

# Estructuras de control con if, elif y else

edad = int(input("Ingresa tu edad:\n"))

if edad < 18:
    print(f'Tu edad es {edad}, es menor a 18, por lo tanto eres menor de edad. Espera {18 - edad} años para ser mayor.')
elif edad > 18 and edad < 65:
    print(f'Actualmente tienes {edad}, por lo tanto eres mayor de edad')
elif edad > 65:
    print(f'Eres todo un adulto mayor!')
else:
    print("No ingresaste un numero. menso!")
