#Defino la clase vector, con su magnitud, suma, producto punto y producto cruz
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

#Todos los resultados de los vectores
print("El resultado de los vectores es:")
vec_1 = Vector(x_1, y_1, z_1)
vec_2 = Vector(x_2, y_2, z_2)
esc1 = esc
print("Vector 1: ", vec_1)
print("Vector 2: ", vec_2)
print("El escalar:", esc)

#Pedir qué quiere
pregunta = (print(input("¿Quiere producto punto o producto por escalar? (1 o 2 respectivamente): ")))
punto = vec_1*esc1 
escalar = Vector(vec_1*vec_2)

if pregunta == 1:
    print("El resultado de la operación es:", punto)
else:
    print("El resultado de la operación es:", escalar)

#Revisar linea
