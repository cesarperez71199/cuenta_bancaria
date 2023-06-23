#Inicio de clase
class CuentaBancaria:
    saldo=None
    nombre=None
    
#Constructor de la clase
def __init___ (self,saldo,nombre):
    
    if((type(saldo)==int or type(saldo)==float) and isinstance(nombre, str)):
        
        self.saldo=saldo
        self.nombre=nombre
        self.mostrarInformacion()
        
#Sino son de tipo especifico, se ponen valores por default
    else:
        self.saldo=0
        self.nombre="Desconocido"
        self.mostrarInformacion()
        
#Metodo que muestra el nombre del cliente y su saldo que es usado por mas metodos
#para saber el estado de cuenta
      

def mostrarInformacion(self):
    print(self.nombre + "cuenta con: " + str(self.saldo)+ "de saldo")
    
    
    
#Creacion de los metodos depositar y retirar  
def deposito(self,cantidad):
    if type(cantidad)==int or type(cantidad)==float:
        print("Deposito de "+ self.nombre+ "por: "+ str(cantidad))
        
        self._calcularSaldo(cantidad)
        self._mostrarInformacion()
        
    else:
        print("Deposito de "+ self.nombre+ "por: "+str(cantidad))
        print("las cantidades deben ser numeros")
        
        
def retiro(self,cantidad):
    if type(cantidad)==int or type(cantidad)==float:
        print("Retiro de "+ self.nombre + "por"+ str(cantidad))
        cantidadRetirar=cantidad
        
        if cantidadRetirar >self.saldo:
            print(self.nombre + "No hay saldo suficiente")
            
        else:
            #Resta la cantidad original de la cuenta
            self._calcularSaldo(self.saldo - cantidadRetirar)
            self.mostrarInformacion()
            
    else:
        print("Retiro de "+ self.nombre + "por"+ str(cantidad))
        print("Las cantidades deben ser numeros")
        
    
#Metodo que calcule (getter) el saldo de la cuenta

def _calcularSaldo(self,cantidad):
    #saldo asociado a la cuenta
    self.saldo=cantidad
    
    
#creacion de dos onjetosde la clase CuentaBancaria
    objeto1=CuentaBancaria(12,"pedro")
    objeto2=CuentaBancaria(125,"juan")
    
#Manipulacion de las funciones de los objetos
    
    objeto2.retiro(89)
    objeto1.retiro(120000)
    objeto1.deposito("mil doscientos")
