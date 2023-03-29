from string import punctuation
import random

# #Defino clase matriz, con vector por si es solo una fila, suma y resta.
# class Matriz:
#   def __init__(self, valores, n, m):
#     self.valores = [valores[i:i+m] for i in range(0, n*m, m)]
#     self.shape = [n, m]
#     self.is_valid = self.validar_matriz()

#   def validar_matriz(self):
#     indices_invalidos = []
#     for i in range(self.shape[0]):
#       for j in range(self.shape[1]):
#         if type(self.valores[i][j]) not in [int, float]:
#           indices_invalidos.append((i,j))
#     if len(indices_invalidos) == 0:
#       return [True, []]
#     else:
#       return [False, indices_invalidos]

#   def __str__(self):
#     if self.shape[0] == 1:
#       respuesta = self.vector_(0)
#       return respuesta
#     else:
#       respuesta = ""
#       for i in range(self.shape[0]-1):
#         respuesta = respuesta + self.vector_(i) + "\n"
#       respuesta = respuesta + self.vector_(self.shape[0]-1)
#       return respuesta
    
#   def vector_(self, fila):
#     respuesta = "|"
#     for i in range(self.shape[1]-1):
#       respuesta = respuesta + str(self.valores[fila][i])
#       respuesta = respuesta + " "
#     respuesta = respuesta + str(self.valores[fila][-1]) + "|"
#     return respuesta

#   def __add__(self, otra):
#     if self.shape != otra.shape:
#       print("Tamaños distintos. No es posible la suma")
    
#     resultado = []
#     for i in range(self.shape[0]):
#       fila = []
#       for j in range(self.shape[1]):
#         fila.append(self.valores[i][j] + otra.valores[i][j])
#       resultado.append(fila)
#     return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])

#   def __sub__(self, otra):
#     if self.shape != otra.shape:
#       print("Tamaños distintos. No es posible la resta")
#     else:
#       resultado = []
#       for i in range(self.shape[0]):
#         fila = []
#         for j in range(self.shape[1]):
#           fila.append(self.valores[i][j] - otra.valores[i][j])
#         resultado.append(fila)
#       return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])

# #Método para multiplicar por un escalar
#   def escalar(self, e):
#     if type(e) in [int, float]:
#       resultado = [[0]*self.shape[1] for _ in range(self.shape[0])]
#       for i in range(self.shape[0]):
#         for j in range(self.shape[1]):
#           resultado[i][j] = self.valores[i][j] * e
#       return Matriz([elem for fila in resultado for elem in fila], self.shape[0], self.shape[1])
#     else:
#       print("Lo ingresado no es un escalar")
  
# #Ahora defino mul y rmul para poder hacer las operaciones entre matrices al momento de G-J
#   def __mul__(self, otra):
#     if self.shape[1] != otra.shape[0]:
#       print("Las matrices no pueden multiplicarse")
#     resultado = [[0]*otra.shape[1] for _ in range(self.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
#     for i in range(self.shape[0]):
#       for j in range(otra.shape[1]):
#         for k in range(self.shape[1]):
#           resultado[i][j] += self.valores[i][k]*otra.valores[k][j]
#     return Matriz([elem for fila in resultado for elem in fila], self.shape[0], otra.shape[1])

#   def __rmul__(self, otra):
#     if self.shape[1] != otra.shape[0]:
#       print("Las matrices no pueden multiplicarse")
#     resultado = [[0]*self.shape[1] for _ in range(otra.shape[0])] #Matriz llena de 0 con las mismas dimensiones para llevar a cabo las mult.
#     for i in range(otra.shape[0]):
#       for j in range(self.shape[1]):
#         for k in range(otra.shape[1]):
#           resultado[i][j] += otra.valores[i][k]*self.valores[k][j]
#     return Matriz([elem for fila in resultado for elem in fila], self.shape[0], otra.shape[1])
  
def palabra_a_vector(palabra):
    for i in punctuation:
        palabra = palabra.replace(i, "")
    tildes = "áéíóúÁÉÍÓÚ"
    for i in range(len(tildes)):
        palabra = palabra.replace(tildes[i], "áéíóúÁÉÍÓÚ"[i])
    palabra = palabra.split()
    vector = []
    for i in palabra:
        vector.append(len(i))
    return(vector)

# print(palabra_a_vector("Hola, cómo estás?"))

def matriznxn(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(1, 10))
        matriz.append(fila)
    return matriz

# N = 4  # Tamaño de la matriz
# matriz = matriznxn(N)
# print(matriz)

def ordenar_indices(vector):
    indices = []
    for j in range(len(vector)):
        indices.append(j)
    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[j] < vector[i]:
                vector[j], vector[i] = vector[i], vector[j]
                indices[j], indices[i] = indices[i], indices[j]
    return indices

vector = [5, 10, 2, 8, 3, 7]
print(vector)
indices = ordenar_indices(vector)
print(indices)