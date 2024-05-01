def hello_world():

    hello = "Hello, world!"

    #print(hello)

    return hello


def suma_simple(num1: int, num2: int):
    
    resultado = num1 + num2

    return resultado

def check_palindromo(palabra):
#[::-1]
    if palabra == palabra[::-1]:
        #print("SI ES!")

        return "si es"
    else:
        #print("NO ES, CHAVO!")
        return "no es"