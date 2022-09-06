from flet import Page, Column, Divider
import requests

from Components.HomepageNavbar import HomepageNavbar
from Components.Stories import Stories
from Components.Posts import Posts

random_user_api = "https://randomuser.me/api/?results=10"
response = requests.get(random_user_api).json()['results']


def Homepage(page: Page):
    def map_f(user):
        return {
            'picture': user['picture']['large'],
            'username': user['name']['last'].lower()
        }

    data = list(map(map_f, response))

    r1 = HomepageNavbar(page)
    stories_container = Stories(page, data)
    posts = Posts(page, data)

    homepage = Column(
        controls=[
            r1,
            stories_container,
            Divider(thickness=0.2),
            posts,
        ]
    )

    return homepage
