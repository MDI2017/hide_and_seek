import random
from pygame_functions import *
from gui.dibujable import Dibujable
from gui.clickeable import Clickeable

class Dado():
    """
    Clase que crea y dibuja el dado, nos da la posibilidad de poder tirarlo y que nos de un resultado aleatorio dentro de las 6
    posibilidades
    """
    def __init__(self):
        self.dadoImg = makeSprite("images/dice1.png")
        addSpriteImage(self.dadoImg, "images/dice2.png")
        addSpriteImage(self.dadoImg, "images/dice3.png")
        addSpriteImage(self.dadoImg, "images/dice4.png")
        addSpriteImage(self.dadoImg, "images/dice5.png")
        addSpriteImage(self.dadoImg, "images/dice6.png")
        moveSprite(self.dadoImg, 670, 80, True)
        showSprite(self.dadoImg)

class Dado(Clickeable, Dibujable):

    def __init__(self, posicion_x=670, posicion_y=100, nombre_archivo="dice1.png",
                 ancho=None, alto=None, dibujado=False):
        super().__init__(posicion_x, posicion_y, nombre_archivo)

    def _al_liberar_click(self):
        self._tirar_dado()

    # def _clickeado(self):
    #     return super()._clickeado()

    # def _al_clickear(self):
    #     super()._al_clickear()

    def _tirar_dado(self):
        pause(100)
        i = 0
        movimientos = 0
        while i < 6:
            pause(100)
            if spriteClicked(self.dadoImg):
                while i < 6:
                    changeSpriteImage(self.dadoImg, i)
                    i += 1
                    pause(100)
                    if i == 6:
                        i = 0
                    if spriteClicked(self.dadoImg):
                        movimientos = random.randint(1, 5)
                        changeSpriteImage(self.dadoImg, movimientos)
                        break
                break
        return movimientos
