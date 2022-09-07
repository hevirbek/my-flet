from flet import Page, Container, Text, Column, TextField, icons

from Components.PostsGrid import PostsGrid


def Explore(page: Page):
    search_input = TextField(
        hint_text="Ara",
        prefix_icon=icons.SEARCH
    )

    images = PostsGrid(page, 3)

    explore = Column(
        controls=[
            search_input,
            images
        ]
    )

    return explore
