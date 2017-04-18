from pygame import *

class Jugador():
    def __init__(self, nombre):
        self.nombre=nombre




class Ficha(Jugador):
    ficha1= image.load("Images/ficha-roja.png").convert_alpha()
    def __init__(self, nombre, ficha):
        Jugador.__init__(self,nombre)
        self.ficha1=ficha
