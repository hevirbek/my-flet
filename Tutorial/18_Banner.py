import flet
from flet import Page, ElevatedButton, Banner, Icon, icons, Text, TextButton


def main(page: Page):
    page.title = "Anasayfa"
    page.window_width = 400
    page.window_height = 700

    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = Banner(
        bgcolor="green",
        leading=Icon(icons.WARNING, color="red", size=40),
        content=Text(
            "Hata! İşlem sırasında bazı hatalar oluştu. Ne yapmak istersiniz?"
        ),
        actions=[
            TextButton("Yeniden Dene", on_click=close_banner),
            TextButton("Yoksay", on_click=close_banner),
            TextButton("İptal", on_click=close_banner),
        ]
    )

    def show_banner(e):
        page.banner.open = True
        page.update()

    b1 = ElevatedButton(text="Göster", on_click=show_banner)

    page.controls.append(b1)

    page.update()


flet.app(target=main)
