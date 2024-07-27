import flet as ft

from gui.main_window import MainWindow

def main(page: ft.Page):
    page.title = "Llama-chat"
    page.theme_mode = "dark"
    window = MainWindow("Llama-chat")
    page.add(window)

if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER)
