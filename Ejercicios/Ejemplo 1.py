#(1)Escribir un programa que solicite el nivel de Ph y si está entre 0 − 4 decir que es un ácido fuerte, 5 − 6 ácido debil, 7 neutral, 8 − 9 base debil y 10 − 14 base fuerte

while True:
    acido = input("Ingrese el Ph (o escriba 'salir' para terminar): ")
    if acido.lower() == 'salir':
        break  
    acido = int(acido)
    if acido >= 0 and acido <= 4:
        print("Es un ácido fuerte")
    elif acido == 5 or acido == 6:  
        print("Es un ácido débil")
    elif acido == 7:
        print("Es un ácido neutro")
    elif acido == 8 or acido == 9:  
        print("Es una base débil")
    elif acido >= 10 and acido <= 14:
        print("Es una base fuerte")
    else:
        print("Número no válido")
