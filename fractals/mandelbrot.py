import time
from itertools import product
from math import isclose, log
from multiprocessing import Pool, cpu_count
from numbers import Real
from typing import Optional, Tuple, Union

import numpy as np

from fractals.cartesian import CartesianArray

Coordinate = Tuple[Real, Real]
Color = Union[int, str, Tuple[int, int, int], Tuple[int, int, int]]


class MandelbrotSet:
    def __init__(self, max_iteration, escape_radius=2, smooth=False):
        self.max_iteration = max_iteration
        self.scape_radius_squared = escape_radius ** 2
        self.smooth = smooth

    def get_scape_velocity(self, position: Coordinate):
        x, y = 0, 0
        for iteration in range(self.max_iteration):
            if x ** 2 + y ** 2 > self.scape_radius_squared:
                if self.smooth:
                    iteration = (
                        iteration + 1 - log(log((x * x + y * y) ** 0.5)) / log(2)
                    )
                return iteration

            x, y = x ** 2 - y ** 2 + position[0], 2 * x * y + position[1]

        return self.max_iteration

    def get_escape_rate(self, position: Coordinate):
        return self.get_scape_velocity(position) / self.max_iteration


def mandelbrot(
    *,
    width: int,
    height: int,
    x_interval: Coordinate = (-2, 2),
    y_interval: Coordinate = (-2, 2),
    color: Color = 0,
    mode: str = "L",
    palette: Optional[str] = None,
    processes: Optional[int] = None,
    max_iteration: int = 256,
    escape_radius: int = 2,
    smooth: bool = False,
    invert=False,
    verbose: int = 0,
):
    verbose_level = [0, 20, 10, 5, 2, 1][min(5, verbose)]
    mandelbrot_image = CartesianArray(
        width=width,
        height=height,
        x_interval=x_interval,
        y_interval=y_interval,
        color=color,
        mode=mode,
    )

    mandelbrot_set = MandelbrotSet(
        max_iteration=max_iteration, escape_radius=escape_radius, smooth=smooth
    )

    is_vertical_symmetric = isclose(
        abs(y_interval[0]), abs(y_interval[1]), rel_tol=1e-09, abs_tol=0.0
    )
    real_height = int(height // 2) + (height & 1) if is_vertical_symmetric else height

    processes = processes or cpu_count()
    with Pool(processes=processes) as pool:
        scape_velocities_iterable = pool.imap(
            mandelbrot_set.get_escape_rate,
            map(
                lambda pos: mandelbrot_image.get_coordinate(row=pos[0], column=pos[1]),
                product(range(real_height), range(width)),
            ),
            (width * real_height) // 25,
        )

        escape_velocities = []
        for escape_rate in scape_velocities_iterable:
            if invert:
                escape_rate = 1 - escape_rate

            escape_velocities.append(int(255 * escape_rate))

            if verbose:
                percent = 100 * len(escape_velocities) / (real_height * width)
                if isclose(percent % verbose_level, 0, rel_tol=0.1):
                    print(f"Getting escape rates, {percent}% finished ...")

    if mandelbrot_image.channels == 1:
        array = np.array(escape_velocities).reshape(real_height, width)
        mandelbrot_image.write_sub_array(x_offset=0, y_offset=0, array=array)

        if is_vertical_symmetric:
            flipped_array = np.flip(
                array[
                    (height & 1):,
                ],
                axis=0,
            )
            mandelbrot_image.write_sub_array(
                x_offset=0, y_offset=real_height, array=flipped_array
            )

    image = mandelbrot_image.get_image()
    if mode == "P":
        image.putpalette(palette)

    image.save("mandelbrot.png")
    return image


def test_1():
    start = time.time()
    mandelbrot(
        width=512,
        height=512,
        mode="L",
        palette="turbo",
        max_iteration=20,
        smooth=True,
        escape_radius=1000,
        invert=True,
    )
    end = time.time()
    print(f"TIME 1: {end - start}")


def test_2():
    mandelbrot = MandelbrotSet(max_iteration=256)

    print(mandelbrot.get_scape_velocity((1, 0)))


def example_1():
    mandelbrot(
        width=512,
        height=512,
        mode="L",
        max_iteration=20,
        smooth=True,
        escape_radius=1000,
        invert=True,
    )


def example_2():
    mandelbrot(
        width=512,
        height=512,
        mode="P",
        palette="turbo",
        max_iteration=256,
        smooth=True,
        escape_radius=1000,
        invert=False,
        x_interval=(-0.7455, -0.7415),
        y_interval=(0.1294, 0.1334),
    )


def main():
    test_1()


if __name__ == "__main__":
    main()
