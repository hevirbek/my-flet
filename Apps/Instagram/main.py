import flet
from flet import Page, Column, Divider, Container, Stack
import requests

from Components.Navbar import Navbar
from Components.Stories import Stories
from Components.Posts import Posts
from Components.NavigationBar import NavigationBar

random_user_api = "https://randomuser.me/api/?results=10"
response = requests.get(random_user_api).json()['results']


def main(page: Page):
    page.window_title_bar_hidden = True
    page.window_width = 450
    page.window_height = 800

    r1 = Navbar(page)
    stories_container = Stories(page, response)
    posts = Posts(page, response)

    mainContent = Column(
        controls=[
            r1,
            stories_container,
            Divider(thickness=0.2),
            posts,
        ]
    )

    mainStack = Container(
        content=Stack(
            controls=[
                mainContent,
                NavigationBar(page),
            ]
        ),
        width=page.window_width,
        height=page.window_height
    )

    page.add(mainStack)

    page.update()


flet.app(target=main, assets_dir="assets", upload_dir="assets/uploads")
