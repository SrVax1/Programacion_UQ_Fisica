#Escriba un programa que le pida al usuario diez números y le
#diga cuál es el mayor (menor) número de todos.

numeros = []

for i in range(10):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)

print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")
