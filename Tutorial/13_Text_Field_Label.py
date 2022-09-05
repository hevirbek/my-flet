import flet
from flet import Page, TextField


def main(page: Page):
    text_input = TextField(label="Başlık", hint_text="Adınız..")

    page.controls.append(text_input)
    page.update()


flet.app(target=main)
