from jugadores.jugador import Jugador
from gui.dibujable import Dibujable
from pygame_functions import *


class InfoTurno:
    """
    Clase que muestra cual es el turno actual, y muestra la cantidad de movimientos restantes del turno actual 
    
    """
    def __init__(self):
        self.cazador = None
        self.posX = 630
        self.posY = 400
        self.movimientos = None

        self.nombre_jugador = makeLabel("", 32, self.posX, self.posY)
        showLabel(self.nombre_jugador)
        drawRect(self.posX - 10, self.posY + 6, 2, 135, 'black')
        self.titulo = makeLabel('Turno actual: ', 34, self.posX-10, self.posY-55)
        showLabel(self.titulo)

        self.avatar = None

    def jugador_actual(self, jugador):
        changeLabel(self.nombre_jugador, jugador.nombre)
        self._renderizar_sprites(jugador.avatar)

    def _renderizar_sprites(self, file):

        if self.avatar:
            self.avatar.nueva_imagen(file)
        else:
            self.avatar = Dibujable(self.posX, self.posY + 40, file)

        self.avatar.dibujar()

    def movim_restantes(self, movimientos):
        if self.movimientos is not None:
            hideLabel(self.movimientos)
        self.movimientos = makeLabel('Movimientos restantes: ' + str(movimientos), 24, self.posX, self.posY + 110)
        showLabel(self.movimientos)
