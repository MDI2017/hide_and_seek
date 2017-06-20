from pygame_functions import*
from gui.dibujable import Dibujable
from gui.button import Button
from constantes import*


class Avatars:
    """
    Clase encargada de la seleccion de avatars
    """
    def __init__(self, seleccionado):
        # Definicion de fondo y Sprites
        self.fondo = Dibujable(0, 0, 'overlay.png')
        self.fondo.dibujar()
        self.xpos = 25
        self.ypos = 600
        self.nomAvatar = None
        self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5,\
            self.sprite6, self.sprite7, self.sprite8, self.sprite9 = \
            None, None, None, None, None, None, None, None, None
        self.lista = [self.sprite1, self.sprite2, self.sprite3, self.sprite4, self.sprite5,
                      self.sprite6, self.sprite7, self.sprite8, self.sprite9]
        self.seleccionado = seleccionado
        self.titulo = makeLabel('Avatars:', 36, 30, 520, 'white')
        showLabel(self.titulo)

        # Dibujado de Sprites
        for i in range(0, 9):
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
                if self.lista[0].click_elemento(self.mouseAction):
                    if self.seleccionado[0]:
                        self.lista[0].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[0]:
                        self.nomAvatar = "avatar1.png"
                        self.seleccionado[0] = True
                        break
                if self.lista[1].click_elemento(self.mouseAction):
                    if self.seleccionado[1]:
                        self.lista[1].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[1]:
                        self.nomAvatar = "avatar2.png"
                        self.seleccionado[1] = True
                        break
                if self.lista[2].click_elemento(self.mouseAction):
                    if self.seleccionado[2]:
                        self.lista[2].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[2]:
                        self.nomAvatar = "avatar3.png"
                        self.seleccionado[2] = True
                        break
                if self.lista[3].click_elemento(self.mouseAction):
                    if self.seleccionado[3]:
                        self.lista[3].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[3]:
                        self.nomAvatar = "avatar4.png"
                        self.seleccionado[3] = True
                        break
                if self.lista[4].click_elemento(self.mouseAction):
                    if self.seleccionado[4]:
                        self.lista[4].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[4]:
                        self.nomAvatar = "avatar5.png"
                        self.seleccionado[4] = True
                        break
                if self.lista[5].click_elemento(self.mouseAction):
                    if self.seleccionado[5]:
                        self.lista[5].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[5]:
                        self.nomAvatar = "avatar6.png"
                        self.seleccionado[5] = True
                        break
                if self.lista[6].click_elemento(self.mouseAction):
                    if self.seleccionado[6]:
                        self.lista[6].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[6]:
                        self.nomAvatar = "avatar7.png"
                        self.seleccionado[6] = True
                        break
                if self.lista[7].click_elemento(self.mouseAction):
                    if self.seleccionado[7]:
                        self.lista[7].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[7]:
                        self.nomAvatar = "avatar8.png"
                        self.seleccionado[7] = True
                        break
                if self.lista[8].click_elemento(self.mouseAction):
                    if self.seleccionado[8]:
                        self.lista[8].cambiar_imagen(ESTADOS_BOTONES.PRESIONADO)
                    if not self.seleccionado[8]:
                        self.nomAvatar = "avatar9.png"
                        self.seleccionado[8] = True
                        break

        hideLabel(self.titulo)
        for i in self.lista:
            i.ocultar()

