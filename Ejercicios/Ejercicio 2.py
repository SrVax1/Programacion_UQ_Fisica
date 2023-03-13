#(2)  Escriba un programa que le pida al usuario una hora entre la 1 y
#las 12, le pida que ingrese am o pm y le pregunte cuántas horas
#en el futuro quiere ir. Imprima cuál será la hora dentro de tantas
#horas en el futuro, imprimiendo am o pm según corresponda. A
#continuación se muestra un ejemplo. (Se pueden ingresar
#número mucho mayores a 24)

while True:
    hora = int(input("Ingrese la hora (1 a 12): "))

    while hora < 1 or hora > 12:
        hora = int(input("Hora inválida. Ingrese la hora (1 a 12): "))

    ap = input("¿Es am o pm? ").lower()

    while ap != "am" and ap != "pm":
        ap = input("Inválido. Ingrese am o pm: ").lower()

    futuro = int(input("Ingrese las horas en el futuro a las que quiere ir: "))

    nueva_hora = hora + futuro

    nueva = (nueva_hora - 1) % 12 + 1

    if ap == "am" and nueva_hora >= 12:
        nuevoap = "pm"
    elif ap == "pm" and nueva_hora < 12:
        nuevoap = "pm"
    elif ap == "pm" and nueva_hora < 12:
        nuevoap = "am"
    elif ap == "pm" and nueva_hora >= 12:
        nuevoap = "am"
    else:
        nuevoap = ap

    print(f"En {futuro} horas, serán las {nueva} {nuevoap}")


