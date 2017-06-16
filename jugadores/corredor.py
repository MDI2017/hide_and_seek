from gui.ficha import Ficha
from .jugador import Jugador


class Corredor(Jugador):
    def __init__(self, nombre, avatar):
        super().__init__(nombre, avatar)
        if self.avatar is None:
            self.avatar = "no_avatar.png"

    def crear_ficha(self, numero_jugador):
        if numero_jugador >= 2:
            numero_jugador += 6
        casillero = [numero_jugador, 10]
        self.ficha = Ficha(casillero, nombre_archivo=self.avatar)
        self.ficha.dibujar()
