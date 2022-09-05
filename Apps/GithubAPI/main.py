import flet
from flet import Page, Text, TextField, Row, CircleAvatar, ElevatedButton
import requests


def get_user(username: str) -> dict:
    api = "https://api.github.com/users/"
    url = api + username

    response = requests.get(url)
    if response.status_code == 200:
        return {
            'success': True,
            'data': response.json()
        }
    return {'success': False}


def main(page: Page):
    page.title = "Github"
    page.window_width = 450
    page.window_height = 800

    def handle_click(e):
        result = get_user(username_input.value)
        if result['success']:
            username.value = '@' + result['data']['login']
            public_repos.value = f"Repos:{result['data']['public_repos']}"
            followers.value = f"Followers:{result['data']['followers']}"
            following.value = f"Following:{result['data']['following']}"
            a1.foreground_image_url = result['data']['avatar_url']

            page.update()

    inital_user = get_user(username='hevirbek')

    a1 = CircleAvatar(
        foreground_image_url=inital_user['data']['avatar_url'],
        radius=100
    )

    r1 = Row(
        controls=[
            a1
        ],
        alignment="center"
    )

    page.controls.append(r1)

    username = Text(
        value=inital_user['data']['login'],
        size=20,
        weight="w900",
        width=page.width,
        text_align="center"
    )

    public_repos = Text(
        value=f"Repos:{inital_user['data']['public_repos']}",
        weight="w500"
    )

    followers = Text(
        value=f"Followers:{inital_user['data']['followers']}",
        weight="w500"
    )

    following = Text(
        value=f"Following:{inital_user['data']['following']}",
        weight="w500"
    )

    r2 = Row(
        controls=[
            public_repos,
            followers,
            following
        ],
        width=page.width,
        alignment="center"
    )

    page.controls.append(username)
    page.controls.append(r2)

    username_input = TextField(label="Username")
    b1 = ElevatedButton(
        text="Submit",
        width=page.width,
        bgcolor="purple",
        color="white",
        on_click=handle_click
    )

    page.controls.append(username_input)
    page.controls.append(b1)

    page.update()


flet.app(target=main)
