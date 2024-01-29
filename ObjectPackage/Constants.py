# width and height of sim window
import math

WIDTH: int = 800
HEIGHT: int = 800

# size of point charge
CHARGE_SIZE = 5

# max frame rate of sim
FRAME_RATE: int = 60

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Physical Constants
VACUUM_PERMITTIVITY = 8.854E-12
COULOMB_CONST = 1/(4*math.pi*VACUUM_PERMITTIVITY)
