#!/usr/bin/env python3
import asyncio
import sys
import platform

import pygame as pg


pg.init()

# Declare globals.
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

# Load assets.

# Set up browser.
IN_BROWSER = sys.platform == "emscripten"
if IN_BROWSER:
    platform.document.body.style.background = f"#{int(Color.LIGHT_GRAY):08x}"  # noqa
    platform.window.canvas.style.imageRendering = "pixelated"  # noqa


async def main():
    flags = 0 if IN_BROWSER else pg.SCALED
    pg.display.set_caption("Dungeon 64")
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

        pg.display.flip()
        await asyncio.sleep(0)

    pg.quit()


if __name__ == '__main__':
    asyncio.run(main())
