from gui.ficha import Ficha
from .jugador import Jugador


class Cazador(Jugador):
    def __init__(self, nombre, avatar):
        super().__init__(nombre, avatar)
        if self.avatar is None:
            self.avatar = "no_avatar.png"
        self.crear_ficha([4, 11])

    def crear_ficha(self, casillero):
        self.ficha = Ficha(casillero, nombre_archivo=self.avatar)
        self.ficha.dibujar()
