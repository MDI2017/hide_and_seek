from pygame_functions import *
from gui.button import Button
from constantes import *


class Avatars(Button):
    def __init__(self, seleccionado):
        # Definicion de fondo, atributos a usar y Sprites
        self.xpos = 25
        self.ypos = 600
        self.nomAvatar = None
        self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5 = None, None, None, None, None
        self.lista = [self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5]
        self.seleccionado = seleccionado

        # Titulos de categoria Sprite
        self.titulo = makeLabel('Avatars:', 36, 30, 480, 'black')
        showLabel(self.titulo)

        # Dibujado de Sprites
        for i in range(0, 5):
            self.lista[i] = Button(self.xpos, self.ypos, "avatar" + str(i + 1) + ".png")
            self.lista[i].agregar_imagen("avatar" + str(i + 1) + "_presionado.png")
            self.lista[i].dibujar()
            if seleccionado[i]:
                self.lista[i].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
            self.xpos += 80

        # Asignacion de funcionalidad clickeable
        while True:
            self.mouseAction = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseAction = pygame.mouse.get_pos()

            if self.mouseAction:
                if self.lista[0].click_elemento(self.mouseAction) & (not self.seleccionado[0]):
                    self.nomAvatar = "avatar1.png"
                    self.seleccionado[0] = True
                    break
                if self.lista[1].click_elemento(self.mouseAction) & (not self.seleccionado[1]):
                    self.nomAvatar = "avatar2.png"
                    self.seleccionado[1] = True
                    break
                if self.lista[2].click_elemento(self.mouseAction) & (not self.seleccionado[2]):
                    self.nomAvatar = "avatar3.png"
                    self.seleccionado[2] = True
                    break
                if self.lista[3].click_elemento(self.mouseAction) & (not self.seleccionado[3]):
                    self.nomAvatar = "avatar4.png"
                    self.seleccionado[3] = True
                    break
                if self.lista[4].click_elemento(self.mouseAction) & (not self.seleccionado[4]):
                    self.nomAvatar = "avatar5.png"
                    self.seleccionado[4] = True
                    break
        hideLabel(self.titulo)
        for i in range(0, 5):
            self.lista[i].ocultar()
