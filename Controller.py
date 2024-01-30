import pygame as pg
import numpy as np
from ObjectPackage.Constants import *
from ObjectPackage import FieldScaler as fl

# set up the init of pygame
pg.init()

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Electric Field Sim")


def main():
    # will cause sim to repeat until user x out of sim
    run = True

    # sets a max frame rate
    clock = pg.time.Clock()

    # create a grid of scaler points
    field_scalars = []

    for x in np.linspace(-(WIDTH / 2), (WIDTH / 2), NUM_OF_POINTS + 2):
        for y in np.linspace(-(WIDTH / 2), (WIDTH / 2), NUM_OF_POINTS + 2):
            point = fl.FieldScaler(x, y)
            field_scalars.append(point)


    point_charges = []

    while run:
        # max fps
        clock.tick(FRAME_RATE)

        WIN.fill(BLACK)

        # test shapes
        # pg.draw.polygon(WIN, BLUE, ((SCALER_SIZE + WIDTH / 4, WIDTH / 4),
        #                             (WIDTH / 4- SCALER_SIZE, WIDTH / 4))
        #                 , SCALER_THICKNESS)
        #
        # pg.draw.polygon(WIN, RED, (((WIDTH / 2), (WIDTH / 2)),
        #                            ((WIDTH / 2), SCALER_SIZE + (WIDTH / 2)),
        #                            ((WIDTH / 2), (WIDTH / 2)),
        #                            (SCALER_SIZE + (WIDTH / 2), (WIDTH / 2)),
        #                            ((WIDTH / 2), (WIDTH / 2)),
        #                            ((WIDTH / 2), (WIDTH / 2) - SCALER_SIZE),
        #                            ((WIDTH / 2), (WIDTH / 2)),
        #                            ((WIDTH / 2) - SCALER_SIZE, (WIDTH / 2))
        #                            )
        #                 , SCALER_THICKNESS)
        #
        # pg.draw.circle(WIN, GREEN, (WIDTH / 3,WIDTH / 3),CHARGE_SIZE)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        for point in field_scalars:
            point.update_point(point_charges)
            point.draw(WIN)

        pg.display.update()

    pg.quit()
