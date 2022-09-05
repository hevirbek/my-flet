import flet
from flet import Page, Text


def main(page: Page):
    t1 = Text(value="Adana")
    t2 = Text(value="Mersin")
    t3 = Text(value="İstanbul")
    page.controls.append(t1)
    page.controls.append(t2)
    page.controls.append(t3)
    page.update()


flet.app(target=main)
