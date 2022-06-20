from dis import dis
import pygame as pg

from arkanoid import ANCHO, ALTO
from arkanoid.escenas import Portada, Partida, HallOfFane

class Arkanoid:
    def __init__(self):
        print("arranca el juego")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid BZ version")
        icon = pg.image.load("resources/images/ball1.png")
        pg.display.set_icon(icon)

        self.escenas = [
            Portada(self.display),
            Partida(self.display),
            HallOfFane(self.display),
        ]

    def jugar (self):
        """Este es el bucle principal"""
        for escena in self.escenas:
            escena.bucle_principal()



