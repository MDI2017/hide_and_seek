from pygame_functions import makeSprite, moveSprite, showSprite, addSpriteImage, changeSpriteImage, hideSprite
from constantes import PATHS
from .posicionable import Posicionable


class Dibujable(Posicionable):
    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=None, alto=None,  dibujado=False):
        super().__init__(posicion_x, posicion_y, ancho, alto)
        self.nombeArchivo = nombre_archivo
        self.dibujado = dibujado
        self.sprite = makeSprite(PATHS.PATH_IMAGENES + self.nombeArchivo)
        self.spriteRect = None

    def dibujar(self):
        moveSprite(self.sprite, self.posicionX, self.posicionY)
        showSprite(self.sprite)
        self._al_dibujar()
        self.dibujado = True

    def agregar_imagen(self, nombre_archivo):
        addSpriteImage(self.sprite, PATHS.PATH_IMAGENES + nombre_archivo)

    def cambiar_imagen(self, indice):
        changeSpriteImage(self.sprite, indice)

    def ocultar(self):
        hideSprite(self.sprite)
        self.dibujado = False

    def mover(self, pos_x=None, pos_y=None):
        if pos_x:
            self.posicionX = pos_x
        if pos_y:
            self.posicionY = pos_y
        moveSprite(self.sprite, self.posicionX, self.posicionY)
        self._al_mover()

    def _al_dibujar(self):
        pass

    def _al_mover(self):
        pass