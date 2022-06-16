import pygame as pg

from arkanoid import ANCHO, ALTO


class Arkanoid:
    def __init__(self):
        print("arranca el juego")
        pg.init()
        pg.display.set_mode((ANCHO, ALTO))

    def jugar (self):
        """Este es el bucle principal"""
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pg.display.flip()



