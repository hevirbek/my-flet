import flet
from flet import Page, Checkbox, TextField, IconButton, icons, Row, ListView, Draggable, DragTarget, Container


def main(page: Page):
    page.title = "Todo List"
    page.window_width = 450
    page.window_height = 800

    lv = ListView(expand=1, spacing=10, padding=10)

    def drag_will_accept(e):
        e.control.content.content.bgcolor = "#CC9999"
        e.control.update()

    def drag_leave(e):
        e.control.content.content.bgcolor = None
        e.control.update()

    def drag_accept(e):
        if page.get_control(id=e.data) == e.control.content:
            return
        src = page.get_control(id=e.data).content.content
        target = e.control.content.content.content
        src.label, target.label = target.label, src.label
        src.value, target.value = target.value, src.value
        e.control.content.content.bgcolor = None
        page.update()

    def add_todo(e):
        new_todo = DragTarget(
            group="todo",
            content=Draggable(
                group="todo",
                content=Container(
                    content=Checkbox(label=todo_input.value)
                )
            ),
            on_will_accept=drag_will_accept,
            on_accept=drag_accept,
            on_leave=drag_leave
        )

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
