from jugador import Jugador
from dado.dado import dado
from tablero.tablero import Tablero


class Partida():

    def __init__(self, array_jugadores):
        self.jugador = Jugador()
        # self.turno = Turno()  Clase Turno todavía no creada
        self.dado = dado()
        self.tablero = Tablero()
        self.jugadores = array_jugadores


