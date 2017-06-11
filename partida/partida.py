import pygame

from gui.button import Button
from jugadores.cazador import Cazador
from jugadores.corredor import Corredor
from pygame_functions import clearShapes
from tablero.tablero import Tablero


class Partida():
    def __init__(self):
        # self.turno = Turno()  Clase Turno todavía no creada
        # self.dado = dado()
        self.tablero = Tablero()
        self.corredores = []
        self.cazador = None
        self.boton_atras = Button(600, 100, "boton_iniciar_partida_habilitado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_presionado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_desactivado.png")

    def iniciar_partida(self, jugadores):
        self.tablero.dibujarTablero()
        self.boton_atras.dibujar()
        self._crear_jugadores(jugadores)
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
        enter_presionado = False

        while en_partida:
            mouseAction = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseAction = pygame.mouse.get_pos()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print('preciono enter')
                        self._enter_presionado()

            if mouseAction:
                if self.boton_atras.dibujado and self.boton_atras.click_elemento(mouseAction):
                    self.tablero.renderizado = False
                    clearShapes()
                    self.boton_atras.ocultar()
                    en_partida = False

    def _enter_presionado(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        print('libero enter')
                        return