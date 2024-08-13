import flet as ft

from time import sleep

from llama.client import ollama_client


class Chat(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        self.__canvas = ft.Column(expand=True, auto_scroll=True, scroll=True)
        self.__canvas_container = ft.Container(content=self.__canvas, expand=5)
        self.__textField = ft.TextField(label="Write a message", value="", expand=True)
        self.__send_button = ft.ElevatedButton(text="Send", icon=ft.icons.SEND, on_click=self.__send_button_on_click_event)
        self.__send_row = ft.Row(controls=[self.__textField, self.__send_button], expand=True)
        self.__send_row_container = ft.Container(content=self.__send_row, expand=1)
        self.__chat = ft.Column(controls=[self.__canvas_container, self.__send_row_container], expand=True)
        self.__ollama = ollama_client()

    def __get_ollama_response(self, message: str):
        return self.__ollama.ask_question(message)
    
    def __send_button_on_click_event(self, e: ft.ControlEvent):
        message = f"# You:\n{self.__textField.value}"
        self.__canvas.controls.append(
            ft.Container(
                #content=ft.Text(message, size=20),
                content=ft.Markdown(value=message,
                                    selectable=True,
                                    extension_set="gitHubWeb",
                                    code_theme="atom-one-dark"),
                #bgcolor=ft.colors.GREEN_900,
                padding=10,
                border_radius=10,
                alignment=ft.alignment.center_left,
            )
        )
        self.__textField.value = ""
        self.__send_button.disabled = True
        self.update()
        response = self.__get_ollama_response(message)
        response_fmt = f"# Chat:\n{response}"
        self.__canvas.controls.append(
            ft.Container(
                #content=ft.Text(response, size=20),
                content=ft.Markdown(value=response_fmt,
                                    selectable=True,
                                    extension_set="gitHubWeb",
                                    code_theme="atom-one-dark"),
                #bgcolor=ft.colors.BLUE_900,
                padding=10,
                border_radius=10,
                alignment=ft.alignment.center_left
            )
        )
        self.__send_button.disabled = False
        self.update()

    def build(self):
        return ft.Container(content=self.__chat, expand=True)
