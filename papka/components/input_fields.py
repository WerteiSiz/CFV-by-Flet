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
        width=300,
    )

class Inputs:
    def __init__(self):

        # --- Позиционирование ---
        self.gradys_d = create_input_field("Долгота (°)")
        self.gradys_sh = create_input_field("Широта (°)")
        self.tochka = create_input_field("Точка стояния (°)")
        self.chastota = create_input_field("Частота (ГГц)")
        self.chastota1 = create_input_field("Частота (ГГц)")
        self.diametr = create_input_field("Диаметр антенны (м)")
        self.k = create_input_field("Коэффициент использования")
        self.P = create_input_field("Давление (кПа)")
        self.T = create_input_field("Температура (°K)")
        self.p = create_input_field("Влажность (г/м³)")


def create_inputs():
    return Inputs()
