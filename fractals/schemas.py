from numbers import Real
from typing import List, Tuple, Union

RGB = Union[Tuple[int, int, int], List[float]]
RGBA = Tuple[int, int, int, int]
Color = Union[int, RGB, RGBA, str]
Coordinate = Tuple[Real, Real]
