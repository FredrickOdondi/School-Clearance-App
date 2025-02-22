import flet as ft
import supabase
from flet.core import page


def home_view():
    def logout(e):
        supabase.auth.sign_out()
        page.go("/login")

    search_bar = ft.Container(
        content=ft.TextField(
            label="🔍 Search",
            border_radius=20,
            bgcolor="#F1F2F3",
            color="black",
            border_color="#E0E0E0",
            expand=True,
        ),
        padding=ft.padding.all(15),  # Added padding for spacing
    )

    # Cards Section
    card_scroll = ft.Row(
        controls=[
            ft.Card(
                color="#00C846",
                elevation=3,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [ft.TextButton("Submit Clearance", style=ft.ButtonStyle(color="white"))],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ]
                    ),
                    padding=20,  # More padding for better spacing
                ),
                width=170,
                height=90,
            ),
            ft.Card(
                color="#00C846",
                elevation=3,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [ft.TextButton("View Status", style=ft.ButtonStyle(color="white"))],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ]
                    ),
                    padding=20,
                ),
                width=170,
                height=90,
            ),
        ],
        spacing=20,  # Increased spacing between cards
        wrap=True
    )

    # Recent Updates Section
    updates_title = ft.Container(
        content=ft.Text(
            "Recent Updates",
            color="black",
            size=18,
            font_family="Inter",
            weight=ft.FontWeight.BOLD,
        ),
        padding=ft.padding.only(top=20, bottom=10),  # Adds spacing above and below
    )

    update_card = ft.Card(
        elevation=5,
        content=ft.Container(
            bgcolor="white",
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.ListTile(
                        height=90,
                        text_color="black",
                        icon_color="green",
                        leading=ft.Icon(ft.Icons.APPROVAL),
                        title=ft.Text("Your Clearance Status", size=16, weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text("Congratulations! Your clearance request was approved.", size=14),
                    ),
                    ft.Row(
                        controls=[
                            ft.TextButton("Read", style=ft.ButtonStyle(color="#007BFF")),
                            ft.TextButton("Delete", style=ft.ButtonStyle(color="red")),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            padding=20,  # More padding inside the card
        ),
    )

    # Departments Section
    departments_title = ft.Container(
        content=ft.Text(
            "Departments",
            color="black",
            size=18,
            font_family="Inter",
            weight=ft.FontWeight.BOLD,
        ),
        padding=ft.padding.only(top=25, bottom=10),
    )

    department_list = ft.GridView(
        runs_count=2,
        spacing=15,  # Increased spacing between items
        run_spacing=15,
        controls=[
            ft.Container(
                content=ft.Text("Science", size=16, weight=ft.FontWeight.BOLD, color="white"),
                alignment=ft.alignment.center,
                bgcolor="#2E7D32",
                width=150,
                height=100,
                border_radius=10,
                on_click=lambda e: print("Science clicked!"),
            ),
            ft.Container(
                content=ft.Text("Library", size=16, weight=ft.FontWeight.BOLD, color="white"),
                alignment=ft.alignment.center,
                bgcolor="yellow",
                width=150,
                height=100,
                border_radius=10,
                on_click=lambda e: print("Library clicked!"),
            ),
            ft.Container(
                content=ft.Text("Finance", size=16, weight=ft.FontWeight.BOLD, color="white"),
                alignment=ft.alignment.center,
                bgcolor="cyan",
                width=150,
                height=100,
                border_radius=10,
                on_click=lambda e: print("Finance clicked!"),
            ),
            ft.Container(
                content=ft.Text("Admin Office", size=16, weight=ft.FontWeight.BOLD, color="white"),
                alignment=ft.alignment.center,
                bgcolor="red",
                width=150,
                height=100,
                border_radius=10,
                on_click=lambda e: print("Admin clicked!"),
            ),
        ],
    )

    return ft.Container(
        bgcolor="white",
        expand=True,
        content=ft.ListView(  # Enables scrolling
            expand=True,
            controls=[
                ft.Container(
                    content=ft.Text("Welcome Back", size=24,color="black" ,weight=ft.FontWeight.BOLD),
                    padding=ft.padding.only(top=20, bottom=15),  # Added spacing
                ),
                search_bar,
                card_scroll,
                updates_title,
                update_card,
                departments_title,
                department_list,
            ],
        ),
    )
