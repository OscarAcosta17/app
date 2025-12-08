import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la ventana
    page.title = "Mi App con Diseño"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK  # O LIGHT
    page.window_width = 400
    page.window_height = 500

    # 2. Funciones (lógica)
    def al_hacer_click(e):
        texto_saludo.value = f"¡Hola, {campo_nombre.value}!"
        texto_saludo.update()
        page.snack_bar = ft.SnackBar(ft.Text("¡Acción ejecutada con éxito!"))
        page.snack_bar.open = True
        page.update()

    # 3. Elementos de diseño (Widgets)
    logo = ft.Icon(name=ft.icons.ROCKET_LAUNCH, size=50, color="blue")
    titulo = ft.Text("Bienvenido al Sistema", size=30, weight="bold")
    campo_nombre = ft.TextField(label="Tu nombre", width=200, border_radius=10)
    boton = ft.ElevatedButton(
        text="Lanzar", 
        on_click=al_hacer_click,
        bgcolor="blue",
        color="white",
        height=50
    )
    texto_saludo = ft.Text("", size=20, color="green")

    # 4. Agregar todo a la página
    page.add(
        logo,
        titulo,
        ft.Divider(),
        campo_nombre,
        boton,
        texto_saludo
    )

ft.app(target=main)