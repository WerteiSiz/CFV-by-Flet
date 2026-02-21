import flet as ft
import math
from papka.components.calculations import ygol_mesta, azimut, dalnost,poteri,factorG,atmosphere
from papka.components.ml import load_model,predict_diameter
from papka.components.constants import R3, H, COLORS, footer
from papka.components.save_functions import *
from papka.components.input_fields import *
from papka.components.buttons import *
from papka.pages.energy_uplink import show_results_energy_uplink
from components.earth_visualization import EarthVisualization


try:
    from pages.positioning import show as show_positioning
    from pages.energy_uplink import show as show_energy_uplink
    from pages.energy_downlink import show as show_energy_downlink
    from pages.desicion_support import show as show_desicion_support
except ImportError:
    def show_positioning(container, page, inputs  ,buttons_row):
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

    def show_energy_uplink(
            container, page, inputs  ,buttons_row1):
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
                    padding=20,
                    border=ft.border.all(1, COLORS["purple_blue"]),
                    border_radius=8,
                    content=ft.Column(
                        spacing=20,
                        controls=[
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
                        ],
                    ),
                ),
                elevation=8,
                color=COLORS["white"],
                margin=ft.margin.only(bottom=30),
            )
        )

        page.update()
    def show_energy_downlink( container, page, inputs  ,buttons_row1,EarthVisualization):
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
                    padding=20,
                    border=ft.border.all(1, COLORS["purple_blue"]),
                    border_radius=8,
                    content=ft.Column(
                        spacing=20,
                        controls=[
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
                        ],
                    ),
                ),
                elevation=8,
                color=COLORS["white"],
                margin=ft.margin.only(bottom=30),
            )
        )

        page.update()
    def show_desicion_support(container, page):
        container.controls.append(ft.Text("СППР (раздел в разработке)", color="gray"))

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.title = "САПР VSAT"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = COLORS["white"]
    inputs = Inputs()
    # Контейнер для динамического контента
    content_area = ft.Column(expand=True, spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def menu_button_style():
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor={
                "": COLORS["lavanda"],
                "hovered": COLORS["white"],

            },
            color={
                "": COLORS["dark_purple"],
                "hovered": COLORS["purple_blue"],

            },
            padding=10,
        )
    def feature_card(icon, title, desc, color, on_click):
        icon_box = ft.Container(
            width=50,
            height=50,
            bgcolor=color,
            border_radius=14,
            alignment=ft.alignment.center,
            content=ft.Icon(icon, color="white", size=28),
            animate_scale=200,
        )

        link = ft.Text(
            "Перейти →",
            color=COLORS["purple_blue"],
            weight=ft.FontWeight.BOLD,
            animate_scale=200,
        )

        card = ft.Container(
            width=420,
            padding=22,
            bgcolor=COLORS["white"],
            border_radius=16,
            border=ft.border.all(1, COLORS["lavanda"]),
            on_click=on_click,
            content=ft.Column(
                spacing=12,
                controls=[
                    icon_box,
                    ft.Text(title, size=20, weight=ft.FontWeight.BOLD, color=COLORS["dark_purple"]),
                    ft.Text(desc, size=14, color=COLORS["graphit"]),
                    link
                ]
            )
        )

        def hover(e):
            if e.data == "true":
                card.border = ft.border.all(2, COLORS["purple_blue"])
                icon_box.scale = 1.15
                link.scale = 1.1
            else:
                card.border = ft.border.all(1, COLORS["lavanda"])
                icon_box.scale = 1
                link.scale = 1
            card.update()

        card.on_hover = hover

        return card
    #Кнопки расчетов и тд
    calc_button = ft.ElevatedButton(
        text="Произвести расчёты",
        icon=ft.Icons.CALCULATE,
        style=calc_btn_style,
        width=200,
        on_click=lambda e: show_results_positioning(
            content_area, page, inputs  ,buttons_row
        )
    )

    save_button = ft.PopupMenuButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.SAVE, color=COLORS["purple_blue"]),
                ft.Text("Сохранить", color=COLORS["purple_blue"]),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        items=[
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.TEXT_SNIPPET, color=COLORS["purple_blue"]),
                        ft.Text("Сохранить в TXT", color=COLORS["dark_purple"]),
                    ]
                ),
                # on_click=lambda e: save_to_txt(),  # замените на вашу функцию
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.DESCRIPTION, color=COLORS["purple_blue"]),
                        ft.Text("Сохранить в Word", color=COLORS["dark_purple"]),
                    ]
                ),
                # on_click=lambda e: save_to_word(),
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.TABLE_CHART, color=COLORS["purple_blue"]),
                        ft.Text("Сохранить в Excel", color=COLORS["dark_purple"]),
                    ]
                ),
                # on_click=lambda e: save_to_excel(),
            ),
        ],
        tooltip="Выберите формат сохранения",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            side=ft.BorderSide(3, COLORS["purple_blue"]),  # обводка толщиной 3
            bgcolor=ft.Colors.WHITE,
        ),
    )
    save_energy_button = ft.PopupMenuButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.SAVE, color=COLORS["purple_blue"]),
                ft.Text("Сохранить", color=COLORS["purple_blue"]),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        items=[
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.TEXT_SNIPPET, color=COLORS["purple_blue"]),
                        ft.Text("Сохранить в TXT", color=COLORS["dark_purple"]),
                    ]
                ),
                # on_click=lambda e: save_to_txt(),  # замените на вашу функцию
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.DESCRIPTION, color=COLORS["purple_blue"]),
                        ft.Text("Сохранить в Word", color=COLORS["dark_purple"]),
                    ]
                ),
                # on_click=lambda e: save_to_word(),
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.TABLE_CHART, color=COLORS["purple_blue"]),
                        ft.Text("Сохранить в Excel", color=COLORS["dark_purple"]),
                    ]
                ),
                # on_click=lambda e: save_to_excel(),
            ),
        ],
        tooltip="Выберите формат сохранения",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            side=ft.BorderSide(3, COLORS["purple_blue"]),  # обводка толщиной 3
            bgcolor=ft.Colors.WHITE,
        ),
    )
    calc_energy_button = ft.ElevatedButton(
        text="Произвести расчёты",
        icon=ft.Icons.CALCULATE,
        style=calc_btn_style,
        width=200,
        on_click=lambda e: show_results_energy_uplink(
            content_area, page, inputs  ,buttons_row1
        )
    )
    buttons_row = ft.Row(
        [calc_button, save_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
    )
    buttons_row1 = ft.Row(
        [calc_energy_button, save_energy_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
    )


    # Обработчики кликов
    def on_click_sapr(e):
        content_area.controls.clear()

        content_area.controls.append(
            ft.Container(
                content=ft.Text(
                    "Добро пожаловать в САПР для VSAT",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.center,
                margin=30,
            )
        )

        content_area.controls.append(
            ft.Container(
                content=ft.Text(
                    "Современная система автоматизированного проектирования спутниковых линий связи. "
                    "Выполняйте расчеты позиционирования, энергетические расчеты и получайте рекомендации по выбору оборудования.",
                    size=20,
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.center,
            )
        )
       # карточки 2 на 2
        content_area.controls.append(
            ft.Column(
                spacing=30,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        spacing=30,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            feature_card(
                                ft.Icons.NEAR_ME,
                                "Позиционирование",
                                "Расчёт угла места, азимута и наклонной дальности для точного позиционирования антенны",
                                COLORS["purple_blue"],
                                on_click_positioning
                            ),
                            feature_card(
                                ft.Icons.WIFI,
                                "Энергетический расчёт (ЗС-ИЗС)",
                                "Расчёт параметров линии связи вверх от земной станции к спутнику",
                                COLORS["light_blue"],
                                on_click_zes_izs
                            ),
                        ]
                    ),
                    ft.Row(
                        spacing=30,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            feature_card(
                                ft.Icons.SATELLITE_ALT,
                                "Энергетический расчёт (ИЗС-ЗС)",
                                "Расчёт параметров линии связи вниз от спутника к земной станции с визуализацией",
                                COLORS["purple_blue"],
                                on_click_izs_zes
                            ),
                            feature_card(
                                ft.Icons.QUERY_STATS,
                                "СППР",
                                "Система поддержки принятия решений для определения оптимального диаметра рефлектора",
                                COLORS["dark_purple"],
                                on_click_sppr
                            ),
                        ]
                    ),
                ]
            ),
        )

        def create_feature_item(text):
            return ft.Row([
                ft.Container(width=8, height=8, bgcolor=COLORS["purple_blue"], border_radius=4),
                ft.Text(text, color=COLORS["graphit"], size=14)
            ], spacing=12)

        features = [
            "Точные расчеты параметров спутниковых линий связи на основе научных формул",
            "Визуализация параметров передачи сигнала с учетом атмосферных потерь",
            "Экспорт результатов в форматы TXT, Word и Excel для дальнейшей обработки",
            "Интеллектуальная система рекомендаций по выбору оборудования",
        ]

        content_area.controls.append(
            ft.Container(
                bgcolor=COLORS["lavanda"],
                width=870,
                height=200,
                border_radius=16,
                padding=20,
                content=ft.Column([
                    ft.Text("Возможности системы", size=20, weight=ft.FontWeight.BOLD, color=COLORS["dark_purple"]),
                    *[create_feature_item(f) for f in features]
                ], spacing=10)
            )
        )
        content_area.controls.append(
            footer,
        )
        page.update()

    def on_click_positioning(e):
        content_area.controls.clear()
        show_positioning(
            content_area,
            page,
            inputs,
            buttons_row,
        )
        page.update()

    def on_click_zes_izs(e):
        content_area.controls.clear()
        show_energy_uplink(
            content_area, page, inputs  ,buttons_row1
        )
        page.update()

    def on_click_izs_zes(e):
        content_area.controls.clear()
        show_energy_downlink(content_area, page, inputs  ,buttons_row1, EarthVisualization)
        page.update()
    def on_click_sppr(e):
        content_area.controls.clear()
        show_desicion_support(content_area, page, inputs)
        page.update()

    # Меню
    menubar = ft.Container(
        bgcolor=COLORS["lavanda"],
        padding=12,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.MenuItemButton(
                    style=menu_button_style(),
                    content=ft.Text("САПР VSAT"),
                    leading=ft.Icon(ft.Icons.RADIO, color=COLORS["dark_purple"]),
                    on_click=on_click_sapr
                ),
                ft.Row(
                    spacing=6,
                    controls=[
                        ft.MenuItemButton(
                            style=menu_button_style(),
                            content=ft.Text("Позиционирование"),
                            leading=ft.Icon(ft.Icons.LOCATION_ON, color=COLORS["dark_purple"]),
                            on_click=on_click_positioning
                        ),
                        ft.MenuItemButton(
                            style=menu_button_style(),
                            content=ft.Text("ЗС-ИЗС"),
                            leading=ft.Icon(ft.Icons.SATELLITE, color=COLORS["dark_purple"]),
                            on_click=on_click_zes_izs
                        ),
                        ft.MenuItemButton(
                            style=menu_button_style(),
                            content=ft.Text("ИЗС-ЗС"),
                            leading=ft.Icon(ft.Icons.SATELLITE_ALT, color=COLORS["dark_purple"]),
                            on_click=on_click_izs_zes
                        ),
                        ft.MenuItemButton(
                            style=menu_button_style(),
                            content=ft.Text("СППР"),
                            leading=ft.Icon(ft.Icons.ANALYTICS, color=COLORS["dark_purple"]),
                            on_click=on_click_sppr
                        ),
                    ]
                )
            ]
        )
    )
    page.add(
        ft.Column(
            [
                menubar,
                ft.Divider(height=2, thickness=1, color=COLORS["accent"]),
                ft.Column(
                    controls=[content_area],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
            ],
            expand=True,
            spacing=0
        )
    )


    on_click_sapr(None)


if __name__ == "__main__":
    ft.app(target=main)
