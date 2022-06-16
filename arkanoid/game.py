import pygame
from arkanoid import ANCHO, ALTO


class Arkanoid:
    def __init__(self):
        print("arranca el juego")
        pygame.init()
        pygame.display.set_mode((ANCHO, ALTO))

    def jugar (self):
        """Este es el bucle principal"""
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pygame.display.flip()



