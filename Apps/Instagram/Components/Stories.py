from flet import Page, ListView, Column, LinearGradient, CircleAvatar, Container, colors, Text, border_radius, alignment


def Stories(page: Page, data: dict):
    stories = ListView(expand=1, spacing=15, padding=5,
                       horizontal=True)

    for user in data:
        img_url = user['picture']
        username = user['username']

        new_img = CircleAvatar(
            foreground_image_url=img_url,
            radius=25,
        )

        story_container = Container(
            content=new_img,
            border_radius=border_radius.all(60),
            padding=3,
            gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=[colors.BLUE, colors.YELLOW],
            ),
        )

        username_story = Text(value=username)

        new_stack = Column(
            controls=[
                story_container,
                username_story
            ],
            alignment='center',
            horizontal_alignment='center'
        )
        stories.controls.append(new_stack)

    stories_container = Container(
        content=stories,
        height=90
    )

    return stories_container
