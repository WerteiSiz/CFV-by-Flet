import flet as ft
from .constants import COLORS

def create_input_field(label):
    return ft.TextField(
        label=label,
        border_color=COLORS["accent"],
        border_radius=10,
        border_width=1.5,
        bgcolor=COLORS["white"],
        label_style=ft.TextStyle(color=COLORS["dark_purple"]),
        color=COLORS["dark_purple"],
        width=300
    )
# Инициализация полей ввода
gradys_d_input = create_input_field("Долгота (°)")
gradys_sh_input = create_input_field("Широта (°)")
tochka_input = create_input_field("Точка стояния (°)")
chastota_input = create_input_field("Частота (ГГц)")
chastota1_input = create_input_field("Частота (ГГц)")
diametr_input = create_input_field("Диаметр антенны (м)")
k_input = create_input_field("Коэффициент использования")
P_input = create_input_field("Давление (кПа)")
T_input = create_input_field("Температура (°K)")
p_input = create_input_field("Влажность (г/м³)")
