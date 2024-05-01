class Cuenta:
    def __init__(self, persona, cantidad):
        self.persona = persona
        self.cantidad = cantidad
    def depositar(self, monto):
        if monto < 0:
            print ("el monto es menor a cero")
        else:   
            self.cantidad += monto
            
    
    def retirar(self, monto):
        if self.cantidad < monto:
            print("no tiene suficiente dinero en la cuenta")
        else:
            self.cantidad -= monto
            
    
    def mostrar(self):
        print("Usuario: "+ self.persona)
        print("Cuenta: "+str(self.cantidad))
    

nombre = input("Ingrese nombre del titular:")
cantidad = int(input("Cuanto dinero tiene en la cuenta: "))
t = 1
nuevo = Cuenta(nombre, cantidad)

while t == 1:
    
    
        deseoUsuario = input("Desea depositar(d) o retirar (r)?: ")
        if deseoUsuario == "r":
            retiro = float(input("Cuanto quiere retirar?: "))
            nuevo.retirar(retiro)
            nuevo.mostrar()
        elif deseoUsuario == "d":
            deposito = float(input("Cuanto quiere ingresar?:"))
            nuevo.depositar(deposito)
            nuevo.mostrar()
        else:
            print("Error! por favor, coloque r o d")
            
        t = int(input("Coloque 1 si quiere continuar o coloque 0 si quiere cerrar sesión: "))
        
if t == 0:
    print("La cuenta se ha cerrado")

    
