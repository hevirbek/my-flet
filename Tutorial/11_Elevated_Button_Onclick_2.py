import flet
from flet import Page, Text, ElevatedButton


def main(page: Page):
    def handle_click(e):
        t1.value = "Tıklandı"
        # page.update()
        t1.update()

    t1 = Text(value="Tıklanmadı")
    b1 = ElevatedButton(text="Tıkla", on_click=handle_click)
    page.controls.append(t1)
    page.controls.append(b1)
    page.update()


flet.app(target=main)
