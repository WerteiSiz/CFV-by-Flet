import flet as ft
from papka.components.constants import *
from papka.pages.positioning import *
from papka.components.input_fields import *
from papka.ui import *

# Стиль для кнопки расчёта
calc_btn_style = ft.ButtonStyle(
    bgcolor=COLORS["purple_blue"],
    color=COLORS["white"],
    shape=ft.RoundedRectangleBorder(radius=12),
    side=ft.BorderSide(1, COLORS["purple_blue"]),
    padding=15,
)



