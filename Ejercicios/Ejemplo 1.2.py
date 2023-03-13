#Realizar un programa que calcule el MCD, para ello use el
#algoritmo de Euclides
#• Primero calcule el residuo de dividir el número más grande por el
#número más pequeño
#• Luego, reemplace el número más grande con el número más
#pequeño y el número más pequeño con el residuo.
#• Repita este proceso hasta que el número menor sea 0. El MCD es
#el último residuo diferente de cero

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

def MCD(numero1, numero2):
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1

print(f"El MCD de {numero1} y {numero2} es: {MCD(numero1, numero2)}")