"""
Factory method es un patrón de diseño creacional que resuelve el problema de crear objetos de producto sin especificar
sus clases concretas.
"""
from abc import abstractmethod, ABC


class Entity(ABC):
    @abstractmethod
    def run(self) -> None: ...


class Boo(Entity):
    def run(self) -> None: ...


class Koopa(Entity):
    def run(self) -> None: ...


class Goomba(Entity):
    def run(self) -> None: ...


class EnemyFactory(ABC):
    @abstractmethod
    def create_enemy(self) -> Entity: ...


class BooEnemyFactory(EnemyFactory):
    def create_enemy(self) -> Entity: ...


class KoopaEnemyFactory(EnemyFactory):
    def create_enemy(self) -> Entity: ...


class GoombaEnemyFactory(EnemyFactory):
    def create_enemy(self) -> Entity: ...


def code_map(enemy: EnemyFactory):
    print(f"Creating {enemy.__class__.__name__}")
    enemy.create_enemy()


if __name__ == '__main__':
    print("Map 1")
    code_map(enemy=GoombaEnemyFactory())

    print("Map 2")
    code_map(enemy=GoombaEnemyFactory())
    code_map(enemy=KoopaEnemyFactory())
