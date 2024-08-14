import flet as ft
from gui.chat import Chat

class MainWindow(ft.Container):
    def __init__(self, title: str):
        super().__init__(expand=True)
        self.__title = ft.Text(title, size=50)
        self.__title_row = ft.Row(controls=[self.__title], alignment="center")
        self.__title_canvas = ft.Container(content=self.__title_row, alignment=ft.alignment.center)
        self.__chat = Chat()
        self.__main_window = ft.Column(controls=[self.__title_canvas, self.__chat], expand=True)
        self.content = self.__main_window
