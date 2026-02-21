import flet as ft
import threading
from .constants import COLORS

notification_text = ft.Text(size=14)


def create_notification():
    """Создает контейнер уведомления"""

    container = ft.Container(
        visible=False,
        opacity=0,
        animate_opacity=300,
        bgcolor=COLORS["accent"],
        border_radius=12,
        padding=15,
        width=420,
        bottom=30,
        right=30,
        content=ft.Row(
            [
                notification_text,
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_size=18,
                    tooltip="Закрыть",
                    on_click=lambda e: hide_notification(e.page),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    return container


# создаём один экземпляр
notification_container = create_notification()

def show_notification(page: ft.Page, message: str, is_error=False):
    """Показать уведомление"""

    notification_text.value = message
    notification_text.color = (
        ft.Colors.PINK_400 if is_error else COLORS["light_blue"]
    )

    notification_container.visible = True
    notification_container.opacity = 1

    # добавляем в overlay если ещё нет
    if notification_container not in page.overlay:
        page.overlay.append(notification_container)

    page.update()

    # авто-скрытие через 3 сек
    timer = threading.Timer(3.0, lambda: hide_notification(page))
    timer.start()


def hide_notification(page: ft.Page):
    """Скрыть уведомление"""

    notification_container.opacity = 0
    page.update()

    def remove():
        notification_container.visible = False
        page.update()

    threading.Timer(0.3, remove).start()