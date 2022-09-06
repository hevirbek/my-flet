from flet import Page, ListView, Column

from Components.Post import Post


def Posts(page: Page, data: dict) -> Column:
    posts = ListView(expand=1, spacing=25)

    for user in data:
        pp_url = user['picture']
        img_url = user['picture']
        username = user['username']

        new_post = Post(page, pp_url, username, img_url)

        posts.controls.append(new_post)

    return posts
