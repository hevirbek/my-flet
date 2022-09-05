import flet
from flet import Page, Text


def main(page: Page):
    page.title = "Anasayfa"
    page.window_width = 400
    page.window_height = 700

    t = Text(value="Hello, world!")
    page.controls.append(t)
    page.update()


flet.app(target=main)
