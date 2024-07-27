import flet as ft

from time import sleep

from llama.client import ollama_client


class Chat(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        self.__canvas = ft.Column(expand=True, auto_scroll=True, scroll=True)
        self.__canvas_container = ft.Container(content=self.__canvas, expand=True)
        self.__textField = ft.TextField(label="Write a message", value="", expand=True)
        self.__send_button = ft.ElevatedButton(text="Send", icon=ft.icons.SEND, on_click=self.__send_button_on_click_event)
        self.__send_row = ft.Row(controls=[self.__textField, self.__send_button], expand=True)
        self.__send_row_container = ft.Container(content=self.__send_row, expand=True)
        self.__chat = ft.Column(controls=[self.__canvas_container, self.__send_row_container], expand=True)
        self.__ollama = ollama_client()

    def __get_ollama_response(self, message: str):
        return self.__ollama.ask_question(message)
    
    def __send_button_on_click_event(self, e: ft.ControlEvent):
        message = self.__textField.value
        self.__canvas.controls.append(
            ft.Container(
                content=ft.Text(message, size=20),
                bgcolor=ft.colors.GREEN_900,
                padding=10,
                border_radius=10
            )
        )
        self.__textField.value = ""
        self.__send_button.disabled = True
        self.update()
        response = self.__get_ollama_response(message)
        self.__canvas.controls.append(
            ft.Container(
                content=ft.Text(response, size=20),
                bgcolor=ft.colors.BLUE_900,
                padding=10,
                border_radius=10
            )
        )
        self.__send_button.disabled = False
        self.update()

    def build(self):
        return ft.Container(content=self.__chat, expand=True)
