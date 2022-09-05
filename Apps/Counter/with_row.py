import flet
from flet import Page, Text, IconButton, icons, Row


def main(page: Page):
    txt_number = Text(value="0")

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        txt_number.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        txt_number.update()

    b1 = IconButton(icon=icons.REMOVE, on_click=minus_click)
    b2 = IconButton(icon=icons.ADD, on_click=plus_click)

    r1 = Row(
        controls=[
            b1,
            txt_number,
            b2
        ],
        width=page.width,
        height=page.height,
        alignment="center",
        vertical_alignment="center"
    )

    page.controls.append(r1)

    page.update()


flet.app(target=main)
