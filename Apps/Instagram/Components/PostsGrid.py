from flet import Page, GridView, Image


def PostsGrid(page: Page, column_count: int):
    images = GridView(
        expand=1,
        runs_count=5,
        max_extent=page.window_width//column_count,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    for i in range(0, 20):
        images.controls.append(
            Image(
                src=f"https://picsum.photos/300/300?{i}",
                fit="none",
                repeat="noRepeat",
            )
        )

    return images
