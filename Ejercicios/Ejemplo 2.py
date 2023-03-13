#(2) Escribe un programa de juegos de multiplicación para niños. 
#El programa debe dar al jugador diez preguntas de multiplicación generadas al azar. Después de cada uno, 
#el programa debe decirles si lo hicieron bien o mal y cuál es la respuesta correcta

import random

aciertos = 0

for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    respuesta = num1 * num2
    usuario = int(input(f"¿Cuánto es {num1} por {num2}? "))
    if usuario == respuesta:
        print("¡Muy bien! ¡Respuesta correcta!")
        aciertos += 1
    else:
        print(f"Lo siento, respuesta incorrecta. La respuesta correcta era {respuesta}.")

print(f"¡Has acertado {aciertos} de 10 preguntas! Aquí están las respuestas: ")

