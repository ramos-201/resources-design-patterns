"""
Adapter es un patrón de diseño estructural que permite la colaboración entre objetos con interfaces incompatibles.
"""
from abc import abstractmethod, ABC


class Guitar(ABC):
    @abstractmethod
    def turn_on(self) -> None: ...

    @abstractmethod
    def turn_off(self) -> None: ...


class ElectricGuitar(Guitar):
    # Target
    def turn_on(self) -> None:
        print(f"{self.__class__.__name__} | Gitarra encendida")

    def turn_off(self) -> None:
        print(f"{self.__class__.__name__} | Gitarra apagada")


class AcousticGuitar:
    # A adaptar
    def play(self) -> None:
        print(f"{self.__class__.__name__} | Tocar la guitarra")

    def stop_playing(self) -> None:
        print(f"{self.__class__.__name__} | Dejar de tocar la guitarra")


class ElectroAcousticGuitar(Guitar):
    # Adapter
    def turn_on(self) -> None:
        AcousticGuitar().play()

    def turn_off(self) -> None:
        AcousticGuitar().stop_playing()


def code_client(guitar: Guitar):
    guitar.turn_on()
    guitar.turn_off()


if __name__ == "__main__":
    code_client(guitar=ElectricGuitar())
    code_client(guitar=ElectroAcousticGuitar())
