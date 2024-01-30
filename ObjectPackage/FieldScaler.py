# from a scale from -1 to 1
# will shrink in size based on the abs size of the field at that point
# +ve being positive field and -ve being negative field
# it will also change sign based on if the point is negative or positive
from Constants import *
import pygame as pg
import math


class FieldScaler:
    """
    Object for the Field Scaler
    created in a grid of points
    with change in size and shape based on the Electric field strength
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.E: float = 0.0
        self.colour = GREEN
        self.size = SCALER_SIZE

    def cal_E(self, charge) -> float:
        """
        Method to cal the E field from point charges in the system
        :param charge: point charge object
        :return: the Electric field
        """
        charge_x, charge_y = charge.x, charge.y
        distance_x = charge_x - self.x
        distance_y = charge_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        E = COULOMB_CONST * charge.q / distance ** 2

        # vector E
        # theta = math.atan2(distance_y, distance_x)
        # E_x = math.cos(theta) * E
        # E_y = math.sin(theta) * E

        return E

    def cal_size_of_point(self) -> None:
        """
        cal the size of field scaler point
        """
        # colour
        if self.E == 0.0:  # 0
            self.size = SCALER_THICKNESS
            return
        # size
        self.size = abs(self.E) * SCALER_SIZE

    def update_point(self, charges: list) -> None:
        """
        update the scaler point for each frame of the sim
        :param charges: each point charge in the sim in a list
        """
        total_E = 0
        for charge in charges:
            total_E += self.cal_E(charge)

        self.E = total_E
        self.cal_size_of_point()
        ## calulate size of shape here or have

    def draw(self, win) -> None:
        # pygame sets 0,0 to top left
        x = self.x + (WIDTH / 2)
        y = self.y + (HEIGHT / 2)

        if self.E > 0.0:  # positive
            # +ve plus sign
            pg.draw.polygon(win, RED, ((x, y),
                                       (x, self.size + y),
                                       (x, y),
                                       (self.size + x, y),
                                       (x, y),
                                       (x, y - self.size),
                                       (x, y),
                                       (x - self.size, y)
                                       )
                            , SCALER_THICKNESS)

        elif self.E < 0.0:  # negative
            pg.draw.polygon(win, BLUE, ((self.size + x, y),
                                        (x - self.size, y))
                            , SCALER_THICKNESS)
        else:  # 0
            pg.draw.circle(win, GREEN, (x, y), self.size)


