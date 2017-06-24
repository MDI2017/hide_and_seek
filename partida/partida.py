import pygame

from gui.button import Button
from jugadores.cazador import Cazador
from jugadores.corredor import Corredor
from partida.info_turno import Info_turno
from pygame_functions import clearShapes
from tablero.tablero import Tablero
from partida.dado import Dado
from pygame_functions import *
from constantes import DIVISIONES, ZONAS, CASILLAS
from .turno import Turno


class Partida:
    """
    Clase encargada de dibujar el tablero, iniciar la partida, crear los jugadores (cazador y corredor/es), del 
    movimiento de las fichas durante cada turno y del cambio de turno.
    Esta clase es la que contiene las reglas del juego y la encargada de verificar cuando un jugador gano la partida
    
    """

    def __init__(self):
        # self.turno = Turno()  Clase Turno todavía no creada

        self.tablero = Tablero()
        self.corredores = []
        self.cazador = None
        self.boton_atras = Button(880, 680, "boton_iniciar_partida_habilitado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_presionado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_desactivado.png")
        self.turno = 0
        self.primer_turno = True
        self.linea_doble_turno = False
        self.dado = None
        self.info = None
        self.movimientos = 1000

    def iniciar_partida(self, jugadores):
        self.tablero.dibujarTablero()
        self.boton_atras.dibujar()
        self._crear_jugadores(jugadores)
        self.info = Info_turno(jugadores)
        self.dado = Dado(670, 100)
        self.dado.dibujar()
        self.info.jugador_actual(self.turno)
        self.info.movim_restantes(self.movimientos)
        print('turno jugador: ' + str(self.turno))
        self.__bucle_partida()

    def _crear_jugadores(self, jugadores):
        for numero_jugador, data_jugador in enumerate(jugadores):

            if data_jugador['es_cazador']:
                self.cazador = Cazador(data_jugador['nombre'], data_jugador['avatar'])
            else:
                print('corredor')
                corredor = Corredor(data_jugador['nombre'], data_jugador['avatar'])
                self.corredores.append(corredor)
                corredor.crear_ficha(len(self.corredores) - 1)

    def __bucle_partida(self):
        en_partida = True
        while en_partida:
            mouseAction = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseAction = pygame.mouse.get_pos()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self._enter_presionado()

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN \
                            or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self._arrow_presionado(event.key)

            if mouseAction:
                if self.boton_atras.dibujado and self.boton_atras.click_elemento(mouseAction):
                    self.tablero.renderizado = False
                    clearShapes()
                    self.cazador.ficha.ocultar()
                    for corredor in self.corredores:
                        corredor.ficha.ocultar()
                    self.boton_atras.ocultar()
                    self.info.borrar(self.turno)
                    hideLabel(self.info.movimientos)
                    self.dado.ocultar()
                    clearShapes()
                    en_partida = False

                if self.dado.dibujado and self.dado.click_elemento(mouseAction):
                    self.movimientos = self.dado.tirar_dado()
                    self.info.movim_restantes(self.movimientos)
                    pause(500)
                    self.dado.ocultar()

    def _enter_presionado(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.movimientos = 0
                        self.dado.dibujar()
                        self._fin_turno()
                        print('turno jugador ' + self._cambio_turno())
                        return

    def _arrow_presionado(self, tecla_precionada):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == tecla_precionada:
                        self._mover_ficha(tecla_precionada)
                        return

    def _mover_ficha(self, direccion):

        if self.turno == 'cazador':
            self.posicionCazadorX = self.cazador.ficha.casillero[0]
            self.posicionCazadorY = self.cazador.ficha.casillero[1]
            self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY].esta_ocupado = True
            if direccion == pygame.K_UP:
                if self.posicionCazadorY == 0:
                    return False
                if self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY].paredes[DIVISIONES.SUPERIOR]:
                    return False
                elif self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY - 1].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY - 1].esta_ocupado = True
            if direccion == pygame.K_DOWN:
                if self.posicionCazadorY == 10:
                    return False
                if self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY].paredes[DIVISIONES.INFERIOR]:
                    return False
                elif self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY + 1].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY + 1].esta_ocupado = True
            if direccion == pygame.K_RIGHT:
                if self.posicionCazadorX == 9:
                    return False
                if self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY].paredes[DIVISIONES.DERECHA]:
                    return False
                elif self.tablero.casilleros[self.posicionCazadorX + 1][self.posicionCazadorY].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCazadorX + 1][self.posicionCazadorY].esta_ocupado = True

            if direccion == pygame.K_LEFT:
                if self.posicionCazadorX == 0:
                    return False
                if self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY].paredes[DIVISIONES.IZQUIERDA]:
                    return False
                elif self.tablero.casilleros[self.posicionCazadorX - 1][self.posicionCazadorY].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCazadorX - 1][self.posicionCazadorY].esta_ocupado = True

            if self.movimientos > 0:
                self.movimientos -= 1
                self.info.movim_restantes(self.movimientos)
                self.tablero.casilleros[self.posicionCazadorX][self.posicionCazadorY].esta_ocupado = False
                self.cazador.ficha.mover_ficha(direccion)

            elif self.movimientos is 0 and self.cazador.ficha.doble_turno is True:
                self.dado.dibujar()

        else:
            self.posicionCorredorX = self.corredores[int(self.turno)].ficha.casillero[0]
            self.posicionCorredorY = self.corredores[int(self.turno)].ficha.casillero[1]
            self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].esta_ocupado = True
            if direccion == pygame.K_UP:
                if self.posicionCorredorY == 0:
                    return False
                if self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].paredes[DIVISIONES.SUPERIOR]:
                    return False
                elif self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY - 1].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY - 1].esta_ocupado = True
            if direccion == pygame.K_DOWN:
                if self.posicionCorredorY == 10:
                    return False
                if self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].paredes[DIVISIONES.INFERIOR]:
                    return False
                elif self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY + 1].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY + 1].esta_ocupado = True
            if direccion == pygame.K_RIGHT:
                if self.posicionCorredorX == 9:
                    return False
                if self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].paredes[DIVISIONES.DERECHA]:
                    return False
                elif self.tablero.casilleros[self.posicionCorredorX + 1][self.posicionCorredorY].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCorredorX + 1][self.posicionCorredorY].esta_ocupado = True
            if direccion == pygame.K_LEFT:
                if self.posicionCorredorX == 0:
                    return False
                if self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].paredes[
                    DIVISIONES.IZQUIERDA]:
                    return False
                if self.tablero.casilleros[self.posicionCorredorX - 1][self.posicionCorredorY].esta_ocupado:
                    return False
                else:
                    self.tablero.casilleros[self.posicionCorredorX - 1][self.posicionCorredorY].esta_ocupado = True

            if self.movimientos > 0:
                self.movimientos -= 1
                self.info.movim_restantes(self.movimientos)
                self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].esta_ocupado = False
                self.corredores[int(self.turno)].ficha.mover_ficha(direccion)

    def _cambio_turno(self):
        """
        Cambia de turno y saltea a cazador en la primera ronda.
        """
        self.info.borrar(self.turno)

        if self.turno == 'cazador':
            self.turno = 0
        else:
            self.turno += 1

        if self.primer_turno is True and self.turno is len(self.corredores):
            self.info.jugador_actual(0)
        else:
            self.info.jugador_actual(self.turno)

        self.info.movim_restantes(self.movimientos)

        if self.turno < len(self.corredores):
            return str(self.turno)
        else:
            if self.primer_turno is True:
                print(self.turno)
                self.turno = 0
                self.primer_turno = False
                return str(self.turno)
            else:
                self.turno = 'cazador'
                return self.turno

    def _chequear_zona(self, direccion):
        if direccion == pygame.K_DOWN:
            if self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].zona is ZONAS.PIEDRA_LIBRE:
                self.corredores[int(self.turno)].ficha.piso_piedra_libre = True
            if self.tablero.casilleros[self.posicionCorredorX][self.posicionCorredorY].zona is ZONAS.LIBERTAD and \
                            self.corredores[int(self.turno)].ficha.piso_piedra_libre is True:
                self.corredores.pop(int(self.turno))

    def _fin_turno(self):

        Turno(self.cazador, self.tablero).fin_turno()
