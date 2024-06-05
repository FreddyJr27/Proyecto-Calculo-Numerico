import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def power_method(matrix, num_iterations):
    # Inicialización del vector inicial
    n = matrix.shape[0]
    initial_vector = np.ones(n)

    # Iteraciones del método de las potencias
    for _ in range(num_iterations):
        # Multiplicación de la matriz por el vector
        product = np.dot(matrix, initial_vector)

        # Normalización del vector resultante
        initial_vector = product / np.linalg.norm(product)

    # Cálculo del autovalor dominante
    eigenvalue = np.dot(np.dot(matrix, initial_vector), initial_vector) / np.dot(initial_vector, initial_vector)

    return eigenvalue, initial_vector
n = int(random.randint(2,4))
m = int(random.randint(2,4))
matriz = np.zeros((m,n))
for i in range(m):
        
        for j in range(n):
            valor = int(random.randint(-100,100))
            matriz[i][j] = valor
    
print(matriz)   
autovalor,autovector = power_method(matriz,100)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(n)
y = np.arange(m)
X, Y = np.meshgrid(x, y)
Z = matriz

ax.plot_surface(X, Y, Z, cmap='hot')

ax.set_xlabel('Columna')
ax.set_ylabel('Fila')
ax.set_zlabel('Valor')

plt.show()

print("autovalor: ")
print(autovector)
print("autovector dominate: ", autovalor)
