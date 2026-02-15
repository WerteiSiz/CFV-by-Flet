import math

# глобальные параметры (используются внутри функций через global)
R3 = 6378.0  # Радиус Земли
H = 35810.0  # Высота орбиты


def ygol_mesta(gradys_d, gradys_sh, tochka):
    global R3, H, delta_y, cos_delta_y, cosinusFi, cosinustri, y0, c, e, drop, res_ygol
    R3 = 6378.0
    H = 35810.0
    delta_y = gradys_d - tochka
    cos_delta_y = math.cos(math.radians(delta_y))
    cosinusFi = math.cos(math.radians(gradys_sh))
    cosinustri = cosinusFi * cos_delta_y
    y0 = (R3 / (R3 + H))
    c = cosinustri - y0
    e = math.sqrt(1 - (cosinustri ** 2))
    drop = c / e
    res = math.atan(drop)
    res_ygol = math.degrees(res)
    return res_ygol


def azimut(gradys_d, gradys_sh, tochka):
    tangens_delta_y = math.tan(math.radians(delta_y))
    sinus_fi = math.sin(math.radians(gradys_sh))
    drop2 = tangens_delta_y / sinus_fi
    arct = math.atan(drop2)
    arct_res = math.degrees(arct) + 180
    return arct_res


def dalnost(gradys_d, gradys_sh, tochka):
    global d, sl_pdk, koren, drop3
    sl_pdk = 1 + y0 ** 2 - 2 * y0 * cosinustri
    koren = math.sqrt(sl_pdk)
    drop3 = koren / y0
    d = R3 * drop3
    return d


def poteri(chastota, diametr, k, tochka):
    global lenth
    global d, sl_pdk, koren, drop3
    sl_pdk = 1 + y0 ** 2 - 2 * y0 * cosinustri
    koren = math.sqrt(sl_pdk)
    drop3 = koren / y0
    d = R3 * drop3
    lenth = (3 * 10 ** 8 / (chastota * 10 ** 9))
    drop4 = math.log10((4 * math.pi * d * 1000) / lenth)
    L = 20 * drop4
    return L


def factorG(chastota, k, diametr):
    lenth = (3 * 10 ** 8 / (chastota * 10 ** 9))
    drop5 = ((math.pi * diametr) / lenth) ** 2
    G = 10 * math.log10(k * drop5)
    return G


def atmosphere(chastota, gradys_d, gradys_sh, tochka, T, p, P):
    global delta1, delta2, deltas, l1, l2, drooop, lh20, l0, drop16, drop11, drop14
    h0 = 6  # высота (км) в метрах
    h3 = 0.02
    l1 = (5.98 / (math.sin(math.radians(ygol_mesta(gradys_d, gradys_sh, tochka)))))
    delta1 = (0.0126 / T ** 0.75)
    delta2 = (0.035 / T ** 0.75)
    deltas = 0.0153 * (1 + 0.0046 * p) / (T ** 0.5)
    drop6 = 1 / (chastota - 183.3) ** 2
    drop7 = 1 / (chastota - 323.8) ** 2
    drop8 = 3 / ((chastota - 22.3) ** 2 + 3)
    hh20 = drop6 + drop7 + 2.2 + drop8
    l2 = ((hh20 - h3) / (math.sin(math.radians(ygol_mesta(gradys_d, gradys_sh, tochka)))))
    drooop = (hh20 - h3)
    drop9 = (chastota ** 2 / T ** 2)
    drop10 = P * delta2
    drop11 = (2 - (chastota / 30)) ** 2
    drop12 = (drop10 / drop11 + (drop10 ** 2))
    drop13 = P * delta1
    drop14 = chastota ** 2 / 900
    drop15 = (drop13 / (drop13 ** 2 + drop14))
    drop16 = (2 + (chastota / 30)) ** 2
    drop17 = (drop10 / (drop16 + drop10 ** 2))
    l0 = 0.321 * P * drop9 * (drop12 + drop15 + drop17)
    drop18 = P * deltas / ((-0.741 + (chastota / 30)) ** 2 + (deltas * P) ** 2)
    drop19 = P * deltas / ((0.741 + (chastota / 30)) ** 2 + (deltas * P) ** 2)
    drop20 = 644 / T
    drop21 = ((5.72 * p * chastota ** 2 * e ** drop20) / T ** 2.5)
    drop22 = (P * deltas * p) / T
    lh20 = (drop18 + 0.0163 * chastota ** 2 * drop22 + drop19) * drop21
    latmosphere = ((l0 * l1) + (lh20 * l2))
    return latmosphere
