from pygame_functions import makeSprite, moveSprite, showSprite, addSpriteImage, changeSpriteImage, hideSprite, killSprite
from constantes import PATHS
from .posicionable import Posicionable



class Dibujable(Posicionable):
    """
    Clase que da la propiedad a los elementos de ser dibujados, y la posibilidad de cambiar las imagenes y de poder 
    moverlos de posicion
    """
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

    def nueva_imagen(self, file):
        killSprite(self.sprite)
        self.nombeArchivo = file
        self.sprite = makeSprite(PATHS.PATH_IMAGENES + self.nombeArchivo)

    def mover(self):

        moveSprite(self.sprite, self.posicionX, self.posicionY)
        self._al_mover()

    def _al_dibujar(self):
        pass

    def _al_mover(self):
        pass