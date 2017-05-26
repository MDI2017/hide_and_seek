from .button import Button
from .datos_jugador import GrillaJugador
from constantes import SEPARACIONES


class SettingPartida:

    def __init__(self):
        self.jugadores = []
        self.grillas = [GrillaJugador(250, 100), GrillaJugador(250, 200)]

    def mostrar_pantalla_sentting(self):
        for grilla in self.grillas:
            grilla.dibujar_grilla()
