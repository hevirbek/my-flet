import flet
from flet import Page, ElevatedButton, SnackBar, Text


def main(page: Page):
    page.title = "Anasayfa"
    page.window_width = 400
    page.window_height = 700

    def show_snackbar(e):
        page.snack_bar = SnackBar(Text("Mesaj gönderildi!"))
        page.snack_bar.open = True
        page.update()

    b1 = ElevatedButton(text="Gönder", on_click=show_snackbar)

    page.controls.append(b1)

    page.update()


flet.app(target=main)
