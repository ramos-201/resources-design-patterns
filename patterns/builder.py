"""
Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos
permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
"""
import typing as Self


class Pizza:
    def __init__(self):
        self.topping = None
        self.cheese = None
        self.sauce = None
        self.base = None

    def set_base(self, base) -> Self:
        self.base = base
        return self

    def set_sauce(self, sauce) -> Self:
        self.sauce = sauce
        return self

    def set_cheese(self, cheese) -> Self:
        self.cheese = cheese
        return self

    def set_topping(self, topping) -> Self:
        self.topping = topping
        return self

    def bake(self) -> None:
        print(self.__dict__)


if __name__ == "__main__":
    pepperoni = Pizza()

    pepperoni \
        .set_base('Whole wheat') \
        .set_sauce('Tomato basil') \
        .set_cheese('Smoked mozzarella')\
        .bake()
