"""
Chain of Responsibility es un patrón de diseño de comportamiento que te permite pasar solicitudes a lo largo de una
cadena de manejadores. Al recibir una solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador
de la cadena
"""
from abc import ABC, abstractmethod


class Buy:
    def __init__(self):
        self._amount: int = 0

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        self.amount = amount


class Approved(ABC):

    def __init__(self):
        self.next = None

    def add_next(self, appreved: 'Approved') -> None:
        self.next = appreved

    @abstractmethod
    def process(self, buy: 'Buy') -> None: ...


class Buyer(Approved):

    def process(self, buy: 'Buy') -> None:
        if buy.amount < 100:
            print(f'Buyer | amount < 100: {buy.amount}')
        else:
            self.next.process(buy=buy)


class Manager(Approved):

    def process(self, buy: 'Buy') -> None:
        if buy.amount < 1000:
            print(f'Manager | amount < 1000: {buy.amount}')
        else:
            self.next.process(buy=buy)


class Director(Approved):

    def process(self, buy: 'Buy') -> None:
        print(f'Director | amount > 999: {buy.amount}')


def code_example_1():
    buyer = Buyer()
    manager = Manager()
    director = Director()

    manager.add_next(director)
    buyer.add_next(manager)

    buy = Buy

    print('amount: 50')
    buy.amount = 50
    buyer.process(buy)

    print('amount: 500')
    buy.amount = 500
    buyer.process(buy)

    print('amount: 5000')
    buy.amount = 5000
    buyer.process(buy)


def code_example_2():
    buyer = Buyer()
    manager = Manager()

    buyer.add_next(manager)

    buy = Buy

    print('amount: 50')
    buy.amount = 50
    buyer.process(buy)

    print('amount: 500')
    buy.amount = 500
    buyer.process(buy)

    print('amount: 5000')
    buy.amount = 5000
    buyer.process(buy)


if __name__ == '__main__':
    code_example_1()


"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None
    
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)

def client_code(handler: Handler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")
    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
"""