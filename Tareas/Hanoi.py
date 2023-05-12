def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mueve el disco 1 de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        print(f"Mueve el disco {n} de {origen} a {destino}")
        hanoi(n-1, auxiliar, destino, origen)

# Menú de usuario
print("Bienvenido al juego de la Torre de Hanoi")
while True:
    try:
        discos = int(input("¿Con cuántos discos quiere jugar? "))
        if discos <= 0:
            print("El número de discos debe ser mayor que cero")
        else:
            break
    except ValueError:
        print("Debe ingresar un número entero")

print(f"Comenzando el juego con {discos} discos")
print("Los movimientos a realizar son:")
hanoi(discos, "A", "C", "B")