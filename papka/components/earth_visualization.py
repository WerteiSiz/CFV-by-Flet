import flet as ft
import math


class EarthVisualization(ft.Control):
    def __init__(self, wavelength=None, frequency=None,
                 atmosphere_loss=None, elevation_angle=None):
        super().__init__()
        self.wavelength = wavelength
        self.frequency = frequency
        self.atmosphere_loss = atmosphere_loss
        self.elevation_angle = elevation_angle
        self.canvas = None

    def build(self):
        """Построение компонента"""
        self.canvas = ft.Canvas(
            width=500,
            height=500,
            shapes=[],
        )

        self.draw_earth()

        return ft.Container(
            content=self.canvas,
            width=520,
            height=520,
            bgcolor=ft.colors.with_opacity(0.03, ft.colors.BLUE_GREY_100),
            border_radius=16,
            padding=10,
        )

    def draw_earth(self):
        """Отрисовка всех элементов"""
        center_x = 250
        center_y = 250
        earth_radius = 100

        shapes = []

        # 1. ПЛАНЕТА ЗЕМЛЯ
        shapes.append(
            ft.canvas.Circle(
                center_x, center_y, earth_radius,
                ft.Paint(
                    gradient=ft.PaintRadialGradient(
                        center=ft.Offset(0.3, 0.3),
                        radius=1.0,
                        colors=[
                            "#4A9EFF",
                            "#2563EB",
                            "#1E40AF",
                        ],
                    ),
                ),
            )
        )

        # 2. СЕТКА КООРДИНАТ
        # Вертикальные линии (меридианы)
        for i in range(-2, 3):
            x_offset = i * 25
            # Рисуем кривую как Path
            path_elements = []

            # Создаем точки для кривой
            for angle in range(0, 361, 10):
                angle_rad = math.radians(angle)
                x = center_x + x_offset + math.sin(angle_rad) * 5
                y = center_y + math.cos(angle_rad) * earth_radius

                if angle == 0:
                    path_elements.append(ft.canvas.Path.MoveTo(x, y))
                else:
                    path_elements.append(ft.canvas.Path.LineTo(x, y))

            shapes.append(
                ft.canvas.Path(
                    path_elements,
                    ft.Paint(
                        stroke_width=1,
                        style=ft.PaintingStyle.STROKE,
                        color=ft.colors.with_opacity(0.3, ft.colors.WHITE),
                    ),
                )
            )

        # Горизонтальные линии (параллели)
        for i in range(-2, 3):
            y = center_y + i * 25
            if abs(i * 25) <= earth_radius:
                width = math.sqrt(earth_radius ** 2 - (i * 25) ** 2)
                shapes.append(
                    ft.canvas.Arc(
                        center_x - width, y - 4,
                        width * 2, 8,
                        0, math.pi * 2,
                        False,
                        ft.Paint(
                            stroke_width=1,
                            style=ft.PaintingStyle.STROKE,
                            color=ft.colors.with_opacity(0.3, ft.colors.WHITE),
                        ),
                    )
                )

        # 3. АТМОСФЕРНЫЕ СЛОИ
        layers_data = [
            (120, "#7C3AED", "Тропосфера"),
            (140, "#2563EB", "Стратосфера"),
            (160, "#60A5FA", "Мезосфера"),
        ]

        for idx, (radius, color, name) in enumerate(layers_data):
            # Пунктирный круг
            for angle in range(0, 360, 10):
                angle_rad = math.radians(angle)
                next_angle_rad = math.radians(angle + 5)

                x1 = center_x + radius * math.cos(angle_rad)
                y1 = center_y + radius * math.sin(angle_rad)
                x2 = center_x + radius * math.cos(next_angle_rad)
                y2 = center_y + radius * math.sin(next_angle_rad)

                shapes.append(
                    ft.canvas.Line(
                        x1, y1, x2, y2,
                        ft.Paint(
                            stroke_width=2,
                            color=ft.colors.with_opacity(0.15, color),
                        ),
                    )
                )

            # Подпись слоя
            shapes.append(
                ft.canvas.Text(
                    center_x + radius + 10,
                    center_y - 50 + idx * 25,
                    name,
                    ft.TextStyle(
                        size=11,
                        color="#7C3AED",
                        weight=ft.FontWeight.W_500,
                    ),
                )
            )

        # 4. СПУТНИК
        satellite_x = center_x + 180
        satellite_y = center_y - 120

        # Свечение спутника
        for r in range(20, 5, -3):
            opacity = 0.3 - (r / 100)
            shapes.append(
                ft.canvas.Circle(
                    satellite_x, satellite_y, r,
                    ft.Paint(
                        color=ft.colors.with_opacity(opacity, "#A78BFA"),
                    ),
                )
            )

        # Сам спутник
        shapes.append(
            ft.canvas.Circle(
                satellite_x, satellite_y, 8,
                ft.Paint(color="#A78BFA"),
            )
        )

        # Солнечные панели
        shapes.append(
            ft.canvas.Rect(
                satellite_x - 20, satellite_y - 3, 15, 6,
                ft.Paint(color="#60A5FA"),
            )
        )
        shapes.append(
            ft.canvas.Rect(
                satellite_x + 5, satellite_y - 3, 15, 6,
                ft.Paint(color="#60A5FA"),
            )
        )

        # 5. ЗЕМНАЯ СТАНЦИЯ
        if self.elevation_angle:
            angle_rad = math.radians(self.elevation_angle) + math.pi
        else:
            angle_rad = math.pi / 4 + math.pi

        station_x = center_x + earth_radius * math.cos(angle_rad)
        station_y = center_y + earth_radius * math.sin(angle_rad)

        # Красная точка станции
        shapes.append(
            ft.canvas.Circle(
                station_x, station_y, 6,
                ft.Paint(color="#EF4444"),
            )
        )

        # Антенна станции
        shapes.append(
            ft.canvas.Line(
                station_x, station_y,
                station_x - 15, station_y - 15,
                ft.Paint(
                    stroke_width=2,
                    color="#EF4444",
                ),
            )
        )

        # 6. ЛИНИЯ СВЯЗИ (пунктирная)
        num_segments = 20
        for i in range(num_segments):
            if i % 2 == 0:  # Рисуем только четные сегменты для пунктира
                t1 = i / num_segments
                t2 = (i + 1) / num_segments

                x1 = station_x + (satellite_x - station_x) * t1
                y1 = station_y + (satellite_y - station_y) * t1
                x2 = station_x + (satellite_x - station_x) * t2
                y2 = station_y + (satellite_y - station_y) * t2

                # Интерполяция цвета
                shapes.append(
                    ft.canvas.Line(
                        x1, y1, x2, y2,
                        ft.Paint(
                            stroke_width=2,
                            color=ft.colors.with_opacity(0.6, "#A78BFA"),
                        ),
                    )
                )

        # 7. ТЕКСТОВЫЕ ПАРАМЕТРЫ
        params = []
        if self.wavelength is not None:
            params.append((f"λ = {self.wavelength:.4f} м", center_x - 100, center_y - 180, "#7C3AED"))
        if self.frequency is not None:
            params.append((f"f = {self.frequency:.2f} ГГц", center_x + 50, center_y - 180, "#2563EB"))
        if self.atmosphere_loss is not None:
            params.append((f"L_atm = {self.atmosphere_loss:.2f} дБ", center_x - 50, center_y + 180, "#A78BFA"))

        for text, x, y, color in params:
            # Фон для текста
            text_width = len(text) * 9
            shapes.append(
                ft.canvas.Rect(
                    x - 10, y - 20, text_width, 30, 8,
                    ft.Paint(
                        color=ft.colors.with_opacity(0.95, ft.colors.WHITE),
                    ),
                )
            )
            shapes.append(
                ft.canvas.Rect(
                    x - 10, y - 20, text_width, 30, 8,
                    ft.Paint(
                        stroke_width=2,
                        style=ft.PaintingStyle.STROKE,
                        color=color,
                    ),
                )
            )

            # Текст
            shapes.append(
                ft.canvas.Text(
                    x, y + 5,
                    text,
                    ft.TextStyle(
                        size=13,
                        color=color,
                        weight=ft.FontWeight.BOLD,
                        font_family="JetBrains Mono",
                    ),
                )
            )

        # Применяем все фигуры
        self.canvas.shapes = shapes

    def update_values(self, wavelength=None, frequency=None,
                      atmosphere_loss=None, elevation_angle=None):
        """Обновление значений и перерисовка"""
        if wavelength is not None:
            self.wavelength = wavelength
        if frequency is not None:
            self.frequency = frequency
        if atmosphere_loss is not None:
            self.atmosphere_loss = atmosphere_loss
        if elevation_angle is not None:
            self.elevation_angle = elevation_angle

        self.draw_earth()
        if self.canvas:
            self.canvas.update()
