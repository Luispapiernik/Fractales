from itertools import product

from PIL import ImageDraw

from fractals.cartesian import CartesianImage
from fractals.schemas import Color


class Sierpinski:
    def __init__(self, image, tiles_color):
        self.drawer = ImageDraw.ImageDraw(image)
        self.tiles_color = tiles_color

    def generate_carpet(self, recursion_level, topleft_corner, length):
        if recursion_level:
            x, y = topleft_corner
            nlength = length // 3
            x0, y0 = x + nlength, y + nlength
            self.drawer.rectangle(
                [x0, y0, x0 + nlength, y0 + nlength],
                self.tiles_color, self.tiles_color
            )

            for i, j in product([0, 1, 2], [0, 1, 2]):
                self.generate_carpet(
                    recursion_level - 1,
                    (x + i * nlength, y + j * nlength),
                    nlength
                )


def sierpinski(
    *,
    length: int,
    background_color: Color = 0,
    color: Color = 255,
    mode: str = "L",
    max_iteration: int = 3,
):
    sierpinski_image = CartesianImage(
        width=length,
        height=length,
        color=background_color,
        mode=mode,
    )

    sierpinski_carpet = Sierpinski(sierpinski_image, tiles_color=color)
    sierpinski_carpet.generate_carpet(
        recursion_level=max_iteration, topleft_corner=(0, 0), length=length
    )

    return sierpinski_image
