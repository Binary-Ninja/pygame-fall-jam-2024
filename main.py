#!/usr/bin/env python3
import asyncio
import sys
import platform

import pygame as pg

from draw import Color, Image, draw


pg.init()

# Declare globals.

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
        # Draw test image.
        draw(screen, (4, 0), Image.GEM, (Color.RED,))

        pg.display.flip()
        await asyncio.sleep(0)

    pg.quit()


if __name__ == '__main__':
    asyncio.run(main())
