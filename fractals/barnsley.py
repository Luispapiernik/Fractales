from random import random

from fractals.cartesian import CartesianImage
from fractals.schemas import Color, Coordinate


class Barnsley:
    def __init__(self,
        a_1=0, b_1=0, c_1=0, d_1=0.16, e_1=0, f_1=0,
        a_2=0.85, b_2=0.04, c_2=-0.04, d_2=0.85, e_2=0, f_2=1.6,
        a_3=0.2, b_3=-0.26, c_3=0.23, d_3=0.22, e_3=0, f_3=1.6,
        a_4=-0.15, b_4=0.28, c_4=0.26, d_4=0.24, e_4=0, f_4=0.44,
    ) -> None:
        self.a_1 = a_1
        self.b_1 = b_1
        self.c_1 = c_1
        self.d_1 = d_1
        self.e_1 = e_1
        self.f_1 = f_1
        self.a_2 = a_2
        self.b_2 = b_2
        self.c_2 = c_2
        self.d_2 = d_2
        self.e_2 = e_2
        self.f_2 = f_2
        self.a_3 = a_3
        self.b_3 = b_3
        self.c_3 = c_3
        self.d_3 = d_3
        self.e_3 = e_3
        self.f_3 = f_3
        self.a_4 = a_4
        self.b_4 = b_4
        self.c_4 = c_4
        self.d_4 = d_4
        self.e_4 = e_4
        self.f_4 = f_4

    def transform(self, x, y, index=1):
        a = getattr(self, f"a_{index}")
        b = getattr(self, f"b_{index}")
        c = getattr(self, f"c_{index}")
        d = getattr(self, f"d_{index}")
        e = getattr(self, f"e_{index}")
        f = getattr(self, f"f_{index}")

        return a * x + b * y + e, c * x + d * y + f


def barnsley(
    *,
    width: int,
    height: int,
    x_interval: Coordinate = (-2.7, 2.7),
    y_interval: Coordinate = (0, 11),
    background_color: Color = 0,
    color: Color = 255,
    mode: str = "L",
    max_iteration: int = 10000,
):
    barnsley_image = CartesianImage(
        width=width,
        height=height,
        x_interval=x_interval,
        y_interval=y_interval,
        color=background_color,
        mode=mode,
    )

    barnsley_transformations = Barnsley()

    x, y = 0, 0
    for _ in range(max_iteration):
        i, j = barnsley_image.get_position(x=x, y=y)
        if (0 <= i < width) and (0 <= j < height):
            barnsley_image.putpixel(position=(i, j), color=color, to_int=False)

        rand = random()
        if rand < 0.01:
            x, y = barnsley_transformations.transform(x, y, index=1)
        elif rand < 0.86:
            x, y = barnsley_transformations.transform(x, y, index=2)
        elif rand < 0.92:
            x, y = barnsley_transformations.transform(x, y, index=3)
        else:
            x, y = barnsley_transformations.transform(x, y, index=4)

    return barnsley_image
