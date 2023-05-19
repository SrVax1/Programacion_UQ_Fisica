from scipy import stats

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"
    
    def edad_graduacion(self, años):
        return self._edad + años
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self._carrera = carrera
        self._calificaciones = [] # Lista vacía para almacenar calificaciones
        self._cursos = {} # Diccionario vacío para almacenar cursos y calificaciones

    def presentación(self):
        super().__str__()
        return f"Carrera: {self._carrera}"

    def edad_graduacion(self, años):
        nueva_edad = super().edad_graduacion(años)
        return f"Edad de graduación: {nueva_edad}"

    def agregar_calificacion(self, calificacion):
        self._calificaciones.append(calificacion)

    def agregar_curso(self, curso, calificacion):
        self._cursos[curso] = calificacion

    def agregar_calificacion_aleatoria(self):
        calificacion_aleatoria = int(stats.norm.rvs(loc=70, scale=10))
        self.agregar_calificacion(calificacion_aleatoria)

estudiante1 = Estudiante("Juan", 20, "Ingeniería")
estudiante1.agregar_calificacion(90)
estudiante1.agregar_calificacion(85)
estudiante1.agregar_curso("Matemáticas", 90)
estudiante1.agregar_curso("Física", 85)
estudiante1.agregar_calificacion_aleatoria()

print(estudiante1) # Nombre: Juan, Edad: 20
print(estudiante1.edad_graduacion(5)) # Edad de graduación: 25
print(estudiante1.presentación()) # Carrera: Ingeniería
print(estudiante1._calificaciones) # [90, 85, calificación aleatoria]
print(estudiante1._cursos) # {'Matemáticas': 90, 'Física': 85}
