import flet as ft
from papka.components.constants import COLORS, footer
from papka.components.calculations import *
from papka.components.input_fields import Inputs
from papka.components.notifications import *
def show_positioning(container, page, inputs, buttons_row):
    container.controls.append(
        ft.Container(
            margin=10,
            content=ft.Text(
                "Позиционирование в пространстве",
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.LEFT,

            ),
            alignment=ft.alignment.top_left,

        )
    )
    container.controls.append(
        ft.Container(
            content=ft.Text(
                "Расчет угла места, азимута и наклонной дальности для точного позиционирования антенны",
                size=16,
                text_align=ft.TextAlign.LEFT,
            ),
            alignment=ft.alignment.top_left,
        )
    )
    container.controls.append(
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ResponsiveRow(
                        [
                            ft.Container(inputs.gradys_d, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.gradys_sh, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.tochka, padding=15, col={"sm": 12, "md": 4}),
                        ],
                        spacing=20,
                        run_spacing={"xs": 10, "sm": 15, "md": 20},
                    ),
                    buttons_row,
                ], spacing=20),
                padding=20,
                border=ft.border.all(1, COLORS["purple_blue"]),
                border_radius=8,
            ),
            elevation=8,
            color=COLORS["white"],
            margin=ft.margin.only(bottom=30),
        )
    )

def show_results_positioning(container, page, inputs, buttons_row):
    try:
        d = float(inputs.gradys_d.value)
        sh = float(inputs.gradys_sh.value)
        t = float(inputs.tochka.value)
        angle = ygol_mesta(d, sh, t)
        az = azimut(d, sh, t)
        dist = dalnost(d, sh, t)
    except Exception as ex:
        page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Ошибка: {ex}"), duration=3000))
        return

    if hasattr(container, 'last_result') and container.last_result:
        container.controls.remove(container.last_result)

    result_container = ft.Container(
        content=ft.Column([
            ft.ResponsiveRow(
                [
                    ft.Text("Результаты расчета", size=32, weight=ft.FontWeight.BOLD ,color=COLORS["purple_blue"],text_align=ft.TextAlign.LEFT),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Угол места", size=16, weight=ft.FontWeight.W_600 ,color=COLORS["graphit"],text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{angle:.2f}°", size=30,text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD,
                                        color=COLORS["purple_blue"]),

                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 4},
                        bgcolor=COLORS["white"],
                        border_radius=12,
                        width=180,
                        height=100,

                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Азимут", size=16, color=COLORS["graphit"],weight=ft.FontWeight.W_600 ,text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{az:.2f}°", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.LEFT,color=COLORS["blue"]),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 4},
                        bgcolor=COLORS["white"],
                        border_radius=12,
                        width=180,
                        height=100,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Наклонная дальность", size=16, color=COLORS["graphit"],weight=ft.FontWeight.W_600 ,text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{dist:.2f} км", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER,
                                        color=COLORS["light_blue"]),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 4},
                        bgcolor=COLORS["white"],
                        border_radius=12,
                        width=180,
                        height=100,
                    ),
                ],
                spacing=20,
                run_spacing={"xs": 10, "sm": 15, "md": 20},
            ),
        ], spacing=20),
        padding=20,
        border=ft.border.all(1, COLORS["purple_blue"]),
        border_radius=8,
        bgcolor=COLORS["lavanda"],
    )
    container.controls.append(
        footer
    )
    # 5. Добавляем новый результат и сохраняем ссылку на него
    container.controls.append(result_container)
    container.last_result = result_container  # сохраняем для удаления в следующий раз
    page.update()

