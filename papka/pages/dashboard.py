import flet as ft
from papka.components.constants import COLORS
from papka.ui import *

def dashboard(content_area, page, inputs, buttons_row1):
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
