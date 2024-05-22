
class Traductor:
    def __init__(self):
        self.r = ""
        self.Principio()

    def Principio(self):
        self.r = input("Coloque 's' si desea continuar o 'n' si no lo desea: ")
        if self.r != "s" and self.r != "n":
            self.Principio()
        elif self.r == "s":
            self.de = input("de qué base se va a traducir? (B/T/C/O/H): ")
            self.a = input("a qué base lo quieres pasar? (B/T/C/O/H): ")
            if self.de :
            self.traducir_decimal()
            self.Principio()
        else:
            print("Gracias por usar el traductor de bases")

    def traducir_decimal(self):
        if self.de == "B" and self.a != "B":
            self.b = input("Coloque su número en binario: ")
            self.decimal = int(0)
            longitud = len(self.b)
                
            for i in range(longitud):
                 if self.b[i] != "0" and self.b[i] != "1":
                    print("No cumple con la especificaciones del binario")
                    break

                 bit = int(self.b[i])
                 exponente = longitud - i - 1
                 self.decimal += bit * (2 ** exponente)
            print(self.decimal)
        else:
            print("No puedes pasar de binario a binario")
        if self.de == "T"
    
        

Traductor = Traductor()


