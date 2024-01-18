import pygame as pg

from ObjectPackage.Constants import *

# set up the init of pygame
pg.init()

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Electric Field Sim")


def main():
    # will cause sim to repeat until user x out of sim
    run = True

    # sets a max frame rate
    clock = pg.time.Clock()

    while run:
        # max fps
        clock.tick(FRAME_RATE)


        WIN.fill(BLACK)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

    pg.quit()




