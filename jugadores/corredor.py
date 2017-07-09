from gui.ficha import Ficha
from .jugador import Jugador


class Corredor(Jugador):
    """
    Clase que crea a jugador corredor, le asigna un nombre, un avatar y crea la ficha
    """

    def __init__(self, nombre, avatar):
        super().__init__(nombre, avatar)
        if self.avatar is None:
            self.avatar = "no_avatar.png"

    def crear_ficha(self, casillero):
        casillero.esta_ocupado = True
        self.ficha = Ficha(casillero, nombre_archivo=self.avatar)
        self.ficha.dibujar()

    def set_position(self, numero_jugador):

        if numero_jugador >= 2:
            numero_jugador += 6
        return [numero_jugador, 10]
