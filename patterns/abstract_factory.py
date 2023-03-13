"""
Abstract Factory es un patrón de diseño creacional que resuelve el problema de crear familias enteras de productos sin
especificar sus clases concretas.
"""
from abc import abstractmethod, ABC
from typing import Union


class Object1:
    def method_o_1(self) -> None: ...


class Object2:
    def method_o_2(self) -> None: ...


class Map1(ABC):
    @abstractmethod
    def run_map_1(self) -> Union[Object1, Object2]: ...


class Map1Object1(Map1):
    def run_map_1(self) -> Object1: ...


class Map1Object2(Map1):
    def run_map_1(self) -> Object2: ...


class Map2(ABC):
    @abstractmethod
    def run_map_2(self) -> Union[Object1, Object2]: ...


class Map2Object1(Map2):
    def run_map_2(self) -> Object1: ...


class Map2Object2(Map2):
    def run_map_2(self) -> Object2: ...


class AbstractFactory(ABC):
    @abstractmethod
    def create_map_object(self) -> Union[Map1, Map2]: ...


class Map1Factory(AbstractFactory):
    def create_map_object(self) -> Map1: ...


class Map2Factory(AbstractFactory):
    def create_map_object(self) -> Map2: ...


def create_object(map_factory: Union[Map1Factory, Map2Factory]) -> None:
    map_factory.create_map_object()


if __name__ == "__main__":
    print("code map1")
    create_object(map_factory=Map1Factory())

    print("code map2")
    create_object(map_factory=Map2Factory())
