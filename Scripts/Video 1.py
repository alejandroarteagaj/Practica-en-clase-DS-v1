
import string 
import random


class Informaciondelvehiculo:
    Marca: string
    Precio_catalogo: int
    Hybrido: bool

    def __init__(self, marca, Hybrido, Precio_catalogo):
        self.Marca = marca
        self.Hybrido = Hybrido
        self.Precio_catalogo = Precio_catalogo
    
    def Calcular_impuesto(self):
        Porcentaje_impuesto = 0.05
        if self.Hybrido:
            Porcentaje_impuesto = 0.02
        return Porcentaje_impuesto * self.Precio_catalogo
    
    def print(self):
        print(f"Marca vehiculo : {self.Marca}")
        print(f"Impuesto a pagar: {self.Calcular_impuesto()}")

class vehiculo:
    serial: string
    placa: string
    informacion: Informaciondelvehiculo

    def __init__(self, serial, placa, informacion):
        self.serial = serial
        self.placa = placa
        self.informacion = informacion

    def print(self):
        print(f"Serial vehiculo: {self.serial}")
        print(f"Placa vehiculo: {self.placa}")
        self.informacion.print()
    
class Registro_vehiculo:

    Informaciondelvehiculo= { }
    def agregar_infoV(self,Marca, Hybrido, Precio_catalogo):
        self.Informaciondelvehiculo[Marca] = Informaciondelvehiculo(Marca,Hybrido,Precio_catalogo)

    def __init__(self):
        self.agregar_infoV("Corrolla cross",True,60000)
        self.agregar_infoV("Susuki swift",True,35000)
        self.agregar_infoV("Mazda 3",False,45000)
    
    def generar_SerialV(self, lenght):
        return ''.join(random.choices(string.ascii_uppercase, k=lenght))

    def generate_vehicle_licese(self, serial):
        return f"{serial[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase,k=2))}"
    
    def crear_vehiculo(self,Marca):
        serial_vehiculo = self.generar_SerialV(12)
        placa_V = self.generate_vehicle_licese(serial_vehiculo)
        return vehiculo(serial_vehiculo,placa_V, self.Informaciondelvehiculo[Marca])
    

class Application:
    def registrar_vehiculo(self,Marca: string):
        registro = Registro_vehiculo()
        return registro.crear_vehiculo(Marca)

app = Application()
automovil = app.registrar_vehiculo("Susuki swift")
automovil.print()

