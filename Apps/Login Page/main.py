import flet
from flet import Page, TextField, Text, ElevatedButton, Column


def main(page: Page):
    def handle_login(e):
        if username.value == "test" and password.value == "test":
            result.value = "Giriş Başarılı!"
        else:
            result.value = "Giriş bilgileri hatalı!"
        result.update()

    username = TextField(label="Kullanıcı Adı")
    password = TextField(label="Parola", password=True)

    login = ElevatedButton(
        text="Giriş",
        width=page.width,
        color="white",
        bgcolor="purple",
        on_click=handle_login
    )

    result = Text(value="")

    col = Column(
        controls=[
            username,
            password,
            login,
            result
        ],
        width=page.width,
        height=page.height,
        alignment="center",
        horizontal_alignment="center"
    )

    page.controls.append(col)

    page.update()


flet.app(target=main)
