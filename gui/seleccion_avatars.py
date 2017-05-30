from pygame_functions import *
from gui.clickeable import Clickeable
from gui.button import Button


class Avatars:

    def __init__(self):
        # Definicion de fondo, atributos a usar y Sprites
        screenSize(800, 420)
        setBackgroundImage("wall.jpg")
        self.xposCaza = 25
        self.xposCont = 500
        self.yposCaza = 60
        self.yposCont = 60
        self.numAvatar = None
        self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5 = None, None, None, None, None
        self.lista = [self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5]
        drawRect(360, 60, 1, 320, 'white')

        # Titulos de categoria Sprite
        self.cazadores = makeLabel('Cazadores', 36, 25, 5, 'white')
        showLabel(self.cazadores)

        self.contadores = makeLabel('Contadores', 36, 500, 5, 'white')
        showLabel(self.contadores)

        # Dibujado de Sprites
        for avatar in range(0, 2):
            self.lista[avatar] = Button(self.xposCaza, self.yposCaza, "avatar1.png")
            self.xposCaza += 80

        for avatar in range(2, 5):
            self.lista[avatar] = Button(self.xposCont, self.yposCont, "avatar1.png")
            self.xposCont += 80

        # Asignacion de funcionalidad clickeable
        # while True:
        #     if Clickeable().click_elemento():
        #         self.numAvatar = 0
        #         break
        #     if Clickeable().click_sprite(mousePressed(), self.sprite2.rect):
        #         self.numAvatar = 1
        #         break
        #     if Clickeable().click_sprite(mousePressed(), self.sprite3.rect):
        #         self.numAvatar = 2
        #         break
        #     if Clickeable().click_sprite(mousePressed(), self.sprite4.rect):
        #         self.numAvatar = 3
        #         break
        #     if Clickeable().click_sprite(mousePressed(), self.sprite5.rect):
        #         self.numAvatar = 4
        #         break


av = Avatars()
print(av.numAvatar)
print(av.sprite1.rect)

