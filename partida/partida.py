from jugador import Jugador
from dado.dado import dado
from tablero.tablero import Tablero
from gui.button import Button
import pygame
from pygame_functions import clearShapes


class Partida():
    def __init__(self):
        # self.turno = Turno()  Clase Turno todavía no creada
        # self.dado = dado()
        self.tablero = Tablero()
        self.jugadores = None
        self.boton_atras = Button(600, 100, "boton_iniciar_partida_habilitado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_presionado.png")
        self.boton_atras.agregar_imagen("boton_iniciar_partida_desactivado.png")

    def iniciar_partida(self, jugadores):
        self.tablero.dibujarTablero()
        self.boton_atras.dibujar()
        self.__bucle_partida()

    def __bucle_partida(self):

        en_partida = True

        while en_partida:
            mouseAction = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseAction = pygame.mouse.get_pos()

            if mouseAction:
                if self.boton_atras.dibujado and self.boton_atras.click_elemento(mouseAction):
                    self.tablero.renderizado = False
                    clearShapes()
                    self.boton_atras.ocultar()
                    en_partida = False
