#(1) Escriba un programa que le permita al usuario pasar una temperatura
#de grados centígrados, farenheit o Kelvin a la escala térmica que el desee.

def C_a_F(temp_c):
    return (temp_c * 1.8) + 32

def C_a_K(temp_c):
    return (temp_c + 273.15)

def F_a_C(temp_f):
    return (temp_f - 32) / 1.8

def F_a_K(temp_f):
    return (temp_f + 459.67) * 5/9

def K_a_C(temp_k):
    return (temp_k - 273.15)

def K_a_F(temp_k):
    return (temp_k * 9/5 - 459.67)

while True:
    temperatura = input("Ingrese la temperatura (Escriba no para salir): ")
    if temperatura.lower() == "no":
        print("Okey")
        break
    else:
        temperatura = float(temperatura)
    
    escala = input("En qué escala se encuentra? (C, F, K): ").upper()
    
    if escala == "C":
        temp_c = temperatura
    elif escala == "F":
        temp_c = F_a_C(temperatura)
    elif escala == "K":
        temp_c = K_a_C(temperatura)
    else:
        print("Escala no válida")
        continue
    
    nueva = input("Ingrese la escala a la que desea convertir: (C, F, K): ").upper()
    nueva_escala = ""

    if nueva == "C":
        nueva_temp = temp_c
        nueva_escala = "C"
    elif nueva == "F":
        nueva_temp = C_a_F(temp_c)
        nueva_escala = "F"
    elif nueva == "K":
        nueva_temp = C_a_K(temp_c)
        nueva_escala = "K"
    else:
        print("Escala no válida")
        continue
    
    print("{:.2f} {} = {:.2f} {}".format(temperatura, escala, nueva_temp, nueva_escala))








