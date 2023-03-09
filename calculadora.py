num1 = int(input(""))
num2 = int(input(""))

def suma(numero1, numero2):
    total = numero1 + numero2
    return total

def resta(numero1, numero2):
    total = numero1 - numero2
    return total

def multi(num1, num2):
    total =num1 * num2
    return total
    

resultado = suma(num1, num2)
resultado2 = resta(num1, num2)
resultador3= multi(num1,num2)

print('El resultado es: ',resultado,"y",resultado2,"y",resultador3)