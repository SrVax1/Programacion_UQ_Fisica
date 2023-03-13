#Escriba un programa que le permita al usuario ingresar
#cualquier cantidad de calificaciones. El usuario indica que ha
#terminado ingresando un número negativo. Se debe imprimir la
#nota más baja, la mas alta y el promedio.

calificaciones = []
i = float(input("Ingrese las calificaciones (escriba un número negativo para salir): "))

while i >= 0:
    calificaciones.append(i)
    i = float(input("Ingrese otra calificación (escriba un número negativo para salir): "))

if len(calificaciones) == 0:
    print("No se ingresaron calificaciones")
else:
    min_calificacion = min(calificaciones)
    max_calificacion = max(calificaciones)
    promedio_calificaciones = sum(calificaciones) / len(calificaciones)
    print(f"La nota más baja es: {min_calificacion}")
    print(f"La nota más alta es: {max_calificacion}")
    print(f"El promedio de las calificaciones es: {promedio_calificaciones}")