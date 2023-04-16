
edad = int(input("Ingrese su edad: "))
mes = int(input("Ingrese el mes de su cumpleaños (en número): "))

if edad <= 0:
    print("Sea serio")
    edad = int(input("Ingrese su edad nuevamente: "))
    mes = input("Ingrese el mes de su cumpleaños (en número): ")
    if edad > 0 and edad < 18:
        print("Es usted menor de edad")
    elif edad > 18 or (edad == 18 and int(mes) <= 2):
        print("Es usted mayor de edad")
    else:
        print("Es usted menor de edad")
else:
    if edad > 18 or (edad == 18 and int(mes) <= 2):
        print("Es usted mayor de edad")
    else:
        print("Es usted menor de edad")





