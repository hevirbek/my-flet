import flet
from flet import Page, Checkbox, TextField, IconButton, icons, Row, ListView


def main(page: Page):
    page.title = "Todo List"
    page.window_width = 450
    page.window_height = 800

    lv = ListView(expand=1, spacing=10, padding=10)

    def add_todo(e):
        new_todo = Checkbox(label=todo_input.value)
        lv.controls.append(new_todo)
        todo_input.value = ""
        page.update()

    todo_input = TextField(label='Todo')
    add_button = IconButton(
        icon=icons.ADD,
        bgcolor="purple",
        icon_color="white",
        on_click=add_todo
    )

    row = Row(
        controls=[
            todo_input,
            add_button,
        ],
        alignment="center"
    )

    page.controls.append(row)
    page.controls.append(lv)

    page.update()


flet.app(target=main)
