#!/usr/bin/env python3
import asyncio
import sys
import platform

import pygame as pg


IN_BROWSER = sys.platform == "emscripten"
if IN_BROWSER:
    platform.document.body.style.background = "#FFFF00"  # noqa


# Declare globals.
# Load assets.


async def main():
    pg.init()
    flags = 0 if IN_BROWSER else pg.SCALED
    screen = pg.display.set_mode((64, 64), flags=flags)
    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick()
        screen.fill((255, 0, 255))
        # screen.fill((255, 0, 0), (0, 0, 1, 1))
        pg.display.flip()

        await asyncio.sleep(0)

    pg.quit()


if __name__ == '__main__':
    asyncio.run(main())
