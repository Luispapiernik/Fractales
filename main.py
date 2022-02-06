from argparse import (
    ArgumentDefaultsHelpFormatter,
    ArgumentParser,
    RawDescriptionHelpFormatter,
)
from typing import List, Tuple, Union

from matplotlib import cm, colors
from PIL import ImagePalette

from fractals.mandelbrot import mandelbrot

RGB = Union[Tuple[int, int, int], List[float]]
RGBA = Tuple[int, int, int, int]
Color = Union[int, RGB, RGBA, str]


class CombinedFormatters(RawDescriptionHelpFormatter, ArgumentDefaultsHelpFormatter):
    pass


def parse_background_color(color: str) -> Color:
    # TODO: This should be revised
    if color.isdigit():
        return int(color)
    if color.replace(" ", "").isdigit():
        return tuple(map(int, color.strip().split(" ")))
    return color


def parse_palette_color(color):
    if color.replace(" ", "").isdigit() and len(color) > 1:
        return tuple(map(int, color.strip().split(" ")))

    color = colors.to_rgba(color)
    return tuple(int(255 * channel) for channel in color)


def float_colors_to_int_colors(colors: List[RGB]) -> List[RGB]:
    return [tuple(int(255 * channel) for channel in color) for color in colors]


def colors_list_to_palette(colors_list):
    palette = ImagePalette.ImagePalette(mode="P")
    for color in float_colors_to_int_colors(colors=colors_list):
        palette.getcolor(tuple(color))

    return palette


def get_palette(args):
    if args.palette_name:
        cmap = cm.get_cmap(args.palette_name)
        if hasattr(cmap, "colors"):
            colors_list = cmap.colors
        else:
            colors_list = cmap(range(256))

        if len(colors_list) > 256:
            # TODO: this should be revised
            # if args.invert_palette:
            # cmap = cmap.reversed()

            # TODO: This choice must be improved
            colors_list = colors_list[0:255]
        return colors_list_to_palette(colors_list)

    if args.palette_nodes:
        # TODO: this must be changed
        cmap = colors.LinearSegmentedColormap.from_list(
            "user_defined", args.palette_nodes
        )

        colors_list = cmap(range(256))
        return colors_list_to_palette(colors_list)

    return None


def process_args(args):
    args.palette = get_palette(args)

    return args


def execute(args):
    print(args)
    if args.mandelbrot:
        image = mandelbrot(
            width=args.width or args.size[0],
            height=args.height or args.size[1],
            x_interval=args.x_interval,
            y_interval=args.y_interval,
            color=args.background_color,
            mode=args.image_mode,
            palette=args.palette,
            processes=args.process_number,
            max_iteration=args.max_iteration,
            escape_radius=args.escape_radius,
            smooth=args.smooth_bands,
            invert=args.invert_palette,
            verbose=args.verbose,
        )

        if args.show:
            image.show()


def main():
    parser = ArgumentParser(
        description="Generates multiples fractals",
        epilog="This should be edited",
        formatter_class=CombinedFormatters,
        allow_abbrev=True,
        conflict_handler="resolve",
    )
    general_args = parser.add_argument_group("General args")
    geometrical_args = parser.add_argument_group("Geometrical args")
    palette_args = parser.add_argument_group("Palette args")
    mandelbrot_args = parser.add_argument_group("Mandelbrot args")

    # generals args
    general_args.add_argument(
        "-o",
        "--output-file",
        default="fractal.png",
        metavar="FILENAME",
        help="name of output image.",
    )
    general_args.add_argument(
        "-im",
        "--image-mode",
        default="L",
        metavar="IMAGE MODE",
        choices=["L", "P"],
        help="mode of the output image. This specify what color schema must be applied.",
    )
    general_args.add_argument(
        "--size",
        default=(512, 512),
        type=int,
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        help="size of output image in pixels.",
    )
    general_args.add_argument(
        "-w", "--width", type=int, help="width of the output image in pixels."
    )
    general_args.add_argument(
        "-h", "--height", type=int, help="height of the output image in pixels."
    )
    general_args.add_argument(
        "-bc",
        "--background-color",
        metavar="COLOR",
        type=parse_background_color,
        help="background color of the output image.",
        default=0,
    )
    general_args.add_argument("--show", action="store_true", help="show the image")
    general_args.add_argument("-v", "--verbose", action="count", default=0)
    general_args.add_argument(
        "--version", action="version", version="Fractal Generator 0.1"
    )

    # geometrical args
    geometrical_args.add_argument(
        "-x",
        "--x-interval",
        default=(-2, 2),
        nargs=2,
        type=float,
        metavar=("xi", "xf"),
        help="interval of visualisation in the X axis",
    )
    geometrical_args.add_argument(
        "-y",
        "--y-interval",
        default=(-2, 2),
        nargs=2,
        type=float,
        metavar=("yi", "yf"),
        help="interval of visualisation in the Y axis",
    )

    # Palette args
    palette_args.add_argument("-pn", "--palette-name", help="edit.")
    palette_args.add_argument(
        "-pnd",
        "--palette-nodes",
        metavar="COLOR",
        type=parse_palette_color,
        nargs="+",
        help="edit.",
    )
    palette_args.add_argument(
        "-i",
        "--invert-palette",
        action="store_true",
        help="edit.",
    )

    # Barnsley args

    # mandelbrot args
    mandelbrot_args.add_argument(
        "--mandelbrot",
        action="store_true",
        help="edit.",
    )
    mandelbrot_args.add_argument(
        "-m",
        "--max-iteration",
        default=20,
        type=int,
        help="maximum iteration.",
    )
    mandelbrot_args.add_argument(
        "-er",
        "--escape-radius",
        default=1000,
        type=float,
        help="edit.",
    )
    mandelbrot_args.add_argument(
        "-s",
        "--smooth-bands",
        action="store_true",
        help="edit.",
    )
    mandelbrot_args.add_argument(
        "-p",
        "--process-number",
        default=0,
        type=int,
        help="number of process for the paralelization, if zero is passed the maximum number allowed will be used.",
    )

    # Sierpinski

    args = parser.parse_args()
    args = process_args(args)
    execute(args)


if __name__ == "__main__":
    main()
