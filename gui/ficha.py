import pygame
from gui.dibujable import Dibujable
from constantes import CASILLAS


class Ficha(Dibujable):
    """
    Clase que genera y proporciona el dibujo y las propiedades de la ficha 
    """

    def __init__(self, casillero, nombre_archivo, ancho=60, alto=60, dibujado=False):
        super().__init__(0, 0, nombre_archivo=nombre_archivo, ancho=ancho, alto=alto, dibujado=dibujado)
        self.casillero = casillero
        self.posicionX = CASILLAS.LADO * self.casillero.indice[CASILLAS.COLUMNA]
        self.posicionY = CASILLAS.LADO * self.casillero.indice[CASILLAS.FILA]
        self.piso_piedra_libre = False
        self.doble_turno = False
        self.movimientos = None

    def mover_ficha(self, nuevo_casillero):

        if self.movimientos == 0:
            return 0

        self.casillero.esta_ocupado = False
        self.casillero = nuevo_casillero

        self.posicionX = CASILLAS.LADO * self.casillero.indice[0]
        self.posicionY = CASILLAS.LADO * self.casillero.indice[1]

        self.casillero.esta_ocupado = True
        self.mover()
        self.movimientos -= 1

        return self.movimientos

    def _al_mover(self):
        pass

    def _al_dibujar(self):
        self.casillero.esta_ocupado = True
