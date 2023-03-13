"""
Composite es un patrón de diseño estructural que te permite componer objetos en estructuras de árbol y trabajar con esas
estructuras como si fueran objetos individuales.
"""
from abc import ABC, abstractmethod
from typing import List


class Entity(ABC):
    @abstractmethod
    def logic(self) -> None: ...


class FireLeftLeg(Entity):
    def logic(self) -> None:
        print(f"{self.__class__.__name__}")


class WaterRightLeg(Entity):
    def logic(self) -> None:
        print(f"{self.__class__.__name__}")


class OctopusMainBody(Entity):
    def logic(self) -> None:
        print(f"{self.__class__.__name__}")


class BigOctopusEnemy(Entity):
    enemy_parts: List[Entity] = []

    def __init__(self):
        self.enemy_parts.append(OctopusMainBody())
        self.enemy_parts.append(FireLeftLeg())
        self.enemy_parts.append(WaterRightLeg())

    def logic(self) -> None:
        for enemy_part in self.enemy_parts:
            enemy_part.logic()


def logic_a():
    OctopusMainBody()\
        .logic()

    FireLeftLeg()\
        .logic()

    WaterRightLeg()\
        .logic()


def logic_client():
    BigOctopusEnemy()\
        .logic()


if __name__ == '__main__':
    print("Logic A")
    logic_a()

    print("Logic composite")
    logic_client()
