"""
Singleton es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la
vez que proporciona un punto de acceso global a dicha instancia.
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass1(Singleton):
    ...


class MyClass2:
    ...


if __name__ == '__main__':
    my_class_1_instance_1 = MyClass1()
    my_class_1_instance_2 = MyClass1()
    my_class_2 = MyClass2()

    print(isinstance(my_class_1_instance_1, Singleton))
    print(my_class_1_instance_1 == my_class_1_instance_2)
    print(isinstance(my_class_2, Singleton))
