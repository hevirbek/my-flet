import flet
from flet import Page, ElevatedButton, AlertDialog, Text, TextButton


def main(page: Page):
    page.title = "Anasayfa"
    page.window_width = 400
    page.window_height = 700

    def close_dlg(e):
        dlg.open = False
        page.update()

    dlg = AlertDialog(
        modal=True,
        title=Text("Hello, world!"),
        content=Text("Emin misiniz?"),
        actions=[
            TextButton("Evet", on_click=close_dlg),
            TextButton("Hayır", on_click=close_dlg)
        ],
        on_dismiss=lambda e: print("Dialog kapatıldı!")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    b1 = ElevatedButton(text="Aç", on_click=open_dlg)

    page.controls.append(b1)

    page.update()


flet.app(target=main)
