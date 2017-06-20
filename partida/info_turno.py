from jugadores.jugador import Jugador
from gui.dibujable import Dibujable
from pygame_functions import *


class Info_turno:
    """
    Clase que muestra cual es el turno actual, y muestra la cantidad de movimientos restantes del turno actual 
    
    """
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.cazador = None
        self.posX = 630
        self.posY = 400
        self.movimientos = None
        self.nombres = []
        self.avatars = []
        self._renderizar_sprites(jugadores)
        self.titulo = makeLabel('Turno actual: ', 34, self.posX-10, self.posY-55)

    def _renderizar_sprites(self, jugadores):

        jugador = []
        for numero_jugador, data_jugador in enumerate(jugadores):
            if data_jugador['es_cazador']:
                self.cazador = Jugador(data_jugador['nombre'], data_jugador['avatar'])
                self.cazador.nombre = makeLabel(self.cazador.nombre, 28, self.posX, self.posY)
                if self.cazador.avatar is None:
                    self.cazador.avatar = "no_avatar.png"
                self.cazador.avatar = Dibujable(self.posX, self.posY + 40, self.cazador.avatar)
            else:
                jugador.append(Jugador(data_jugador['nombre'], data_jugador['avatar']))
        for indice in jugador:
            print(indice.nombre)
            if indice.avatar is None:
                indice.avatar = "no_avatar.png"
            self.nombres.append(makeLabel(indice.nombre, 32, self.posX, self.posY))
            self.avatars.append(Dibujable(self.posX, self.posY + 40, indice.avatar))

    def jugador_actual(self, turno):
        drawRect(self.posX - 10, self.posY + 6, 2, 135, 'black')
        showLabel(self.titulo)
        if turno < len(self.jugadores)-1:
            showLabel(self.nombres[turno])
            self.avatars[turno].dibujar()
        else:
            showLabel(self.cazador.nombre)
            self.cazador.avatar.dibujar()

    def borrar(self, turno):
        hideLabel(self.titulo)
        if turno == 'cazador':
            hideLabel(self.cazador.nombre)
            self.cazador.avatar.ocultar()
        else:
            hideLabel(self.nombres[turno])
            self.avatars[turno].ocultar()

    def movim_restantes(self, movimientos):
        if self.movimientos is not None:
            hideLabel(self.movimientos)
        self.movimientos = makeLabel('Movimientos restantes: ' + str(movimientos+1), 24, self.posX, self.posY + 110)
        showLabel(self.movimientos)
