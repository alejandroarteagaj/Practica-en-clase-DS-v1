from abc import ABC, abstractmethod
from calendar import c 
class conmutadores(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class consola(conmutadores):
    def turn_on(self):
        print("Consola: encendida ...")
    
    def turn_off(self):
        print("Consola: apagada ...")

class computador(conmutadores):
     def turn_on(self):
        print("Computador: encendido ...")
    
     def turn_off(self):
        print("Computador: apagado ...")


class breaker:
    def __init__(self,u:conmutadores):
        self.usuario = u
        self.on = False
    
    def press(self):
        if self.on:
            self.usuario.turn_off()
            self.on = False
        else:
            self.usuario.turn_on()
            self.on = True

c = consola()
comp = computador()
conmutar= breaker(comp)
conmutar.press()
conmutar.press()