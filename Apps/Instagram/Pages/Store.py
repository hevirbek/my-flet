from flet import Page, Container, Text, Column, TextField, icons


from Components.PostsGrid import PostsGrid


def Store(page: Page):
    search_input = TextField(
        hint_text="Ara",
        prefix_icon=icons.SEARCH
    )

    images = PostsGrid(page, 2)

    store = Column(
        controls=[
            search_input,
            images
        ]
    )

    return store
