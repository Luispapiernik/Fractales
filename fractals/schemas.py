from numbers import Real
from typing import Tuple, Union

RGB = Tuple[int, int, int]
RGBA = Tuple[int, int, int, int]
Color = Union[int, RGB, RGBA, str]
Coordinate = Union[Tuple[Real, Real], Tuple[int, int]]
Component = Union[Real, int]
