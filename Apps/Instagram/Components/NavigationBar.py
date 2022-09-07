from flet import Page, Container, Row, IconButton, icons, WindowDragArea


def NavigationBar(page: Page):
    def go_route(route):
        page.route = route
        page.update()

    navbar = Container(
        content=WindowDragArea(Row(
            controls=[
                IconButton(icon=icons.HOME_FILLED,
                           on_click=lambda e: go_route("/")),
                IconButton(icon=icons.SEARCH_OUTLINED,
                           on_click=lambda e: go_route("/explore")),
                IconButton(icon=icons.SMART_DISPLAY_OUTLINED,
                           on_click=lambda e: go_route("/reels")),
                IconButton(icon=icons.SHOPPING_BASKET_OUTLINED,
                           on_click=lambda e: go_route("/store")),
                IconButton(icon=icons.PERSON_OUTLINE,
                           on_click=lambda e: go_route("/profile")),
            ],
            alignment="spaceAround",
            vertical_alignment="center",
        )
        ),
        width=page.width,
        height=60,
        bgcolor='white',
        left=0,
        bottom=10,
        right=0
    )

    return navbar
