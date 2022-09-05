import flet
from flet import Page, Text


def main(page: Page):
    t1 = Text(value="Hello, world!")  # default -> 16
    t2 = Text(value="Hello, world!", size=20)
    t3 = Text(value="Hello, world!", size=8)
    page.controls.append(t1)
    page.controls.append(t2)
    page.controls.append(t3)
    page.update()


flet.app(target=main)
