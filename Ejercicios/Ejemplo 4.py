#(4) Escriba un programa que le pida al usuario que ingrese un número e imprima todos los divisores de ese número

numero = int(input("Ingrese un número: "))

print(f"Los divisores de {numero} son: ")

for i in range(1, numero+1):
    if numero % i == 0:
        print(i)