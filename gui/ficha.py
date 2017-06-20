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

        if direccion == pygame.K_UP:
            if self.casillero[1] == 0:
                return False
            else:
                self.casillero[1] -= 1
        elif direccion == pygame.K_DOWN:
            if self.casillero[1] == 10:
                return False
            else:
                self.casillero[1] += 1
        elif direccion == pygame.K_RIGHT:
            if self.casillero[0] == 9:
                return False
            else:
                self.casillero[0] += 1
        elif direccion == pygame.K_LEFT:
            if self.casillero[0] == 0:
                return False
            else:
                self.casillero[0] -= 1
        self.mover(CASILLAS.LADO * self.casillero[0], CASILLAS.LADO * self.casillero[1])
        print("Casillero luego de moverse",self.casillero)

    def _al_mover(self):
        pass

    def _al_dibujar(self):
        pass
