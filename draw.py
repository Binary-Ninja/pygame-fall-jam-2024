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


class Image:
    GEM = (" 00 \n"
           "0  0\n"
           "0  0\n"
           " 00 ")
