import pygame
from code.Menu import Menu


class Game:
    def __init__(self):
        print('Setup start')
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

        print('Setup end')
    def Run(self):
        print('Start loop')
        while True:
            menu = Menu(self.window)
            menu.Run()
            pass

            #check for all events
            for event in pygame.event.get():
                if event==pygame.QUIT:
                    print('Quiting...')
                    pygame.quit()
                    quit()

