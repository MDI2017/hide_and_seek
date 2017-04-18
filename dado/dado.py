import random
from pygame_functions import *

def dado():
    dadoImg = makeSprite("dado/dice1.png")
    addSpriteImage(dadoImg, "dado/dice2.png")
    addSpriteImage(dadoImg, "dado/dice3.png")
    addSpriteImage(dadoImg, "dado/dice4.png")
    addSpriteImage(dadoImg, "dado/dice5.png")
    addSpriteImage(dadoImg, "dado/dice6.png")
    moveSprite(dadoImg,670,100,True)
    showSprite(dadoImg)
    etiqueta = makeLabel("Movimientos: ",20,610,20,"black")
    showLabel(etiqueta)
    i = 0
    movimientos = 0
    while i < 6:
        changeSpriteImage(dadoImg, i)
        i += 1
        pause(100)
        if i == 6:
            i = 0
        if spriteClicked(dadoImg):
            movimientos = random.randint(1, 6)
            changeSpriteImage(dadoImg, movimientos - 1)
            break
    return movimientos
