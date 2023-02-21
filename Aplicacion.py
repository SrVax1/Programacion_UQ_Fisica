# Defino la clase vector
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def producto_cruz(self, otro):
        x_nuevo = self.y * otro.z - self.z * otro.y
        y_nuevo = self.z * otro.x - self.x * otro.z
        z_nuevo = self.x * otro.y - self.y * otro.x
        return (x_nuevo, y_nuevo, z_nuevo)

    def __mul__(self, escalar):
        x_nuevo = self.x * escalar
        y_nuevo = self.y * escalar
        z_nuevo = self.z * escalar
        resultado = Vector(x_nuevo, y_nuevo, z_nuevo)
        return resultado

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

# Fuerza de Lorentz es F = q * (V X B), lo que sería así:
print("Ingrese coordenadas del vector velocidad")
x_1 = float(input("Componente X: "))
y_1 = float(input("Componente Y: "))
z_1 = float(input("Componente Z: "))

print("Ingrese coordenadas del vector del campo mágnetico")
x_2 = float(input("Componente X: "))
y_2 = float(input("Componente Y: "))
z_2 = float(input("Componente Z: "))

print("El resultado de los vectores es:")
vec_1 = Vector(x_1, y_1, z_1)
vec_2 = Vector(x_2, y_2, z_2)

print("Vector 1: ", vec_1)
print("Vector 2: ", vec_2)

print("Ingrese la carga eléctrica:")
q = int(input("La carga es (número entero): "))

producto_cruz = vec_1.producto_cruz(vec_2)
fuerza = Vector(*producto_cruz) * q

print("Entonces la fuerza de Lorentz es: ", fuerza)
