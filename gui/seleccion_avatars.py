from pygame_functions import *
from gui.button import Button
import pygame


class Avatars:
    def __init__(self):
        # Definicion de fondo, atributos a usar y Sprites
        self.xpos = 25
        self.ypos = 425
        self.numAvatar = None
        self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5 = None, None, None, None, None
        self.lista = [self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5]

        # Titulos de categoria Sprite
        self.titulo = makeLabel('Avatars:', 36, 100, 350, 'black')
        showLabel(self.titulo)

        # Dibujado de Sprites
        for i in range(0, 5):
            self.lista[i] = Button(self.xpos, self.ypos, "avatar" + str(i + 1) + ".png")
            self.lista[i].dibujar()
            self.xpos += 80

        # Asignacion de funcionalidad clickeable
       #while True:
            #if spriteClicked(self.sprite1):
                #self.numAvatar = 0
                #break
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
