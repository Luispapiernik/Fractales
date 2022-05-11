from argparse import (ArgumentDefaultsHelpFormatter, ArgumentParser,
                      RawDescriptionHelpFormatter)

from matplotlib import cm, colors

from fractals.barnsley import barnsley
from fractals.mandelbrot import mandelbrot
from fractals.sierpinski import sierpinski
from fractals.utils import colors_list_to_palette, get_channels_number


class CombinedFormatters(RawDescriptionHelpFormatter, ArgumentDefaultsHelpFormatter):
    pass


def parse_color(color):
    if color.replace(" ", "").isdigit() and len(color) > 1:
        return tuple(map(int, color.strip().split(" ")))

    return color


def parse_palette_color(color):
    color = parse_color(color)

    if isinstance(color, str):
        color = colors.to_rgba(color)
        color = tuple(map(int, color))

    return color


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
        data = args.palette_nodes
        if args.nodes_weights:
            assert len(data) == len(args.nodes_weights)
            data = list(zip(args.nodes_weights, data))

        cmap = colors.LinearSegmentedColormap.from_list("user_defined", data, N=256)
        colors_list = cmap(range(256))
        return colors_list_to_palette(colors_list)

    return None


def process_args(args):
    args.palette = get_palette(args)

    if get_channels_number(mode=args.image_mode) == 1:
        if (
            isinstance(args.background_color, str)
            and args.background_color.strip().isdigit()
        ):
            args.background_color = int(args.background_color.strip())
        if isinstance(args.color, str) and args.color.strip().isdigit():
            args.color = int(args.color.strip())
    else:
        if (
            isinstance(args.background_color, str)
            and args.background_color.strip().isalpha()
        ):
            args.background_color = colors.to_rgba(args.background_color)
            args.background_color = tuple(
                map(lambda x: int(255 * x), args.background_color)
            )
        if isinstance(args.color, str) and args.color.strip().isalpha():
            args.color = colors.to_rgba(args.color)
            args.color = tuple(map(lambda x: int(255 * x), args.color))

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

        image.save(args.output_file)
        if args.show:
            image.show()

    if args.barnsley:
        image = barnsley(
            width=args.width or args.size[0],
            height=args.height or args.size[1],
            x_interval=args.x_interval,
            y_interval=args.y_interval,
            background_color=args.background_color,
            color=args.color,
            mode=args.image_mode,
            max_iteration=args.max_iteration,
        )

        image.save(args.output_file)
        if args.show:
            image.show()

    if args.sierpinski:
        w = args.width or args.size[0]
        h = args.height or args.size[1]
        length = max(h, w)
        image = sierpinski(
            length=length,
            background_color=args.background_color,
            color=args.color,
            mode=args.image_mode,
            max_iteration=args.max_iteration,
        )

        image.save(args.output_file)
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
    barnsley_args = parser.add_argument_group("Barnsley args")
    mandelbrot_args = parser.add_argument_group("Mandelbrot args")
    sierpinski_args = parser.add_argument_group("Sierpinkski args")

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
        choices=["1", "L", "P", "RGB", "RGBA", "CMYK", "YCbCr", "LAB", "HSV"],
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
        type=parse_color,
        help="background color of the output image.",
        default=0,
    )
    general_args.add_argument(
        "-c",
        "--color",
        metavar="COLOR",
        type=parse_color,
        help="color to paint the fractal in a solid way.",
        default=255,
    )
    general_args.add_argument(
        "--show", action="store_true", help="show the generated fractal."
    )
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
    geometrical_args.add_argument(
        "-m",
        "--max-iteration",
        default=20,
        type=int,
        help="maximum iteration or recursion level acording to the selected fractal.",
    )

    # Palette args
    palette_args.add_argument(
        "-pn", "--palette-name",
        help="name of the palette to select, all matplotlib palettes are supported."
    )
    palette_args.add_argument(
        "-pnd",
        "--palette-nodes",
        metavar="COLOR",
        type=parse_palette_color,
        nargs="+",
        help="nodes to create a linear segmented palette.",
    )
    palette_args.add_argument(
        "-nw",
        "--nodes-weights",
        type=float,
        nargs="+",
        help="weight of the nodes. it must be acomulative up to 1",
    )
    palette_args.add_argument(
        "-i",
        "--invert-palette",
        action="store_true",
        help="invert the order of the palette colors.",
    )

    # Barnsley args
    # TODO: add parameters to control the afin transformations
    barnsley_args.add_argument(
        "--barnsley",
        action="store_true",
        help="generated the barnsley fractal.",
    )

    # mandelbrot args
    mandelbrot_args.add_argument(
        "--mandelbrot",
        action="store_true",
        help="generated the mandelbrot fractal.",
    )
    mandelbrot_args.add_argument(
        "-er",
        "--escape-radius",
        default=1000,
        type=float,
        help="escape radius of the mandelbrot set.",
    )
    mandelbrot_args.add_argument(
        "-s",
        "--smooth-bands",
        action="store_true",
        help="smooth the transition between colors in the fractal.",
    )
    mandelbrot_args.add_argument(
        "-p",
        "--process-number",
        default=0,
        type=int,
        help="number of process for the paralelization, if zero is passed the maximum number allowed will be used.",
    )

    # Sierpinski
    sierpinski_args.add_argument(
        "--sierpinski",
        action="store_true",
        help="generated the sierpinski fractal.",
    )

    args = parser.parse_args()
    args = process_args(args)
    execute(args)


if __name__ == "__main__":
    main()
