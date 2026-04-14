from abc import ABC, abstractmethod


class EnchufeEuropeo(ABC):
    """Interfaz esperada por el cliente."""

    @abstractmethod
    def proveer_energia_220v(self) -> str:
        """Entrega energia en el formato que espera el cliente."""


class CargadorAmericano:
    """Clase existente con una interfaz incompatible."""

    def cargar_110v(self) -> str:
        return "Cargando dispositivo con 110V..."


class AdaptadorCorriente(EnchufeEuropeo):
    """Traduce la solicitud del cliente al objeto legacy."""

    def __init__(self, cargador_americano: CargadorAmericano) -> None:
        self.cargador = cargador_americano

    def proveer_energia_220v(self) -> str:
        print("Adaptando 220V a 110V de forma segura...")
        return self.cargador.cargar_110v()


def main() -> None:
    cargador_usa = CargadorAmericano()
    adaptador = AdaptadorCorriente(cargador_usa)

    print("Cliente conectado a un enchufe europeo.")
    resultado = adaptador.proveer_energia_220v()
    print(resultado)


if __name__ == "__main__":
    main()

