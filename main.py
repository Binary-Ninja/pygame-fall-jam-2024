#!/usr/bin/env python3
import asyncio
import sys
import platform
from collections.abc import Sequence

import pygame as pg

from draw import Color, Image, draw, draw_text

pg.init()

# Declare globals.

# Load assets.

# Set up browser.
IN_BROWSER = sys.platform == "emscripten"
if IN_BROWSER:
    platform.document.body.style.background = f"#{int(Color.LIGHT_GRAY):08x}"  # noqa
    platform.window.canvas.style.imageRendering = "pixelated"  # noqa


def create_favicon(size: tuple[int, int], pos: tuple[int, int], image: str, colors: Sequence[pg.Color]):
    surf = pg.Surface(size)
    draw(surf, pos, image, colors)
    surf = pg.transform.scale(surf, (32, 32))
    pg.image.save(surf, "favicon.png")


async def main():
    pg.display.set_caption("Dungeon 64")
    # create_favicon((4, 4), (0, 0), Image.GEM, (Color.DARK_RED, Color.RED, Color.WHITE))
    pg.display.set_icon(pg.image.load("favicon.png"))
    flags = 0 if IN_BROWSER else pg.SCALED
    screen = pg.display.set_mode((64, 64), flags=flags)
    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick()

        screen.fill(Color.BLACK)
        # Draw the checkerboard.
        for x in range(16):
            for y in range(16):
                if (x + y) % 2 == 0:
                    screen.fill(Color.DARK_GRAY, (x * 4, y * 4, 4, 4))
        # Draw test image.
        draw(screen, (4, 0), Image.GEM, (Color.DARK_RED, Color.RED, Color.WHITE))
        # Draw test text.
        draw_text(screen, (0, 0), "hello world", Color.YELLOW)

        pg.display.flip()
        await asyncio.sleep(0)

    pg.quit()


if __name__ == '__main__':
    asyncio.run(main())
