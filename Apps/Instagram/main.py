import flet
from flet import Page, Column, Divider, Container, Stack, View

from Components.NavigationBar import NavigationBar

from Pages.Homepage import Homepage
from Pages.Explore import Explore
from Pages.Reels import Reels
from Pages.Store import Store
from Pages.Profile import Profile


def get_all_controls(page):
    try:
        if not page.controls:
            return
        for c in page.controls:
            print(c)
            get_all_controls(c)
    except:
        try:
            if not page.content:
                return
            print(page)
            get_all_controls(page.content)
        except:
            return


def main(page: Page):
    page.window_title_bar_hidden = True
    page.window_width = 450
    page.window_height = 800

    homepage = Homepage(page)
    explore = Explore(page)
    reels = Reels(page)
    store = Store(page)
    profile = Profile(page)

    mainStack = View(
        route="/",
        controls=[
            Container(
                content=Stack(
                    controls=[
                        homepage,
                        NavigationBar(page),
                    ]
                ),
                width=page.window_width,
                height=page.window_height
            )
        ]
    )

    def route_change(route):
        view = View()

        if page.route == "/":
            mainStack.route = "/"
            mainStack.controls[0].content.controls[0] = homepage
        elif page.route == "/explore":
            mainStack.route = "/explore"
            mainStack.controls[0].content.controls[0] = explore
        elif page.route == "/reels":
            mainStack.route = "/reels"
            mainStack.controls[0].content.controls[0] = reels
        elif page.route == "/store":
            mainStack.route = "/store"
            mainStack.controls[0].content.controls[0] = store
        elif page.route == "/profile":
            mainStack.route = "/profile"
            mainStack.controls[0].content.controls[0] = profile

        page.views.clear()
        page.views.append(mainStack)
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


flet.app(target=main, assets_dir="assets", upload_dir="assets/uploads")
