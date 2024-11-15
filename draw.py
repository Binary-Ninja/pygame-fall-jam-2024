# This file holds the colors, images, and image drawing functions.
from collections.abc import Sequence

import pygame as pg


class Color:
    BLACK = pg.Color(0, 0, 0)
    DARK_GRAY = pg.Color(85, 85, 85)
    LIGHT_GRAY = pg.Color(170, 170, 170)
    WHITE = pg.Color(255, 255, 255)

    RED = pg.Color(255, 0, 0)
    GREEN = pg.Color(0, 255, 0)
    BLUE = pg.Color(0, 0, 255)
    CYAN = pg.Color(0, 255, 255)
    MAGENTA = pg.Color(255, 0, 255)
    YELLOW = pg.Color(255, 255, 0)

    DARK_RED = pg.Color(128, 0, 0)
    DARK_GREEN = pg.Color(0, 128, 0)
    DARK_BLUE = pg.Color(0, 0, 128)
    DARK_CYAN = pg.Color(0, 128, 128)
    DARK_MAGENTA = pg.Color(128, 0, 128)
    DARK_YELLOW = pg.Color(128, 64, 0)


text_images = {
    "A": " 0\n"
         "000\n"
         "0 0",
    "B": "00\n"
         "000\n"
         "00",
    "C": " 00\n"
         "0\n"
         " 00",
    "D": "00\n"
         "0 0\n"
         "00",
    "E": "000\n"
         "00\n"
         "000",
    "F": "000\n"
         "00\n"
         "0",
    "G": "00\n"
         "0 0\n"
         "000",
    "H": "0 0\n"
         "000\n"
         "0 0",
    "I": "000\n"
         " 0\n"
         "000",
    "J": "  0\n"
         "  0\n"
         "00",
    "K": "0 0\n"
         "00\n"
         "0 0",
    "L": "0\n"
         "0\n"
         "000",
    "M": "000\n"
         "000\n"
         "0 0",
    "N": "00\n"
         "0 0\n"
         "0 0",
    "O": "000\n"
         "0 0\n"
         "000",
    "P": "000\n"
         "000\n"
         "0",
    "Q": "000\n"
         "0 0\n"
         "00",
    "R": "00\n"
         "000\n"
         "0 0",
    "S": " 00\n"
         " 0\n"
         "00",
    "T": "000\n"
         " 0\n"
         " 0",
    "U": "0 0\n"
         "0 0\n"
         "000",
    "V": "0 0\n"
         "0 0\n"
         " 00",
    "W": "0 0\n"
         "000\n"
         "000",
    "X": "0 0\n"
         " 0\n"
         "0 0",
    "Y": "0 0\n"
         " 0\n"
         " 0",
    "Z": "00\n"
         " 0\n"
         " 00",
    "0": "000\n"
         "0 0\n"
         "000",
    "1": "00\n"
         " 0\n"
         "000",
    "2": "00\n"
         " 0\n"
         " 00",
    "3": "00\n"
         " 00\n"
         "00",
    "4": "0 0\n"
         "000\n"
         "  0",
    "5": " 00\n"
         " 0\n"
         "00",
    "6": "0\n"
         "000\n"
         "000",
    "7": "000\n"
         "  0\n"
         "  0",
    "8": "000\n"
         "000\n"
         "000",
    "9": "000\n"
         "000\n"
         "  0",
}


class Image:
    GEM = (" 11 \n"
           "1121\n"
           "0111\n"
           " 01 ")


def draw(surf: pg.Surface, pos: tuple[int, int], image_str: str, colors: Sequence[pg.Color]):
    with pg.PixelArray(surf) as pixels:
        x, y = pos
        for char in image_str:
            if char == "\n":
                x, y = pos[0], y + 1
                continue
            if char != " ":
                pixels[x, y] = colors[int(char)]
                pass
            x += 1


def draw_text(surf: pg.Surface, pos: tuple[int, int], text: str, color: pg.Color):
    x, y = pos
    for char in text:
        if char == "\n":
            x, y = pos[0], y + 4
            continue
        if image := text_images.get(char.upper()):
            draw(surf, (x, y), image, (color,))
        x += 4

