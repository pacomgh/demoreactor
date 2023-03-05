num1 = 5
num2 = -2
num3 =10
def suma(numero1, numero2):
    total = numero1 * numero2
    return total

def resta(numero1, numero2):
    total = numero1 - numero2
    return total
def suma(numero1, numero3):
    total = numero1 + numero3
    return total

resultado = suma(num1, num2)
resultado2 = resta(num1, num2)
resultado3 = suma(num1, num3)

print('El resultado es: ', resultado2,resultado,resultado3)