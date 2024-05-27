import flet as ft

class MainWindow(ft.Container):
    def __init__(self, title: str):
        super().__init__(expand=True)
        self.__title = ft.Text(title)

    def build(self):
        return ft.Column(
                controls=[
                    self.__title,
                    ],
                )
