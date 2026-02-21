import flet as ft
# Глобальные параметры
R3 = 6378.0
H = 35810.0

# Цветовая палитра
COLORS = {
    "lavanda": "#E2D4F0",
    "dark_purple": "#9932CC",
    "Fon": "#FFF9F0",
    "accent": "#A78BFA",
    "graphit": "#414A4C",
    "light_blue": "#1F91DC",
    "white": "#FFFFFF",
    "purple_blue": "#7C39EC",
    "blue": "#2592f3",
    "light_blue":"#60a5fa"
}
footer = ft.Container(
        content=ft.Text(
            "© 2026 САПР VSAT. Система расчета спутниковых линий связи.",
            color=COLORS["graphit"],
            size=12,
            text_align=ft.TextAlign.CENTER,
        ),
        padding=10,
        bgcolor=COLORS["white"],
        alignment=ft.alignment.center,
    )
