from pygame_functions import makeSprite, moveSprite, showSprite, addSpriteImage, changeSpriteImage
from constantes import PATHS
from .posicionable import Posicionable


class Dibujable(Posicionable):
    def __init__(self, posicion_x, posicion_y, nombre_archivo, ancho=None, alto=None,  dibujado=False):
        super().__init__(posicion_x, posicion_y, ancho, alto)
        self.nombeArchivo = nombre_archivo
        self.dibujado = dibujado
        self.sprite = None
        self.spriteRect = None

    def dibujar(self):
        self.sprite = makeSprite(PATHS.PATH_IMAGENES + self.nombeArchivo)
        moveSprite(self.sprite, self.posicionX, self.posicionY)
        self.spriteRect = self.sprite.rect
        showSprite(self.sprite)
        self.dibujado = True

    def agregar_imagen(self, nombre_archivo):
        addSpriteImage(self.sprite, PATHS.PATH_IMAGENES + nombre_archivo)

    def cambiar_imagen(self, indice):
        print(indice)
        changeSpriteImage(self.sprite, indice)