import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Constantes
G = 1  # Constante gravitacional normalizada
m1 = 1.0  # Masa del cuerpo 1
m2 = 1.0  # Masa del cuerpo 2
r1 = np.array([-0.5, 0, 0])  # Posición del cuerpo 1
r2 = np.array([0.5, 0, 0])   # Posición del cuerpo 2

# Condiciones iniciales del cuerpo liviano
x0, y0, z0 = 0.1, 0, 0  # Posición inicial en 3D
vx0, vy0, vz0 = 0, 1.5, 0.1  # Velocidad inicial en 3D

# Ecuaciones de movimiento para el cuerpo liviano
def motion(t, y):
    x, y, z, vx, vy, vz = y
    r = np.array([x, y, z])
    acc1 = -G * m1 * (r - r1) / np.linalg.norm(r - r1)**3
    acc2 = -G * m2 * (r - r2) / np.linalg.norm(r - r2)**3
    acc = acc1 + acc2
    return [vx, vy, vz, acc[0], acc[1], acc[2]]

# Resolver el problema de valor inicial
t_span = (0, 20)  # Tiempo total de simulación
y0_vec = [x0, y0, z0, vx0, vy0, vz0]  # Vector de estado inicial
sol = solve_ivp(motion, t_span, y0_vec, method='RK45', dense_output=True)

# Función para animar
def animate(i):
    ax.clear()
    ax.plot(sol.y[0][:i], sol.y[1][:i], sol.y[2][:i], label='Cuerpo liviano')
    ax.scatter([r1[0], r2[0]], [r1[1], r2[1]], [r1[2], r2[2]], color='red', label='Cuerpos masivos')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Animación 3D del Problema Restringido de Tres Cuerpos")

# Crear la figura y los ejes en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, animate, frames=300, interval=20)

# Mostrar la animación
plt.show()



