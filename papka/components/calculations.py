import math

R3 = 6378.0   # Радиус Земли (км)
H = 35810.0   # Высота орбиты (км)

def _geometry(gradys_d, gradys_sh, tochka):
    """Общие геометрические параметры (без global)."""

    delta_y = gradys_d - tochka
    cos_delta_y = math.cos(math.radians(delta_y))
    cosinusFi = math.cos(math.radians(gradys_sh))

    cosinustri = cosinusFi * cos_delta_y
    y0 = R3 / (R3 + H)

    return delta_y, cosinustri, y0

def ygol_mesta(gradys_d, gradys_sh, tochka):

    _, cosinustri, y0 = _geometry(gradys_d, gradys_sh, tochka)

    c = cosinustri - y0
    e = math.sqrt(1 - cosinustri ** 2)

    res = math.atan(c / e)
    return math.degrees(res)

def azimut(gradys_d, gradys_sh, tochka):

    delta_y, _, _ = _geometry(gradys_d, gradys_sh, tochka)

    tangens_delta_y = math.tan(math.radians(delta_y))
    sinus_fi = math.sin(math.radians(gradys_sh))

    arct = math.atan(tangens_delta_y / sinus_fi)
    return math.degrees(arct) + 180

def dalnost(gradys_d, gradys_sh, tochka):

    _, cosinustri, y0 = _geometry(gradys_d, gradys_sh, tochka)

    sl_pdk = 1 + y0**2 - 2 * y0 * cosinustri
    koren = math.sqrt(sl_pdk)

    drop3 = koren / y0
    d = R3 * drop3

    return d

def poteri(chastota, gradys_d, gradys_sh, tochka):

    d = dalnost(gradys_d, gradys_sh, tochka)

    wavelength = 3e8 / (chastota * 1e9)

    drop = math.log10((4 * math.pi * d * 1000) / wavelength)
    L = 20 * drop

    return L

def factorG(chastota, k, diametr):

    wavelength = 3e8 / (chastota * 1e9)

    drop = ((math.pi * diametr) / wavelength) ** 2
    G = 10 * math.log10(k * drop)

    return G

def atmosphere(chastota, gradys_d, gradys_sh, tochka, T, p, P):

    elevation = ygol_mesta(gradys_d, gradys_sh, tochka)

    h3 = 0.02

    l1 = 5.98 / math.sin(math.radians(elevation))

    delta1 = 0.0126 / T ** 0.75
    delta2 = 0.035 / T ** 0.75
    deltas = 0.0153 * (1 + 0.0046 * p) / (T ** 0.5)

    drop6 = 1 / (chastota - 183.3) ** 2
    drop7 = 1 / (chastota - 323.8) ** 2
    drop8 = 3 / ((chastota - 22.3) ** 2 + 3)

    hh20 = drop6 + drop7 + 2.2 + drop8

    l2 = (hh20 - h3) / math.sin(math.radians(elevation))

    drop9 = chastota**2 / T**2
    drop10 = P * delta2

    drop12 = drop10 / ((2 - chastota / 30) ** 2 + drop10**2)
    drop13 = P * delta1
    drop15 = drop13 / (drop13**2 + chastota**2 / 900)

    drop17 = drop10 / ((2 + chastota / 30) ** 2 + drop10**2)

    l0 = 0.321 * P * drop9 * (drop12 + drop15 + drop17)

    drop18 = P * deltas * p / T

    lh20 = 5.72 * p * chastota**2 * math.exp(644 / T) / T**2.5
    lh20 *= drop18

    latmosphere = (l0 * l1) + (lh20 * l2)

    return latmosphere
