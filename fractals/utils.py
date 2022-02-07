from typing import List

from PIL import ImagePalette

from fractals.schemas import RGB


def get_channels(*, mode: str) -> int:
    if mode == "YCbCr":
        return 3

    return len(mode)


def float_colors_to_int_colors(colors: List[RGB]) -> List[RGB]:
    return [tuple(int(255 * channel) for channel in color) for color in colors]


def colors_list_to_palette(colors_list):
    palette = ImagePalette.ImagePalette(mode="P")
    for color in float_colors_to_int_colors(colors=colors_list):
        palette.getcolor(tuple(color))

    return palette
