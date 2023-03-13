"""
Bridge es un patrón de diseño estructural que divide la lógica de negocio o una clase muy grande en jerarquías de clases
separadas que se pueden desarrollar independientemente.
"""
from abc import abstractmethod, ABC
from typing import List


content = [
    {
        'type': 'video',
        'title': 'title 1',
        'image': 'imagen 1'
    },
    {
        'type': 'stream',
        'title': 'title 2',
        'image': 'imagen 2',
        'viewers': '1'
    }
]


class Video:
    def __init__(self):
        self.title: str = content[0]['title']
        self.imagen: str = content[0]['imagen']


class Stream:
    def __init__(self):
        self.title: str = content[1]['title']
        self.imagen: str = content[1]['imagen']
        self.viewers: str = content[1]['viewers']


class IViewModel(ABC):
    @abstractmethod
    def title(self) -> str: ...

    @abstractmethod
    def image(self) -> str: ...


class VideoViewModel(IViewModel):
    def __init__(self):
        self.video: Video = Video()

    def title(self) -> str:
        return self.video.title

    def image(self) -> str:
        return self.video.imagen


class StreamViewModel(IViewModel):
    def __init__(self):
        self.stream: Stream = Stream()

    def title(self) -> str:
        return f'{self.stream.title} : {self.stream.viewers}'

    def image(self) -> str:
        return self.stream.imagen


class ListItemView(ABC):

    def __init__(self, view_model):
        self.view_model: IViewModel = view_model

    @abstractmethod
    def render(self) -> None: ...


class WithThumbnailListIView(ListItemView):
    def render(self) -> None:
        print(self.view_model.image())
        print(self.view_model.title())


class JustTextListItemView(ListItemView):
    def render(self) -> None:
        print(self.view_model.title())


def code_example_implementation():
    list_views: List[ListItemView] = []

    for item in content:
        if item['type'] == 'video':
            list_views.append(WithThumbnailListIView(VideoViewModel()))
            list_views.append(JustTextListItemView(VideoViewModel()))
        elif item['type'] == 'stream':
            list_views.append(WithThumbnailListIView(StreamViewModel()))
            list_views.append(JustTextListItemView(StreamViewModel()))

    for view in list_views:
        view.render()
