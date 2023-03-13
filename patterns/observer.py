"""
Observer es un patrón de diseño de comportamiento que te permite definir un mecanismo de suscripción para notificar
a varios objetos sobre cualquier evento que le suceda al objeto que están observando.
"""
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self) -> None: ...


class Observable(ABC):
    @abstractmethod
    def attach(self, o: 'Observer') -> None: ...

    @abstractmethod
    def detach(self, o: 'Observer') -> None: ...

    @abstractmethod
    def notify(self) -> None: ...


class YoutubeChannel(Observable):

    def __init__(self):
        self.channel_subscribers: List['Observer'] = []
        self.last_video_posted = ''

    def attach(self, o: 'Observer') -> None:
        self.channel_subscribers.append(o)

    def detach(self, o: 'Observer') -> None: ...

    def notify(self) -> None:
        for suscriptor in self.channel_subscribers:
            suscriptor.update()

    def add_new_video(self, title: str):
        self.last_video_posted = title
        self.notify()
        print('adding video')


class Subscriber(Observer):
    def __init__(self, channel: 'Observable'):
        self.observable = channel

    def update(self) -> None:
        print(f'New video posted! {self.observable.last_video_posted}')


if __name__ == '__main__':
    channel = YoutubeChannel()
    s1 = Subscriber(channel=channel)
    s2 = Subscriber(channel=channel)

    channel.attach(s1)
    channel.attach(s2)

    channel.add_new_video(title='New video zzz')
