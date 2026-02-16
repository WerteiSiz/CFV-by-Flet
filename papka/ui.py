import flet as ft
import math

try:
    from pages.positioning import show as show_positioning
    from pages.energy_uplink import show as show_energy_uplink
    from pages.energy_downlink import show as show_energy_downlink
    from pages.desicion_support import show as show_desicion_support
except ImportError:
    def show_positioning(container, page):
        container.controls.append(ft.Text("Позиционирование (раздел в разработке)", color="gray"))
    def show_energy_uplink(container, page):
        container.controls.append(ft.Text("ЗС-ИЗС (раздел в разработке)", color="gray"))
    def show_energy_downlink(container, page):
        container.controls.append(ft.Text("ИЗС-ЗС (раздел в разработке)", color="gray"))
    def show_desicion_support(container, page):
        container.controls.append(ft.Text("СППР (раздел в разработке)", color="gray"))

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
    "purple_blue": "#7C39EC"
}


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.title = "САПР VSAT"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = COLORS["white"]

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
            )
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
            footer
        )

        page.update()

    def on_click_positioning(e):
        content_area.controls.clear()
        show_positioning(content_area, page)
        page.update()

    def on_click_zes_izs(e):
        content_area.controls.clear()
        show_energy_uplink(content_area, page)
        page.update()

    def on_click_izs_zes(e):
        content_area.controls.clear()
        show_energy_downlink(content_area, page)
        page.update()

    def on_click_sppr(e):
        content_area.controls.clear()
        show_desicion_support(content_area, page)
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
    footer = ft.Container(
        content=ft.Text(
            "© 2026 САПР VSAT. Система расчета спутниковых линий связи.",
            color=COLORS["graphit"],
            size=12,
            text_align=ft.TextAlign.CENTER,
        ),
        padding=10,
        bgcolor=COLORS["white"],  # по желанию
    )
    page.add(
        ft.Column(
            [
                menubar,
                ft.Divider(height=2, thickness=1, color=COLORS["accent"]),
                content_area
            ],
            expand=True,
            spacing=0
        )
    )

    on_click_sapr(None)


if __name__ == "__main__":
    ft.app(target=main)
