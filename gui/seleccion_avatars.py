from pygame_functions import *
from constantes import *
from gui.clickeable import Clickeable


class avatars:
    mouseAction = mousePressed()

    def __init__(self):
        screenSize(800, 400)
        setBackgroundColour(COLORES.BLANCO)
        self.xposCaza = 25
        self.xposCont = 25
        self.yposCaza = 60
        self.yposCont = 225
        self.numAvatar = None
        self.sprite1 = makeSprite("avatar1.png")
        self.sprite2 = makeSprite("avatar2.png")
        self.sprite3 = makeSprite("avatar3.png")
        self.sprite4 = makeSprite("avatar4.png")
        self.sprite5 = makeSprite("avatar5.png")
        self.lista = [self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5]

        self.cazadores = makeLabel('Cazadores:', 36, 25, 5)
        showLabel(self.cazadores)

        for avatar in range(0, 2):
            moveSprite(self.lista[avatar], self.xposCaza, self.yposCaza)
            showSprite(self.lista[avatar])
            self.xposCaza += 80

        self.contadores = makeLabel('Contadores:', 36, 25, 170)
        showLabel(self.contadores)

        for avatar in range(2, 5):
            moveSprite(self.lista[avatar], self.xposCont, self.yposCont)
            showSprite(self.lista[avatar])
            self.xposCont += 80

        while True:
            if Clickeable().click_elemento(mousePressed(), self.sprite1.rect[0], self.sprite1.rect[1],
                                           self.sprite1.rect[2], self.sprite1.rect[3]):
                self.numAvatar = 0
                break
            if Clickeable().click_elemento(mousePressed(), self.sprite2.rect[0], self.sprite2.rect[1],
                                           self.sprite2.rect[2], self.sprite2.rect[3]):
                self.numAvatar = 1
                break
            if Clickeable().click_elemento(mousePressed(), self.sprite3.rect[0], self.sprite3.rect[1],
                                           self.sprite3.rect[2], self.sprite3.rect[3]):
                self.numAvatar = 2
                break
            if Clickeable().click_elemento(mousePressed(), self.sprite4.rect[0], self.sprite4.rect[1],
                                           self.sprite4.rect[2], self.sprite4.rect[3]):
                self.numAvatar = 3
                break
            if Clickeable().click_elemento(mousePressed(), self.sprite5.rect[0], self.sprite5.rect[1],
                                           self.sprite5.rect[2], self.sprite5.rect[3]):
                self.numAvatar = 4
                break


av = avatars()
print(av.numAvatar)