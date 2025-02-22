import flet as ft
from supabase import create_client, Client
from views import home_view
SUPABASE_URL = "https://tdbxxshfsrztubbleium.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRkYnh4c2hmc3J6dHViYmxlaXVtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAxMzY2NTEsImV4cCI6MjA1NTcxMjY1MX0.viuJIoYR8c_SSK6xHbGZVwES5-Rf3o-xHK8KdUA9AUs"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def main(page: ft.Page):
    page.title = "School Clearance System"
    page.window.max_width = 420
    page.window.width = 420
    page.window.height = 900
    page.window.max_height = 1200
    page.vertical_alignment=ft.VerticalAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER

    page.bgcolor = ft.colors.WHITE
    page.route = "/login" #The default route page REMEMBER login
    page.update()

    def route_change(route):
        tr = page.route.split("/")[-1]
        if tr == "login":
            page.clean()
            page.add(login_view())
        elif tr == "signup":
            page.clean()
            page.add(signup_view())
        elif tr == "home":
            page.clean()
            page.add(home_view())
        page.update()

    def login_view():
        def login(e):
            email = txt_email.value.strip()
            password = txt_password.value.strip()

            if not email or not password:
                lbl_message.value = "Please fill in all fields!"
                lbl_message.color = ft.colors.RED
                page.update()
                return

            try:
                response = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if response and response.user:
                    page.go("/home")
                else:
                    lbl_message.value = "Invalid email or password!"
                    lbl_message.color = ft.colors.RED
            except Exception as ex:
                lbl_message.value = str(ex)
                lbl_message.color = ft.colors.RED
            page.update()

        lbl_message = ft.Text("")
        txt_email = ft.TextField(label="Email", width=300, border_radius=10, content_padding=10, adaptive=True,
                                 border_color="grey")
        txt_password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300,
                                    content_padding=10, border_radius=10, border_color='grey', adaptive=True)
        btn_login = ft.ElevatedButton("Login", color='white', bgcolor="blue", width=300, on_click=login)
        btn_signup = ft.TextButton("Sign Up", on_click=lambda _: page.go("/signup"))

        return ft.Column(
            [
                ft.Image(src="download (3).jpeg", width=200, height=200, border_radius=20),
                ft.Text("Welcome Back 😎", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color='black'),
                txt_email,
                txt_password,
                lbl_message,
                btn_login,
                ft.Text("Don't have an account?", color='black'),
                btn_signup,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )

    def signup_view():
        def signup(e):
            new_email = txt_new_email.value.strip()
            new_password = txt_new_password.value.strip()

            if not new_email or not new_password:
                lbl_message.value = "Please fill in all fields!"
                lbl_message.color = ft.colors.RED
                page.update()
                return

            try:
                response = supabase.auth.sign_up({"email": new_email, "password": new_password})
                if response and response.user:
                    lbl_message.value = "Account created successfully! Please log in."
                    lbl_message.color = ft.colors.GREEN
                    page.go("/login")
                else:
                    lbl_message.value = "Signup failed. Try again."
                    lbl_message.color = ft.colors.RED
            except Exception as ex:
                lbl_message.value = str(ex)
                lbl_message.color = ft.colors.RED
            page.update()

        lbl_message = ft.Text("")
        txt_new_email = ft.TextField(label="New Email", width=300, border_radius=10, content_padding=10, adaptive=True,
                                     border_color="grey")
        txt_new_password = ft.TextField(label="New Password", password=True, can_reveal_password=True, width=300,
                                        content_padding=10, border_radius=10, border_color='grey', adaptive=True)
        btn_signup = ft.ElevatedButton("Sign Up", color='white', bgcolor="blue", width=300, on_click=signup)
        btn_back = ft.TextButton("Back to Login", on_click=lambda _: page.go("/login"))

        return ft.Column(
            [
                ft.Image(src="download (3).jpeg", width=200, height=200, border_radius=20),
                ft.Text("Sign Up", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.BLACK),
                txt_new_email,
                txt_new_password,
                lbl_message,
                btn_signup,
                btn_back,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        )



    page.on_route_change = route_change


ft.app(target=main)
