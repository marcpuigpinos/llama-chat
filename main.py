import flet as ft

from gui.main_window import MainWindow

TITLE = "Llama-Chat"

def main(page: ft.Page):
    page.title = TITLE
    page.theme_mode = "dark"
    window = MainWindow(TITLE)
    page.add(window)

if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER)
