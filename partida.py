from .jugador import Jugador
from .dado.dado import dado
from .tablero.tablero import Tablero

class Partida(object):

    jugadores={"Nombre", "Numero"}

    def __init__(self, jugadores):
        self.jugador = Jugador()
        self.turno = Turno()
        self.dado = dado()
        self.tablero = Tablero()
        self.jugadores=jugadores
        self.jugadores["Nombre"]=self.jugador.nombre
        self.jugadores["Numero"]=self.jugador.numero


