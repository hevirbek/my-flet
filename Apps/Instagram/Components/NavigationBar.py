from flet import Page, Container, Row, Icon, icons


def NavigationBar(page: Page):
    navbar = Container(
        content=Row(
            controls=[
                Icon(name=icons.HOME_FILLED),
                Icon(name=icons.SEARCH_OUTLINED),
                Icon(name=icons.SMART_DISPLAY_OUTLINED),
                Icon(name=icons.SHOPPING_BASKET_OUTLINED),
                Icon(name=icons.PERSON_OUTLINE),
            ],
            alignment="spaceAround",
            vertical_alignment="center",
        ),
        width=page.width,
        height=60,
        bgcolor='white',
        left=0,
        bottom=10,
        right=0
    )

    return navbar
