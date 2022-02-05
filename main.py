from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Generates multiples fractals")

    # generals args
    parser.add_argument(
        "-o",
        "--output-file",
        default="mandelbrot.png",
        metavar="FILENAME",
        help="""name of output image.
                                Default value is mandelbrot.png""",
    )
    parser.add_argument(
        "--size",
        default=(360, 360),
        type=int,
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        help="""size of output image in pixels.
                                Default value is (360, 360)""",
    )
    parser.add_argument(
        "-w", "--width", default=0, type=int, help="width of the output image"
    )
    parser.add_argument(
        "-ht", "--height", default=0, type=int, help="height of the output image"
    )
    parser.add_argument(
        "-bc",
        "--background-color",
        metavar=("R", "G", "B"),
        nargs=3,
        type=int,
        choices=range(0, 256),
        default=(0, 0, 0),
    )
    parser.add_argument("--show", action="store_true", help="show the image")

    # Pallete args
    # Barnsley args

    # mandelbrot args
    parser.add_argument(
        "-x",
        "--xinterval",
        default=(-2, 2),
        nargs=2,
        type=float,
        metavar=("xi", "xf"),
        help="""interval of visualisation in the X axis""",
    )
    parser.add_argument(
        "-y",
        "--yinterval",
        default=(-2, 2),
        nargs=2,
        type=float,
        metavar=("yi", "yf"),
        help="""interval of visualisation in the Y axis""",
    )
    parser.add_argument(
        "-m",
        "--max-iteration",
        default=20,
        type=int,
        help="maximum iteration. Default value is 100",
    )

    # Sierpinski

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
