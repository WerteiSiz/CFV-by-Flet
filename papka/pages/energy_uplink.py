import flet as ft
from papka.components.constants import COLORS, footer
from papka.components.calculations import *
from papka.components.input_fields import *
from papka.components.notifications import *
def show_energy_uplink(container, page, inputs, buttons_row1):
    container.controls.append(
        ft.Container(
            margin=10,
            content=ft.Text(
                "Энергетический расчет (ЗС-ИЗС)",
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
                "Расчет параметров линии связи вверх от земной станции к спутнику",
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
                            ft.Container(inputs.chastota, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.diametr, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.k, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.P, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.T, padding=15, col={"sm": 12, "md": 4}),
                            ft.Container(inputs.p, padding=15, col={"sm": 12, "md": 4}),
                        ],
                        spacing=20,
                        run_spacing={"xs": 10, "sm": 15, "md": 20},
                    ),
                    buttons_row1,
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

def show_results_energy_uplink(container, page, inputs, buttons_row1):
    try:
        gradys_d = float(inputs.gradys_d.value)
        gradys_sh = float(inputs.gradys_sh.value)
        tochka = float(inputs.tochka.value)
        chastota = float(inputs.chastota.value)
        diametr = float(inputs.diametr.value)
        k = float(inputs.k.value)
        P = float(inputs.P.value)
        T = float(inputs.T.value)
        p = float(inputs.p.value)

        # Вычисляем параметры
        angle= ygol_mesta(gradys_d, gradys_sh, tochka)
        azimuth_angle = azimut(gradys_d, gradys_sh, tochka)
        distance = dalnost(gradys_d, gradys_sh, tochka)
        signal_loss = round(poteri(chastota, diametr, k, tochka), 3)
        gain = round(factorG(chastota, k, diametr), 3)
        atmos = round(atmosphere(chastota, gradys_d, gradys_sh, tochka, T, p, P), 3)
        length = 0.3 / chastota  # Пример вычисления длины волны

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
                    ft.Text("Позиционирование", size=24, color=COLORS["purple_blue"],
                            text_align=ft.TextAlign.LEFT),

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
                                ft.Text(f"{azimuth_angle:.2f}°", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.LEFT,color=COLORS["blue"]),
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
                                ft.Text(f"{distance:.2f} км", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER,
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
            ft.ResponsiveRow(
                [
                    ft.Text("Энергетические расчеты", size=24,color=COLORS["purple_blue"],
                            text_align=ft.TextAlign.LEFT),

                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Длина волны", size=16, weight=ft.FontWeight.W_600, color=COLORS["graphit"],
                                        text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{length:.2f}°", size=30, text_align=ft.TextAlign.CENTER,
                                        weight=ft.FontWeight.BOLD,
                                        color=COLORS["purple_blue"]),

                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 6},
                        bgcolor=COLORS["white"],
                        border_radius=12,
                        width=180,
                        height=100,

                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Потери в свободном пространстве", size=16, color=COLORS["graphit"], weight=ft.FontWeight.W_600,
                                        text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{atmos:.2f}°", size=30, weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.LEFT, color=ft.Colors.RED_600),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 6},
                        bgcolor=COLORS["white"],
                        border_radius=12,
                        width=180,
                        height=100,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Потери в атмосфере", size=16, color=COLORS["graphit"],
                                        weight=ft.FontWeight.W_600, text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{signal_loss:.2f} км", size=30, weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        color=ft.Colors.ORANGE_300),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 6},
                        bgcolor=COLORS["white"],
                        border_radius=12,
                        width=180,
                        height=100,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Коэффициент усиления", size=16, color=COLORS["graphit"],
                                        weight=ft.FontWeight.W_600, text_align=ft.TextAlign.CENTER),
                                ft.Text(f"{gain:.2f} км", size=30, weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER,
                                        color=ft.Colors.GREEN_300),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        padding=15,
                        col={"sm": 12, "md": 6},
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

