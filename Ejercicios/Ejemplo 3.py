#(3) Escriba un juego que le permita al usuario jugar piedra papel o tijera cierto numero de rondas y al final diga el marcador.

import random

opciones = ["piedra", "papel", "tijera"]

rondas = int(input("Ingrese el número de rondas que desea jugar: "))

puntosJ = 0
puntosNPC = 0

for i in range(rondas):
    print(f"Ronda {i + 1}")
    eleccionJ = input("¿Piedra, papel o tijera? (en minúscula): ").lower()
    while eleccionJ not in opciones:
        eleccionJ = input("Opción inválida. Intente de nuevo: ")
    eleccionNPC = random.choice(opciones)
    print(f"La computadora eligió: {eleccionNPC}")

    if eleccionJ == eleccionNPC:
        print(f"Es un empate. Ambos eligieron {eleccionJ}")
    elif eleccionJ == "piedra" and eleccionNPC == "tijera" \
            or eleccionJ == "papel" and eleccionNPC == "piedra" \
            or eleccionJ == "tijera" and eleccionNPC == "papel":
        print(f"Ganaste, {eleccionJ} le gana a {eleccionNPC}")
        puntosJ += 1
    else:
         print(f"Perdiste, {eleccionNPC} le gana a {eleccionJ}")
         puntosNPC += 1

print(f"El puntaje final es:")
print(f"Jugador: {puntosJ}")
print(f"Computadora: {puntosNPC}")

if puntosJ > puntosNPC:
    print("¡Felicidades! ¡Has ganado el juego!")
elif puntosNPC > puntosJ:
    print("Lo siento, has perdido el juego.")
else:
    print("El juego ha terminado en empate.")
