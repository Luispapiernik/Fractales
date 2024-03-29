from numbers import Real
from typing import Any

import numpy as np
from PIL import Image

from fractals.schemas import Color, Component, Coordinate
from fractals.utils import get_channels_number


class Cartesian:
    """
    This class handles the conversion of coordinates between a region on the
    cartesian plane and a matrix (rectangular region with integer coordinates).

    Parameters
    ----------
    x_interval: Coordinate
        limits in the x coordinate of the region on the cartesian plane.
    y_interval: Coordinate
        limits in the y coordinate of the region on the cartesian plane.
    width: int
        width of the matrix.
    height: int
        height of the matrix.
    """

    def __init__(
        self, *, x_interval: Coordinate, y_interval: Coordinate, width: int, height: int
    ):
        self.x_interval = x_interval
        self.y_interval = y_interval
        self.height = height
        self.width = width

    def bijection(self, *, w: Component, h: Component) -> Coordinate:
        """
        This method converts a coordinate in the matrix into a coordinate on
        the Cartesian plane.

        Parameters
        ----------
        w, h: int, int
            coordinate of the point in the matrix.

        Returns
        -------
        out: Coordinate
            coordinate of the associated point in the cartesian plane.

        Note
        ----
            This method does not represent a strict bijection.
        """
        x = (w + self.width / 2) * (
            self.x_interval[1] - self.x_interval[0]
        ) / self.width + self.x_interval[0]
        y = (h + self.height / 2) * (
            self.y_interval[1] - self.y_interval[0]
        ) / self.height + self.y_interval[0]
        return x, y

    def inverse_bijection(self, *, x: Component, y: Component) -> Coordinate:
        """
        This method converts a coordinate in the Cartesian plane into a
        coordinate on the matrix.

        Parameters
        ----------
        x, y: Real, Real
            coordinate of the point in the cartesian plane.

        Returns
        -------
        out: Coordinate
            coordinate of the associated point in the matrix.

        Note
        ----
            This method does not represent a strict bijection.
        """
        w = (x - self.x_interval[0]) * self.width / (
            self.x_interval[1] - self.x_interval[0]
        ) - self.width / 2
        h = (y - self.y_interval[0]) * self.height / (
            self.y_interval[1] - self.y_interval[0]
        ) - self.height / 2
        return w, h

    def get_coordinate(self, *, column: Component, row: Component) -> Coordinate:
        """
        This method returns the coordinate (x, y) in the plane, given a
        position in the matrix.

        Parameters
        ----------
        column, row: int, int
            coordinate of the point in the matrix.

        Returns
        -------
        out: Coordinate
            coordinate of the associated point in the cartesian plane.
        """
        w = column - self.width / 2
        h = -row + self.height / 2
        return self.bijection(w=w, h=h)

    def get_position(self, *, x: Component, y: Component) -> Coordinate:
        """
        This method returns a position in the matrix given some coordinate
        (x, y) in the plane.

        Parameters
        ----------
        x, y: Real, Real
            coordinate of the point in the cartesian plane.

        Returns
        -------
        out: Coordinate
            coordinate of the associated point in the matrix.
        """
        x, y = self.inverse_bijection(x=x, y=y)
        column = int(x + self.width / 2)
        row = int(self.height / 2 - y)
        return column, row


