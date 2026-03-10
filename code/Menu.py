import pygame
from pygame import window


class Menu:
    def __init__(self):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.surf.get_rect(left=0, top=0)

    def Run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()
        pass
