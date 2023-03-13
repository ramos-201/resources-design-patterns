"""
Decorator es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos
dentro de objetos encapsuladores especiales que contienen estas funcionalidades.
"""
from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def compute_damage(self, received_attack: int) -> int: pass


class ConcreteEnemy(Enemy):
    def compute_damage(self, received_attack: int) -> int:
        return 100


class EnemyDecorator(Enemy):

    def __init__(self, enemy_to_decorator: Enemy):
        self.decorator_enemy: Enemy = enemy_to_decorator

    def compute_damage(self, received_attack: int) -> int: ...


class ConcreteEnemyDecorator(EnemyDecorator):
    def compute_damage(self, received_attack: int):
        self.decorator_enemy.compute_damage(received_attack=received_attack)


if __name__ == "__main__":
    print("Enemigo sin armadura")
    enemy = ConcreteEnemy()

    print("Enemigo con armadura")
    enemy = ConcreteEnemyDecorator(enemy_to_decorator=enemy)

    print("Enemigo con armadura x2")
    enemy = ConcreteEnemyDecorator(enemy_to_decorator=enemy)