class CartesianImage(Cartesian):
    """
    This class represents an image in the Cartesian plane

    Parameters
    ----------
    width: int
        width of the image.
    height: int
        height of the image.
    x_interval: Coordinate
        limits in the x coordinate of the region on the cartesian plane.
    y_interval: Coordinate
        limits in the y coordinate of the region on the cartesian plane.
    color: int or Tuple[int, int, int] or Tuple[int, int, int, int]
        initial color of the image.
    mode: str
        color mode of the image.
    """

    def __init__(
        self,
        *,
        width: int,
        height: int,
        x_interval: Coordinate = None,
        y_interval: Coordinate = None,
        color=0,
        mode="RGB",
    ):
        if x_interval is not None and y_interval is not None:
            super().__init__(
                x_interval=x_interval, y_interval=y_interval, width=width, height=height
            )

        self._image = Image.new(mode, (width, height), color)

    def __getattr__(self, key: Any) -> Any:
        if key == "_image":
            raise AttributeError()
        if key == "putpixel":
            return getattr(self, key)

        return getattr(self._image, key)

    def putpixel(self, *, position: Coordinate, color: Color, to_int=True) -> None:
        """
        This method set the color of a specific pixel.

        Parameters
        ----------
        position: Coordinate
            position of the especifi pixel.
        color: Color
            color to use.
        to_int: bool
            specifies when to change from Cartesian to matrix coordinates.
        """
        if to_int:
            position = self.get_position(x=position[0], y=position[1])
        self._image.putpixel(position, color)


class CartesianArray(Cartesian):
    """
    This class represents an image in the Cartesian plane manage throught arrays.

    Parameters
    ----------
    width: int
        width of the image.
    height: int
        height of the image.
    x_interval: Coordinate
        limits in the x coordinate of the region on the cartesian plane.
    y_interval: Coordinate
        limits in the y coordinate of the region on the cartesian plane.
    color: int or Tuple[int, int, int] or Tuple[int, int, int, int]
        initial color of the image.
    mode: str
        color mode of the image.
    """

    def __init__(
        self,
        *,
        width: int,
        height: int,
        x_interval: Coordinate = None,
        y_interval: Coordinate = None,
        color=0,
        mode="RGB",
    ):
        if x_interval is not None and y_interval is not None:
            super().__init__(
                x_interval=x_interval, y_interval=y_interval, width=width, height=height
            )

        self.mode = mode
        self.channels = get_channels_number(mode=mode)
        if self.channels > 1:
            self.array = np.ones((height, width, self.channels))
            # self.array = np.insert(self.array[:, :, None], [1], [1, 1], axis=2)
        else:
            self.array = np.ones((height, width))
        self.array[:, :] = color

    def write_sub_array(self, x_offset: int, y_offset: int, array: np.ndarray) -> None:
        """
        This method write a subarray on the image array.

        Parameters
        ----------
        x_offset, y_offset: int, int
            point where the subarray is writed.
        """
        self.array[
            y_offset: y_offset + array.shape[0], x_offset: x_offset + array.shape[1]
        ] = array

    def putpixel(self, *, position: Coordinate, color, to_int=True):
        """
        This method set the color of a specific pixel.

        Parameters
        ----------
        position: Coordinate
            position of the especifi pixel.
        color: Color
            color to use.
        to_int: bool
            specifies when to change from Cartesian to matrix coordinates.
        """
        if to_int:
            position = self.get_position(x=position[0], y=position[1])
        self.array[position[1], position[0]] = color

    def get_image(self) -> Image.Image:
        """
        This method returns the image.

        Returns
        -------
        out: Image.Image
            image.
        """
        return Image.fromarray(np.uint8(self.array), self.mode)


def test_sin_1():
    image = CartesianImage(
        width=1000, height=1000, x_interval=(-6 * np.pi, 6 * np.pi),
        y_interval=(-2, 2)
    )

    for x in np.arange(-6 * np.pi, 6 * np.pi, 0.0001):
        image.putpixel(position=(x, np.sin(x)), color=(255, 0, 0))

    image.save("seno1.png")


def test_sin_2():
    image = CartesianArray(
        width=1000, height=1000, x_interval=(-6 * np.pi, 6 * np.pi),
        y_interval=(-2, 2)
    )

    for x in np.arange(-6 * np.pi, 6 * np.pi, 0.0001):
        image.putpixel(position=(x, np.sin(x)), color=(255, 0, 0))

    image.get_image().save("seno2.png")


def main():
    import time

    start = time.time()
    test_sin_1()
    end = time.time()
    print(f"TIME 1: {end - start}")

    start = time.time()
    test_sin_2()
    end = time.time()
    print(f"TIME 2: {end - start}")


if __name__ == "__main__":
    main()
