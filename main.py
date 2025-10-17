import flet as ft

def main(page: ft.Page):
    page.title = "Teste Flet APK"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_600

    page.add(
        ft.Text(
            "O BUILD FUNCIONOU!",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.WHITE
        )
    )

if __name__ == "__main__":
    ft.app(target=main)