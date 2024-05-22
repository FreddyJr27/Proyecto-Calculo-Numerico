import random
import numpy as np
n = int(input("Ingrese la dimensión de la matriz cuadrada (n): "))
p = input("Desea rellenar la matriz (r) o que se rellene automaticamente (a)?  ")
# se creo una matriz de tamaño nxn
matriz = np.zeros((n,n))
ma = np.zeros((n,1))
if p == "r":
    # Crear una matriz vacía de tamaño nxn
    

    # Pedir al usuario los valores para cada posición
    for i in range(n):
        
        for j in range(n):
            valor = int(input(f"ingrese el valor de la posición ({i}, {j}): "))
            matriz[i,j] = valor
    for k in range(n):
        valor2 = int(input(f"ingrese los valores de la segunda matriz ({k}): "))
        ma[k] = valor2

elif p == "a":
   for i in range(n):
        
        for j in range(n):
            valor = int(random.randint(-100,100))
            matriz[i][j] = valor
    
   for k in range(n):        
        valor2 = int(random.randint(-100,100))
        ma[k]= valor2

# Imprimir la matriz ingresada por el usuario
print("Matriz ingresada:")

print(matriz)

print(ma)
