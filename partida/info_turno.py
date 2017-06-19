from jugadores.jugador import Jugador
from gui.dibujable import Dibujable
from pygame_functions import *


class Info_turno:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.cazador = None
        self.nombres = []
        self.avatars = []
        self._renderizar_sprites(jugadores)

    def _renderizar_sprites(self, jugadores):
        posY = 300
        jugador = []
        for numero_jugador, data_jugador in enumerate(jugadores):
            if data_jugador['es_cazador']:
                self.cazador = Jugador(data_jugador['nombre'], data_jugador['avatar'])
                self.cazador.nombre = makeLabel(self.cazador.nombre, 32, 620, posY)
                self.cazador.avatar = Dibujable(620, posY + 40, self.cazador.avatar)
            else:
                jugador.append(Jugador(data_jugador['nombre'], data_jugador['avatar']))
        for indice in jugador:
            print(indice.nombre)
            self.nombres.append(makeLabel(indice.nombre, 32, 620, posY))
            self.avatars.append(Dibujable(620, posY + 40, indice.avatar))

    def juagdor_actual(self, turno):
        if turno < len(self.jugadores)-1:
            showLabel(self.nombres[turno])
            self.avatars[turno].dibujar()
        else:
            showLabel(self.cazador.nombre)
            self.cazador.avatar.dibujar()

    def borrar(self, turno):
        if turno == 'cazador':
            hideLabel(self.cazador.nombre)
            self.cazador.avatar.ocultar()
        else:
            hideLabel(self.nombres[turno])
            self.avatars[turno].ocultar()
