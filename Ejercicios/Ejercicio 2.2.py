#Realice un programa que pase de kilogramos a libras,
#cerciorándose que se ingrese un dato correcto

while True:
    kg_o_lb = int(input(("Quiere pasar (kg a lb) o (lb a kg) (1 o 2): ")))

    if kg_o_lb == 1:
        while True:
            kg = int(input("Ingrese los kilogramos: "))
            if kg < 0:
                print("Número inválido")
            else:
                lb = kg * 2.20462
                print(f"{kg :.2f} kg son equivalentes a {lb :.2f} lb.")
            break

    elif kg_o_lb == 2:
        while True:
            lb = int(input("Ingrese las libras: "))
            if lb < 0:
                print("Número inválido")
            else:
                kg = lb * 0.453592
                print(f"{lb :.2f} lb son equivalentes a {kg :.2f} kg.")
            break