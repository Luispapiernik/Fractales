from typing import List

from PIL import ImagePalette

from fractals.schemas import RGB


def get_channels_number(*, mode: str) -> int:
    """
    This function return the numbers of channels given a color mode.

    Parameters
    ----------
    mode: str
        color mode.

    Returns
    -------
    out: int
        number of channels associated with the color mode.
    """
    if mode == "YCbCr":
        return 3

    return len(mode)


def float_colors_to_int_colors(colors: List[RGB]) -> List[RGB]:
    """
    This function maps color components from the interval [0, 1] to the interval
    [0, 255].

    Parameters
    ----------
    colors: List[RGB]
        list of colors with each color components in the interval [0, 1].

    Returns
    -------
    out: List[RGB]
        list of colors with each color components in the interval [0, 255].
    """
    return [tuple(int(255 * channel) for channel in color) for color in colors]


def colors_list_to_palette(colors: List[RGB]) -> ImagePalette.ImagePalette:
    """
    This function create a palette from the given color list.

    Parameters
    ----------
    colors: List[RGB]
        list of colors.

    Returns
    -------
    out: ImagePalette.ImagePalette
        palette of colors.
    """
    palette = ImagePalette.ImagePalette(mode="P")
    for color in float_colors_to_int_colors(colors=colors):
        palette.getcolor(tuple(color))

    return palette
