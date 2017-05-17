from pygame import *


class Jugador():
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero


class Ficha(Jugador):
    ficha1 = image.load("Images/ficha-roja.png").convert_alpha()

    def __init__(self, nombre, ficha):
        Jugador.__init__(self, nombre)
        self.ficha1 = ficha


class Partida:
    def __init__(self, nombre, numero, es_corredor):
        self.nombre = nombre
        self.numero = numero
        self.es_corredor = es_corredor
        self.participan = Jugador()
        self.tiene = Turno()
        self.tiene = Dado()
        self.tiene = Tablero()
        self.jugadores = []

    def crearJugador(self, avatar):
        self.avatar = avatar
        self.participan.Jugador.nombre = self.nombre
        self.numero = self.participan.Jugador.numero
        if self.es_corredor==True:
            return self.participan.Jugador.Corredor
        else:
            return self.participan.Jugador.Contador
