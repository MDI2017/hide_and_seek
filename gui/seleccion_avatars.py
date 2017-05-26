from pygame_functions import *
from constantes import *


class avatars:
    mouseAction = mousePressed()
    def __init__(self):
        screenSize(800, 400)
        setBackgroundColour(COLORES.BLANCO)
        self.xpos = 5
        self.numAvatar = None
        self.sprite1 = makeSprite("avatar1.png")
        self.sprite2 = makeSprite("avatar2.png")
        self.sprite3 = makeSprite("avatar3.png")
        self.sprite4 = makeSprite("avatar4.png")
        self.sprite5 = makeSprite("avatar5.png")
        self.lista = [self.sprite1,self.sprite2,self.sprite3,self.sprite4,self.sprite5]

        for avatar in range(0,5):
            moveSprite(self.lista[avatar], self.xpos ,15)
            showSprite(self.lista[avatar])
            self.xpos += 80
            pause(200)

        while True:
            if spriteClicked(self.sprite1):
                print('hola')
                self.numAvatar=0
                break
            if spriteClicked(self.sprite2):
                self.numAvatar=1
                break
            if spriteClicked(self.sprite3):
                self.numAvatar=2
                break
            if spriteClicked(self.sprite4):
                self.numAvatar=3
                pygame.quit()
            if spriteClicked(self.sprite5):
                self.numAvatar=4
                pygame.quit()





av = avatars()
print(av.numAvatar)

