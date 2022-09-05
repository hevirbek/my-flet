import flet
from flet import Page, Checkbox


def main(page: Page):
    page.title = "Anasayfa"
    page.window_width = 400
    page.window_height = 700

    cb1 = Checkbox(value=False)
    cb2 = Checkbox(value=False, label="Seçenek 1")
    cb3 = Checkbox(value=True, label="Seçenek 2")

    page.controls.append(cb1)
    page.controls.append(cb2)
    page.controls.append(cb3)

    page.update()


flet.app(target=main)
