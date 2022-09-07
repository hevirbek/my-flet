from flet import Page, Row, Image, IconButton, Icon, icons, FilePicker, FilePickerResultEvent, FilePickerUploadFile, FilePickerUploadEvent

from Components.Post import Post

instagram_top_left_src = "https://seeklogo.com/images/I/instagram-logo-468E0CC266-seeklogo.com.png"


def HomepageNavbar(page: Page):
    instagram_top_left = Image(
        src=instagram_top_left_src,
        width=100,
        height=50,
        fit="contain",
    )

    def files_result(e: FilePickerResultEvent):
        upload_list = []
        if files_dialog.result != None and files_dialog.result.files != None:
            for f in files_dialog.result.files:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            files_dialog.upload(upload_list)

    def on_upload_progress(e: FilePickerUploadEvent):
        if e.progress == 1:
            root = page.controls[0]
            main = root.content.controls[0]
            posts = main.controls[3]

            pp_url = "https://avatars.githubusercontent.com/u/72341654?v=4"

            new_post = Post(
                page, pp_url, "me", f"/assets/uploads/{e.file_name}")

            posts.controls.insert(0, new_post)
            posts.update()

    files_dialog = FilePicker(on_result=files_result,
                              on_upload=on_upload_progress)

    page.overlay.append(files_dialog)

    plus_icon = IconButton(
        icon=icons.ADD, on_click=lambda _: files_dialog.pick_files())
    dm_icon = IconButton(icon=icons.SEND)

    top_right_row = Row(
        controls=[
            plus_icon,
            dm_icon
        ],
    )

    r1 = Row(
        controls=[
            instagram_top_left,
            top_right_row
        ],
        alignment="spaceBetween",
        height=50,
    )

    return r1
