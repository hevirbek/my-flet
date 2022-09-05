import flet
from flet import Page, TextField, Text


def main(page: Page):
    def handle_change(e):
        text.value = e.control.value
        text.update()

    text_input = TextField(
        label="Başlık",
        hint_text="Adınız..",
        on_change=handle_change
    )

    text = Text()

    page.controls.append(text_input)
    page.controls.append(text)
    page.update()


flet.app(target=main)
