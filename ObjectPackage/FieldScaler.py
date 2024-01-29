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

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.E: float = 0
        self.colour = GREEN

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

    def cal_size_of_point(self):
        # cal the shape, size and colour of point

        if self.E > 0.0:  # positive
            self.colour = RED
        elif self.E < 0.0:  # negative
            self.colour = BLUE
        else:  # 0
            self.colour = GREEN

        pass

    def update_point(self, charges):
        total_E = 0
        for charge in charges:
            total_E += self.cal_E(charge)

        ## calulate size of shape here or have
