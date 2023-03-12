#Hecho por Jhon S. García y Santiago Cardenas
# Defino la clase vector, producto escalar y por escalar
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
    
    def __mul__(self, otro):
        if type(self) == type(otro):
            resultado = (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)
            return resultado
        else:
            resultado = Vector((self.x * otro), (self.y * otro), (self.z * otro))
            return resultado
        
    def __rmul__(self, otro):
        if type(self) == type(otro):
            resultado = (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)
            return resultado
        else:
            resultado = Vector((self.x * otro), (self.y * otro), (self.z * otro))
            return resultado
        
# Ahora defino con matrices
class Matriz:
  def __init__(self, lista):
    self.a00=lista[0][0]
    self.a01=lista[0][1]
    self.a10=lista[1][0]
    self.a11=lista[1][1]

  def __str__(self):
    return "|{:^5} {:^5}|\n|{:^5} {:^5}|".format(self.a00, self.a01, self.a10, self.a11)

  def __add__(self, otro):
    a00 = self.a00 + otro.a00
    a01 = self.a01 + otro.a01
    a10 = self.a10 + otro.a10
    a11 = self.a11 + otro.a11
    return Matriz([[a00, a01], [a10, a11]])

  def __sub__(self, otro):
    a00 = self.a00 - otro.a00
    a01 = self.a01 - otro.a01
    a10 = self.a10 - otro.a10
    a11 = self.a11 - otro.a11
    return Matriz([[a00, a01], [a10, a11]])
 
  def __mul__(self, escalar):
    a00 = self.a00 * escalar
    a01 = self.a01 * escalar
    a10 = self.a10 * escalar
    a11 = self.a11 * escalar
    return Matriz([[a00, a01], [a10, a11]])

  def __rmul__(self, escalar):
    a00 = self.a00 * escalar
    a01 = self.a01 * escalar
    a10 = self.a10 * escalar
    a11 = self.a11 * escalar
    return Matriz([[a00, a01], [a10, a11]])
  
  def iesima(self, i):
    if i == 1:
      return [self.a00, self.a10]
    elif i == 2:
      return [self.a01, self.a11]
    else:
      return None

# Preguntar qué quiere el usuario
tipo = input("¿Quiere trabajar con vectores o matrices?: ")
if tipo == "vectores":
  # Pido definir vectores
  print("Ingrese coordenadas del primer vector")
  x_1 = float(input("Componente X: "))
  y_1 = float(input("Componente Y: "))
  z_1 = float(input("Componente Z: "))

  print("Ingrese coordenadas del segundo vector")
  x_2 = float(input("Componente X: "))
  y_2 = float(input("Componente Y: "))
  z_2 = float(input("Componente Z: "))

  print("Ahora un escalar (entero)")
  esc = int(input("Ingrese el escalar: "))

  # Todos los resultados de los vectores
  print("El resultado de los vectores es:")
  vec_1 = Vector(x_1, y_1, z_1)
  vec_2 = Vector(x_2, y_2, z_2)
  print("Vector 1: ", vec_1)
  print("Vector 2: ", vec_2)
  print("El escalar:", esc)

  # Pedir qué quiere
  pregunta = int(input("¿Quiere producto punto o producto por escalar? (1 o 2 respectivamente): "))
  punto = vec_1 * vec_2

  if pregunta == 1:
    print("El resultado del producto punto es:", punto)
  elif pregunta ==2:
    pregunta_esc = int(input("¿Quiere multiplicar el vector 1 o 2 por el escalar?: "))
    if pregunta_esc == 1:
      print("El producto por un escalar y el vector 1 es:")
      print(vec_1 * esc)
    elif pregunta_esc == 2:
      print("El producto por un escalar y el vector 2 es:")
      print(vec_2 * esc)
    else:
      print("Número no válido")
  else:
    print("Número no válido")

else:
   #Pedir a al usuario de forma estética :)
  print("Ingrese los valores de la primera matriz:")
  a00 = int(input("Ingrese A_11: "))
  a01 = int(input("Ingrese A_12: "))
  a10 = int(input("Ingrese A_21: "))
  a11 = int(input("Ingrese A_22: "))

  print("Ingrese los valores de la segunda matriz:")
  b00 = int(input("Ingrese B_11: "))
  b01 = int(input("Ingrese B_12: "))
  b10 = int(input("Ingrese B_21: "))
  b11 = int(input("Ingrese B_22: "))

  print("La primera matriz es: ")
  matriz_a = Matriz([[a00, a01], [a10, a11]])
  print(matriz_a)

  print("La segunda matriz es: ")
  matriz_b = Matriz([[b00, b01], [b10, b11]])
  print(matriz_b)

  escalar = int(input("Ingrese un escalar para multiplicar por la matriz: "))

  # Pedir qué quiere
  pregunta = int(input("¿Quiere sumar, restar o producto por un escalar entre matrices? (1, 2 o 3 respectivamente): "))
  suma = matriz_a + matriz_b
  resta = matriz_a - matriz_b
  esc = matriz_a * escalar

  if pregunta == 1:
   print(suma)
  elif pregunta == 2:
   print(resta)
  elif pregunta == 3:
   pregunta_esc = int(input("¿Quiere multiplicar la matriz 1 o 2 por el escalar?: "))
   if pregunta_esc == 1:
    print("El producto por un escalar de la matriz 1 es:")
    print(matriz_a * escalar)
   elif pregunta_esc == 2:
    print("El producto por un escalar de la matriz 2 es:")
    print(matriz_b * escalar)
   else:
    print("Número no válido")
  else:
   print("Número no válido")

#matriza = Matriz([[a00, a10], [a01, b11]])
#matrizb = Matriz([[b00, b10], [b01, b11]])

pregunta = int(input("¿De qué matriz desea obtener la i-ésima fila (1 o 2): "))
if pregunta == 1:
  i = int(input("Ingrese la i-ésima fila que desea obtener (1 o 2): "))
  fila_i = matriz_a.iesima(i)
  print("La fila i-ésima es: ")
  print(fila_i)
elif pregunta == 2:
  i = int(input("Ingrese la i-ésima fila que desea obtener (1 o 2): "))
  fila_i = matriz_b.iesima(i)
  print("La fila i-ésima es: ")
  print(fila_i)
else:
  print("Número no válido")