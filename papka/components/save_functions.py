import flet as ft
import math
import os
from openpyxl import Workbook
from openpyxl.styles import Alignment as OpenPyXLAlignment, Border, Side
from datetime import datetime
from docx import Document
from docx.shared import Pt  # Для работы с размерами шрифта
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT  # Для выравнивания текста
from papka.ui  import gradys_d_input, gradys_sh_input, tochka_input, chastota_input, chastota1_input, diametr_input, k_input, P_input, T_input, p_input
from papka.ui import create_input_field
from .calculations import ygol_mesta, azimut, dalnost, poteri, factorG, atmosphere
from .constants import R3, H, COLORS
from papka.components.input_fields import *
from papka.components.message import *

def save_result_txt(e):
    try:
        gradys_d = float(gradys_d_input.value)
        gradys_sh = float(gradys_sh_input.value)
        tochka = float(tochka_input.value)
        chastota = float(chastota_input.value)
        diametr = float(diametr_input.value)
        k = float(k_input.value)
        P = float(P_input.value)
        T = float(T_input.value)
        p = float(p_input.value)

        angle_of_elevation = ygol_mesta(gradys_d, gradys_sh, tochka)
        azimuth_angle = azimut(gradys_d, gradys_sh, tochka)
        distance = dalnost(gradys_d, gradys_sh, tochka)
        signal_loss = round(poteri(chastota, diametr, k, tochka), 3)
        gain = round(factorG(chastota, k, diametr), 3)
        atmos = round(atmosphere(chastota, gradys_d, gradys_sh, tochka, T, p, P), 3)

        result_text = f"""
   ╔════════════════════════════════╗
   ║       ОТЧЕТ О РАСЧЕТАХ        ║
   ╠════════════════════════════════╣
   ║  ВХОДНЫЕ ДАННЫЕ               ║
   ║  • Широта: {gradys_sh:>12}°       ║
   ║  • Долгота: {gradys_d:>11}°       ║
   ║  • Точка стояния: {tochka:>6}°       ║
   ║  • Диаметр антенны: {diametr:>5.2f} м     ║
   ║  • Коэффициент: {k:>10.2f}       ║
   ║  • Давление: {P:>11.2f} кПа    ║
   ║  • Температура: {T:>8.2f} °K   ║
   ║  • Влажность: {p:>10.2f} г/м³  ║
   ╠════════════════════════════════╣
   ║  РЕЗУЛЬТАТЫ                   ║
   ║  • Угол места: {angle_of_elevation:>8.2f}°       ║
   ║  • Азимут: {azimuth_angle:>12.2f}°       ║
   ║  • Дальность: {distance:>10.2f} км     ║
   ║  • Потери сигнала: {signal_loss:>6.2f} дБ ║
   ║  • Потери в атмосфере: {atmos:>4.2f} дБ ║
   ║  • Коэффициент усиления: {gain:>2.2f} дБ ║
   ╚════════════════════════════════╝
   """

        with open("Результаты_Расчётов.txt", "w", encoding="utf-8") as file:
            file.write(result_text)

        show_save_message("Данные сохранены в Результаты_Расчётов.txt")

    except ValueError:
        show_save_message("Ошибка: проверьте корректность данных", is_error=True)

def save_result_to_word(e):
    try:
        gradys_d = float(gradys_d_input.value)
        gradys_sh = float(gradys_sh_input.value)
        tochka = float(tochka_input.value)

        angle_of_elevation = ygol_mesta(gradys_d, gradys_sh, tochka)
        azimuth_angle = azimut(gradys_d, gradys_sh, tochka)
        distance = dalnost(gradys_d, gradys_sh, tochka)

        result_text = f"""Результаты Вычислений:
                  Ваши входные данные:
                      Градусы широты: {gradys_sh}°
                      Градусы Долготы: {gradys_d}°
                      Значение Точки стояния спутника: {tochka}°


                  Результаты Позиционирования:
                      Угол места: {angle_of_elevation:.2f}°
                      Азимут: {azimuth_angle:.2f}°
                      Наклонная дальность: {distance:.2f} км
                          ~~~~~~~~~~~~~~~~~~
               Спасибо, что пользуетесь нашей системой расчётов!"""

        user_input = result_text

        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop_path, "output.docx")

        doc = Document()
        doc.add_paragraph(user_input)
        doc.save(file_path)

        with open("Результаты_Расчётов.doc", "w") as file:
            file.write(result_text)
        show_save_message("Данные сохранены в файл Результаты_Расчётов.doc")
    except ValueError:
        show_save_message("Пожалуйста, введите корректные данные", is_error=True)


