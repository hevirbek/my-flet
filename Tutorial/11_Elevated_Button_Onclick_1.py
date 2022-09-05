import flet
from flet import Page, ElevatedButton


def main(page: Page):
    def handle_click(e):
        # b1.text = "Tıklandı"
        e.control.text = "Tıklandı"
        e.control.update()

    b1 = ElevatedButton(text="Tıkla", on_click=handle_click)
    page.controls.append(b1)
    page.update()


flet.app(target=main)
