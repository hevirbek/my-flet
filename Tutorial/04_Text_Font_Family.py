import flet
from flet import Page, Text


def main(page: Page):
    t1 = Text(value="Hello, world!")
    t2 = Text(value="Hello, world!", font_family="Consolas")
    page.controls.append(t1)
    page.controls.append(t2)
    page.update()


flet.app(target=main)
