import random
from pygame_functions import *

class Dado():
    def __init__(self):
        self.dadoImg = makeSprite("images/dice1.png")
        addSpriteImage(self.dadoImg, "images/dice2.png")
        addSpriteImage(self.dadoImg, "images/dice3.png")
        addSpriteImage(self.dadoImg, "images/dice4.png")
        addSpriteImage(self.dadoImg, "images/dice5.png")
        addSpriteImage(self.dadoImg, "images/dice6.png")
        moveSprite(self.dadoImg, 670, 100, True)
        showSprite(self.dadoImg)
        etiqueta = makeLabel("Movimientos: ", 20, 610, 20, "black")
        showLabel(etiqueta)



    def tirarDado(self):
        pause(100)
        i = 0
        movimientos = 0
        while i < 6:
            changeSpriteImage(self.dadoImg, i)
            i += 1
            pause(100)
            if i == 6:
                i = 0
            if spriteClicked(self.dadoImg):
                movimientos = random.randint(1, 5)
                changeSpriteImage(self.dadoImg, movimientos )
                break
        return movimientos

