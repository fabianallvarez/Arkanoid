import pygame as pg

from arkanoid import ANCHO, ALTO


class Arkanoid:
    def __init__(self):
        print("arranca el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid BZ version")
        icon = pg.image.load("resources/images/ball1.png")
        pg.display.set_icon(icon)
        
    def jugar (self):
        """Este es el bucle principal"""
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.display.fill((99, 99, 99))
            pg.display.flip()



