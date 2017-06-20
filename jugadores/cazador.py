from gui.ficha import Ficha
from .jugador import Jugador


class Cazador(Jugador):
    """
    Clase que crea al jugador cazador, se le asigna un nombre, un avatar y crea la ficha para poder introducirla al tablero
    """
    def __init__(self, nombre, avatar):
        super().__init__(nombre, avatar)
        if self.avatar is None:
            self.avatar = "no_avatar.png"
        self.crear_ficha([4, 11])

    def crear_ficha(self, casillero):
        self.ficha = Ficha(casillero, nombre_archivo=self.avatar)
        self.ficha.dibujar()
