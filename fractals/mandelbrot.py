import time
from itertools import product
from multiprocessing import Pool
from numbers import Real
from typing import Tuple

import numpy as np
from cartesian import CartesianArray

Coordinate = Tuple[Real, Real]


def get_scape_velocity(position: Coordinate):
    x, y = 0, 0
    iteration = 0
    while (x ** 2 + y ** 2 < 4) and (iteration < 4000):
        x, y = x ** 2 - y ** 2 + position[0], 2 * x * y + position[1]

        iteration += 1

    return iteration


def mandelbrot(
    *,
    width: int,
    height: int,
    x_interval: Coordinate = (-2, 2),
    y_interval: Coordinate = (-2, 2),
    color=0,
):
    mandelbrot_image = CartesianArray(
        width=width,
        height=height,
        x_interval=x_interval,
        y_interval=y_interval,
        color=color,
        mode="L",
    )

    with Pool(processes=8) as pool:
        scape_velocities = pool.map(
            get_scape_velocity,
            map(
                lambda pos: mandelbrot_image.get_coordinate(row=pos[0], column=pos[1]),
                product(range(int(height // 2) + 1), range(width)),
            ),
        )

    arr = np.array(scape_velocities).reshape(int(height // 2) + 1, width)
    mandelbrot_image.array = np.concatenate((arr, np.flip(arr, 0)))

    mandelbrot_image.get_image().save("mandelbrot.png")


def main():
    start = time.time()
    mandelbrot(width=4000, height=4000)
    end = time.time()
    print(f"TIME 1: {end - start}")


if __name__ == "__main__":
    main()
