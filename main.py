from arkanoid import ANCHO, ALTO
from arkanoid.game import Arkanoid

if __name__ == "__main__":
    print(f"el tamaño de pantalla es {ANCHO} x {ALTO}")
    juego = Arkanoid()
    juego.jugar()