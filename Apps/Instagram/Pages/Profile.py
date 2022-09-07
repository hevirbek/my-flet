from flet import Page, Column, Text, CircleAvatar, Row, Column, WindowDragArea, Container
from flet import padding, ElevatedButton, IconButton, icons, GridView, Image
from flet import ButtonStyle

from flet.buttons import RoundedRectangleBorder
import requests

from Components.Stories import Stories


def get_images() -> dict:
    api_urL = "https://picsum.photos/v2/list?limit=9"

    response = requests.get(api_urL)

    if response.status_code == 200:
        return {
            'success': True,
            'data': response.json()
        }
    return {'success': False}


pp_url = "https://images.hdqwalls.com/wallpapers/python-logo-4k-i6.jpg"
response = get_images()['data']


def Profile(page: Page):
    def map_f(pic):
        return {
            'picture': pic['download_url'],
            'username': "Highlights"
        }

    data = list(map(map_f, response))

    title_username = WindowDragArea(
        Text(value="huseyinaverbek", size=20, weight="w500")
    )

    pp = CircleAvatar(
        foreground_image_url=pp_url,
        radius=50
    )

    post_count = Column(
        controls=[
            Text("9", size=20, weight="w500"),
            Text("Gönderi")
        ],
        horizontal_alignment="center"
    )

    follower_count = Column(
        controls=[
            Text("311", size=20, weight="w500"),
            Text("Takipçi")
        ],
        horizontal_alignment="center"
    )

    following_count = Column(
        controls=[
            Text("342", size=20, weight="w500"),
            Text("Takip")
        ],
        horizontal_alignment="center"
    )

    profile_data = Row(
        controls=[
            post_count,
            follower_count,
            following_count
        ],
        alignment="spaceEvenly",
        vertical_alignment="center",
        expand=True
    )

    pp_and_data = Container(
        Row(
            controls=[
                pp,
                profile_data
            ],
        ),
        padding=padding.all(10)
    )

    name = Text(value="Hüseyin Averbek", weight="w500")
    biography = Text(value="Fullstack Developer")

    btns = Row(
        controls=[
            ElevatedButton(
                text="Profili Düzenle",
                bgcolor="white",
                color="black",
                style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=5),
                ),
                expand=True
            )
        ]
    )

    stories = Stories(page, data)

    images = GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    for i in range(0, 60):
        images.controls.append(
            Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit="none",
                repeat="noRepeat",
            )
        )
    page.update()

    profile = Column(
        controls=[
            title_username,
            pp_and_data,
            name,
            biography,
            btns,
            stories,
            images
        ]
    )

    return profile
