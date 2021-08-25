class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""


import math


def calc_square(ab, bc, ca):
    if ab <= 0 or bc <= 0 or ca <= 0:
        raise InvalidTriangleError('One of the sides is less or equal to 0.')
    p = (ab + bc + ca) / 2
    s = math.sqrt(p * (p - ab) * (p - ca) * (p - bc))

    return s


try:
    square = calc_square(4, 4, 6)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(square)
