class ReproductorDVD:
    def encender(self) -> None:
        print("DVD encendido")

    def reproducir(self, pelicula: str) -> None:
        print(f"Reproduciendo '{pelicula}'")


class Proyector:
    def encender(self) -> None:
        print("Proyector encendido")

    def modo_panoramico(self) -> None:
        print("Proyector en modo panoramico")


class Luces:
    def atenuar(self, nivel: int) -> None:
        print(f"Luces atenuadas al {nivel}%")


class CineEnCasaFacade:
    """Oculta la complejidad de coordinar varios subsistemas."""

    def __init__(self) -> None:
        self.dvd = ReproductorDVD()
        self.proyector = Proyector()
        self.luces = Luces()

    def ver_pelicula(self, pelicula: str) -> None:
        print("\n--- Preparando la experiencia de cine en casa ---")
        self.luces.atenuar(10)
        self.proyector.encender()
        self.proyector.modo_panoramico()
        self.dvd.encender()
        self.dvd.reproducir(pelicula)


def main() -> None:
    cine = CineEnCasaFacade()
    cine.ver_pelicula("Inception")


if __name__ == "__main__":
    main()

