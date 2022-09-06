from flet import Page, Row, Image, IconButton, Icon, icons, ListView, Column, CircleAvatar, Text, SnackBar


def Post(page: Page, pp_url: str, username: str, img_url: str,) -> Column:
    pp = CircleAvatar(
        foreground_image_url=pp_url,
        radius=10,
    )
    title_row = Row(
        controls=[
            pp,
            Text(value=username),
        ],
        vertical_alignment='center'
    )
    new_img = Image(
        src=img_url,
        width=page.width,
        fit="contain",
    )

    def like_or_dislike(e):
        if e.control.icon == icons.FAVORITE_BORDER_OUTLINED:
            e.control.icon = icons.FAVORITE
        else:
            e.control.icon = icons.FAVORITE_BORDER_OUTLINED
        e.control.update()

    heart_icon = IconButton(
        icon=icons.FAVORITE_BORDER_OUTLINED, on_click=like_or_dislike)
    comment_icon = IconButton(icon=icons.SMS_OUTLINED)
    send_icon = IconButton(icon=icons.SEND)

    reaction_row = Row(
        controls=[
            heart_icon,
            comment_icon,
            send_icon
        ]
    )

    def save_or_unsave(e):
        if e.control.icon == icons.BOOKMARK_OUTLINE_OUTLINED:
            e.control.icon = icons.BOOKMARK
            page.snack_bar = SnackBar(Text(value="Gönderi kaydedildi"))
            page.snack_bar.open = True
            page.update()
        else:
            e.control.icon = icons.BOOKMARK_OUTLINE_OUTLINED
        e.control.update()

    bookmark_icon = IconButton(
        icon=icons.BOOKMARK_OUTLINE_OUTLINED, on_click=save_or_unsave)

    under_image_row = Row(
        controls=[
            reaction_row,
            bookmark_icon
        ],
        alignment="spaceBetween"
    )

    likes = Row(
        controls=[
            Text(value="280", weight="bold"),
            Text(value="likes"),
        ],
    )

    new_post = Column(
        controls=[
            title_row,
            new_img,
            under_image_row,
            likes
        ],
    )

    return new_post
