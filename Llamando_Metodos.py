from Metodos import *

def main():
    my_world = hello_world()
    
    # Conversion a str

    my_world = str(my_world)

    new_world = my_world.split("l")

    print(f'Lista completa: {new_world}')

    print(f'This is new_world: {new_world[::-1]}')

def sumando():
    n1 = int(input("Ingresa tu primer numero:\n"))
    n2 = int(input("Ingresa tu segundo numero:\n"))

    res_suma = suma_simple(n1,n2)

    print(f'\nEl resultado de {n1} + {n2} es {res_suma}')

def palindromo_checker():

    palabra = str(input("Dame tu palabra:\n"))
    print(f'que hay: {palabra.lower().replace(" ", "")}')
    check = check_palindromo(palabra.lower().replace(" ", ""))

    print(check)

if __name__ == '__main__':
    palindromo_checker()