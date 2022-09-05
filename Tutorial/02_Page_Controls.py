import flet
from flet import Page, Text


def main(page: Page):
    print(page.controls)
    t = Text(value="Hello, world!", color="green")
    page.controls.append(t)
    print(page.controls)
    page.update()


flet.app(target=main)
