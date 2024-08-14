import flet as ft

from llama.client import ollama_client


class Chat(ft.Container):
    def __init__(self):
        super().__init__(expand=True)
        self.__canvas = ft.Column(expand=True, auto_scroll=True, scroll=True)
        self.__canvas_container = ft.Container(content=self.__canvas, expand=5)
        self.__textField = ft.TextField(label="Write a message", value="", shift_enter=True, on_submit=self.__send_button_on_click_event, expand=True)
        self.__send_button = ft.ElevatedButton(text="Send", icon=ft.icons.SEND, on_click=self.__send_button_on_click_event)
        self.__send_row = ft.Row(controls=[self.__textField, self.__send_button], expand=True)
        self.__send_row_container = ft.Container(content=self.__send_row, expand=1)
        self.__chat = ft.Column(controls=[self.__canvas_container, self.__send_row_container], expand=True)
        self.__ollama = ollama_client()
        self.content = self.__chat

    def __get_ollama_response(self, message: str):
        return self.__ollama.ask_question(message)
    
    def __send_button_on_click_event(self, e: ft.ControlEvent):
        message = f"# You:\n{self.__textField.value}"
        message = message.replace("\n", "\n\n")
        self.__canvas.controls.append(
            ft.Container(
                content=ft.Markdown(value=message,
                                    selectable=True,
                                    extension_set="gitHubWeb",
                                    code_theme="atom-one-dark"),
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
                content=ft.Markdown(value=response_fmt,
                                    selectable=True,
                                    extension_set="gitHubWeb",
                                    code_theme="atom-one-dark"),
                padding=10,
                border_radius=10,
                alignment=ft.alignment.center_left
            )
        )
        self.__send_button.disabled = False
        self.update()
