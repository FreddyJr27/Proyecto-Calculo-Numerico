import random
import numpy as np


class GaussSeidelSolver:
    def __init__(self, iteraciones=100, t=1e-6):
        
        self.ite = iteraciones
        self.t = t

    def solve(self, A, b):
       
        n = len(b)
        #se crea un vector lleno de ceros
        x = np.zeros(n)  

        for _ in range(self.ite):
            # se copia el vector x cada vez que se repite las iteraciones
            x1 = np.copy(x)  

            for i in range(n):
                # Calcula la suma de los productos de los coeficientes y las soluciones conocidas,
                # tanto para los términos anteriores como para los términos posteriores a la incógnita actual.
                sum1 = np.dot(A[i, :i], x1[:i])
                sum2 = np.dot(A[i, i + 1:], x[i + 1:])

                # Calcula la nueva solución para la incógnita actual utilizando la fórmula del método de Gauss-Seidel.
                x1[i] = (b[i] - sum1 - sum2) / A[i, i]

            # Comprueba la condición de convergencia: si la norma de la diferencia entre las soluciones
            # anteriores y las soluciones actuales es menor que la tolerancia, devuelve la solución actual.
            if np.linalg.norm(x1 - x) < self.t:
                return x1

            x = x1  

        return x
    

   
#se le pide al usuario de cuanto va a ser la matriz nxn y se le pregunta si se va rellenar auto matico o no
n = int(input("Cual va a ser el valor de n para la matriz nxn (n): "))
p = input("Desea rellenar la matriz (r) o que se rellene automaticamente (a)?  ")
#se crean las matrices llenas de ceros
matriz = np.zeros((n,n))
ma = np.zeros((n,1))
#si el usuario quizo rellenar la matriz
if p == "r":
    
#se le pide con un bucle que vaya rellenando posicion por posicion 
    
    for i in range(n):
        
        for j in range(n):
            valor = int(input(f"ingrese el valor de la posición ({i}, {j}): "))
            matriz[i,j] = valor
    for k in range(n):
        valor2 = int(input(f"ingrese los valores de la segunda matriz ({k}): "))
        ma[k] = valor2
#si el usuario quizo que se rellenara automatico
elif p == "a":
   #se rellena automatico con numeros de -100 a 100 mediante bucles
   for i in range(n):
        
        for j in range(n):
            valor = int(random.randint(-100,100))
            matriz[i][j] = valor
    
   for k in range(n):        
        valor2 = int(random.randint(-100,100))
        ma[k]= valor2


print("Matriz creada:")

print(matriz)

print(ma)

solucion = GaussSeidelSolver()
solucion1 = solucion.solve(matriz, ma)
print("Solución:")
print(solucion1)
