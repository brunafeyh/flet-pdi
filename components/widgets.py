import flet as ft

def build_upload_box(file_picker):
    return ft.Container(
        width=300,
        height=180,
        bgcolor="#F4F4F4",
        border=ft.border.all(2, "#D8D8D8"),
        border_radius=6,
        padding=20,
        alignment=ft.alignment.center,
        content=ft.Column([
            ft.Container(
                bgcolor="#DCDBDB",
                border_radius=100,
                padding=15,
                content=ft.Icon(name="insert_drive_file", size=40, color="#A3A3A3")
            ),
            ft.Column([
                ft.Text("Arraste e solte o arquivo aqui ou", size=14),
                ft.TextButton(
                    content=ft.Text(
                        "escolha um arquivo",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color="#2C2C2C",
                        style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    ),
                    on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=["jpg", "jpeg", "png"])
                )
            ], horizontal_alignment="center", spacing=0),
            ft.Text("Formatos suportados: JPG, PNG", size=11, color="grey"),
        ],
            horizontal_alignment="center",
            tight=True,
            spacing=5
        )
    )


def build_buttons(start_button_ref):
    return ft.Row([
        ft.Container(
            content=ft.TextButton(
                "Cancelar",
                style=ft.ButtonStyle(color="black")
            ),
            bgcolor="#E7E5E5",
            padding=ft.padding.symmetric(horizontal=8, vertical=2),
            border=ft.border.all(1, "#6B6B6B"),
            border_radius=0,
        ),
        ft.Container(
            content=ft.TextButton(
                "Iniciar",
                ref=start_button_ref,
                style=ft.ButtonStyle(color="white")
            ),
            bgcolor="blue",
            padding=ft.padding.symmetric(horizontal=8, vertical=2),
            border=ft.border.all(1, "blue"),
            border_radius=0,
        ),
    ], spacing=10)