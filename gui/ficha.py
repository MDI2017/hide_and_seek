import pygame
from gui.dibujable import Dibujable
from constantes import CASILLAS


class Ficha(Dibujable):
    def __init__(self, casillero, nombre_archivo, ancho=60, alto=60, dibujado=False):
        super().__init__(0, 0, nombre_archivo=nombre_archivo, ancho=ancho, alto=alto, dibujado=dibujado)
        self.casillero = casillero
        self.posicionX = CASILLAS.LADO * self.casillero[0]
        self.posicionY = CASILLAS.LADO * self.casillero[1]

    def mover_ficha(self, direccion):
        print(self.casillero)
        if direccion == pygame.K_UP:
            self.casillero[1] -= 1
        elif direccion == pygame.K_DOWN:
            self.casillero[1] += 1
        elif direccion == pygame.K_RIGHT:
            self.casillero[0] += 1
        elif direccion == pygame.K_LEFT:
            self.casillero[0] -= 1
        self.mover(CASILLAS.LADO * self.casillero[0], CASILLAS.LADO * self.casillero[1])

    def _al_mover(self):
        pass

    def _al_dibujar(self):
        pass