from pygame_functions import *
from constantes import *
from gui.clickeable import Clickeable


class avatars:
    mouseAction = mousePressed()

    def __init__(self):
        screenSize(800, 420)
        setBackgroundImage("wall.jpg")
        self.xposCaza = 25
        self.xposCont = 500
        self.yposCaza = 60
        self.yposCont = 60
        self.numAvatar = None
        self.sprite1 = makeSprite("avatar1.png")
        self.sprite2 = makeSprite("avatar2.png")
        self.sprite3 = makeSprite("avatar3.png")
        self.sprite4 = makeSprite("avatar4.png")
        self.sprite5 = makeSprite("avatar5.png")
        self.lista = [self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5]
        drawRect(360,60,1,320,'white')

        self.cazadores = makeLabel('Cazadores:', 36, 25, 5,'white')
        showLabel(self.cazadores)

        for avatar in range(0, 2):
            moveSprite(self.lista[avatar], self.xposCaza, self.yposCaza)
            showSprite(self.lista[avatar])
            self.xposCaza += 80

        self.contadores = makeLabel('Contadores:', 36, 500, 5,'white')
        showLabel(self.contadores)

        for avatar in range(2, 5):
            moveSprite(self.lista[avatar], self.xposCont, self.yposCont)
            showSprite(self.lista[avatar])
            self.xposCont += 80

        while True:
            if Clickeable().elemento_precionado(mousePressed(),
                                                self.sprite1.rect[0], self.sprite1.rect[1],
                                                self.sprite1.rect[2], self.sprite1.rect[3]):
                self.numAvatar = 0
                break
            if Clickeable().elemento_precionado(mousePressed(),
                                                self.sprite2.rect[0], self.sprite2.rect[1],
                                                self.sprite2.rect[2], self.sprite2.rect[3]):
                self.numAvatar = 1
                break
            if Clickeable().elemento_precionado(mousePressed(),
                                                self.sprite3.rect[0], self.sprite3.rect[1],
                                                self.sprite3.rect[2], self.sprite3.rect[3]):
                self.numAvatar = 2
                break
            if Clickeable().elemento_precionado(mousePressed(),
                                                self.sprite4.rect[0], self.sprite4.rect[1],
                                                self.sprite4.rect[2], self.sprite4.rect[3]):
                self.numAvatar = 3
                break
            if Clickeable().elemento_precionado(mousePressed(),
                                                self.sprite5.rect[0], self.sprite5.rect[1],
                                                self.sprite5.rect[2], self.sprite5.rect[3]):
                self.numAvatar = 4
                break


av = avatars()
print(av.numAvatar)
