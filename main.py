from argparse import (
    ArgumentDefaultsHelpFormatter,
    ArgumentParser,
    RawDescriptionHelpFormatter,
)


class CombinedFormatters(RawDescriptionHelpFormatter, ArgumentDefaultsHelpFormatter):
    pass


def main():
    parser = ArgumentParser(
        description="Generates multiples fractals",
        epilog="This should be edited",
        formatter_class=CombinedFormatters,
        allow_abbrev=True,
        conflict_handler="resolve",
    )
    general_args = parser.add_argument_group("General args")
    mandelbrot_args = parser.add_argument_group("Mandelbrot args")

    # generals args
    general_args.add_argument(
        "-o",
        "--output-file",
        default="mandelbrot.png",
        metavar="FILENAME",
        help="name of output image.",
    )
    general_args.add_argument(
        "--size",
        default=(360, 360),
        type=int,
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        help="size of output image in pixels.",
    )
    general_args.add_argument(
        "-w", "--width", default=0, type=int, help="width of the output image"
    )
    general_args.add_argument(
        "-h", "--height", default=0, type=int, help="height of the output image"
    )
    general_args.add_argument(
        "-bc",
        "--background-color",
        metavar=("R", "G", "B"),
        nargs=3,
        type=int,
        choices=range(0, 256),
        default=(0, 0, 0),
    )
    general_args.add_argument("--show", action="store_true", help="show the image")
    general_args.add_argument(
        "--version", action="version", version="Fractal Generator 0.1"
    )

    # Pallete args
    # Barnsley args

    # mandelbrot args
    mandelbrot_args.add_argument(
        "-x",
        "--xinterval",
        default=(-2, 2),
        nargs=2,
        type=float,
        metavar=("xi", "xf"),
        help="interval of visualisation in the X axis",
    )
    mandelbrot_args.add_argument(
        "-y",
        "--yinterval",
        default=(-2, 2),
        nargs=2,
        type=float,
        metavar=("yi", "yf"),
        help="interval of visualisation in the Y axis",
    )
    mandelbrot_args.add_argument(
        "-m",
        "--max-iteration",
        default=20,
        type=int,
        help="maximum iteration.",
    )

    # Sierpinski

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
