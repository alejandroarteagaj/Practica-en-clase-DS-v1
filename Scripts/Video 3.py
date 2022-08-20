from ast import Or
import string
import random
from typing import List, Callable


def Generar_identificador(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class Tickete_soporte:

    def __init__(self, Cliente, inconveniente):
        self.identificacion = Generar_identificador()
        self.Cliente = Cliente
        self.inconveniente = inconveniente


def Ordenamiento_fifo(list: List[Tickete_soporte]) -> List[Tickete_soporte]:
    return list.copy()


def Ordenamiento_filo(list: List[Tickete_soporte]) -> List[Tickete_soporte]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def Ordenamiento_random(list: List[Tickete_soporte]) -> List[Tickete_soporte]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


def Ordenamiento_Vacio(list: List[Tickete_soporte]) -> List[Tickete_soporte]:
    return []


class Servicio_cliente:

    def __init__(self):
        self.ticketes = []

    def Crear_tiquete(self, cliente, inconveniente):
        self.ticketes.append(Tickete_soporte(cliente, inconveniente))

    def Procesar_tiquetes(self, Ordenamiento: Callable[[List[Tickete_soporte]], List[Tickete_soporte]]):
        
        lista_tiquete = Ordenamiento(self.ticketes)

        if len(lista_tiquete) == 0:
            print("No hay tiquetes para procesar, buen trabajo maquina!")
            return

        for tickete in lista_tiquete:
            self.Procesar_tiquete(tickete)

    def Procesar_tiquete(self, tickete: Tickete_soporte):
        print("==================================")
        print(f"Numero del tiquete procesado : {tickete.identificacion}")
        print(f"Cliente: {tickete.Cliente}")
        print(f"Inconveniente: {tickete.inconveniente}")
        print("==================================")



app = Servicio_cliente()


app.Crear_tiquete("Sara betancourt","No me prende la luz del computador")
app.Crear_tiquete("Orlando valencia", "El teclado no me funciona")
app.Crear_tiquete("Laura villegas","Se partio un pedazo del ventilador y suena raro")
app.Procesar_tiquetes(Ordenamiento_random)