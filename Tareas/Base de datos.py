import pandas as pd
import numpy as np

# Recibir archivo csv y leer archivo csv  
df = pd.read_csv('C:/Users/USUARIO/Documents/Base de Datos/MDG_0000000003 (1).csv')

# Retornar el nombre de las columnas y su tipo de datos
print(df.dtypes)

# Recibir el nombre de una columna str y una númerica int
columna1 = input("Ingrese el nombre de la columna 1: ")
columna2 = input("Ingrese el nombre de la columna 2: ")

# Retornar valores únicos de la columna 1
print(df[columna1].unique())

# Pedir al usuario un valor de la columna 1
valor1 = input("Ingrese el valor de la columna 1: ")

# Guardar en A los datos numéricos sin los valores de esa columna numérica
A = df[df[columna1] != valor1][columna2]

# Guardar en Y los datos de esa columna numérica
Y = df[df[columna1] == valor1][columna2]

# Calcular el rango de la matriz A
rango_A = np.linalg.matrix_rank(A)

# Verificar si la matriz A es invertible
if rango_A < len(A):
    print("La matriz A no es invertible, hay columnas linealmente dependientes.")
else:
    # Resolver sistema de ecuaciones lineales AX = Y
    X = np.linalg.solve(A, Y)
    # Exportar el resultado a un archivo csv
    np.savetxt('C:/Users/USUARIO/Documents/Base de Datos/resultado.csv', X, delimiter=',')



