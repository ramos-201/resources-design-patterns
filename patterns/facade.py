"""
Facade es un patrón de diseño estructural que proporciona una interfaz simplificada a una biblioteca, un framework o
cualquier otro grupo complejo de clases.
"""
from typing import List


class Subsystem1:
    def operation1(self) -> str:
        return f"{self.__class__.__name__} | operation_1"

    def operation_n(self):
        return f"{self.__class__.__name__} | operation_n"


class Subsystem2:
    def operation1(self):
        return f"{self.__class__.__name__} | operation_1"

    def operation_z(self):
        return f"{self.__class__.__name__} | operation_z"


class Facade:
    def __init__(self, sub_system_1: Subsystem1, sub_system_2: Subsystem2):
        self.sub_system_1 = sub_system_1 or Subsystem1()
        self.sub_system_2 = sub_system_2 or Subsystem2()

    def operation(self) -> List[str]:
        return ["facade initializes subsystem: ",
                self.sub_system_1.operation1(),
                self.sub_system_2.operation1(),
                "Facade orders subsystem to perform actions :",
                self.sub_system_1.operation_n(),
                self.sub_system_2.operation_z()]


def client(facade: Facade) -> None:
    print(facade.operation())


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(sub_system_1=subsystem1, sub_system_2=subsystem2)
    client(facade=facade)
