#(3) Un frasco de dulces de Halloween contiene una cantidad
#desconocida de dulces y si puedes adivinar exactamente
#cuántos dulces hay en el tazón, entonces ganas todos los
#dulces. La persona a cargo te dice: Si el caramelo se divide en
#partes iguales entre 5 personas, quedarían 2 dulces. Si se
#dividen en partes iguales entre 6 personas, la cantidad restante
#es de 3 piezas. Por último, pregunta por dividir los dulces en
#partes iguales entre 7 personas, y la cantidad que queda es de 2
#piezas. Al mirar el cuenco, puede ver que hay menos de 200
#piezas. Escribe un programa para determinar cuántas piezas hay
#en el cuenco.

for i in range(1, 200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print(f"La cantidad de dulces en el cuenco es {i}")
        break
