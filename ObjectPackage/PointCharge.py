from Constants import *
import pygame as pg
import math


class PointCharge:
    """
    Object for the point charge
    the user controls the position of new point chargers are made
    and if they are +ve or -ve
    """

    def __init__(self, x, y, q) -> None:
        """
        init for a point charge
        :param x: x positon
        :param y: y positon
        :param q: charge of point charge, either 1 or -1 c
        """
        self.x = x
        self.y = y
        self.q = q
        if q > 0:  # positive
            self.colour = RED
        else:  # negative
            self.colour = BLUE

    def draw(self, win) -> None:
        pg.draw.circle(win, self.colour, (int(self.x), int(self.y)), CHARGE_SIZE)
