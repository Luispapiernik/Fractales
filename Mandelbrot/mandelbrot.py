from argparse import ArgumentParser
from cartesian import CartesianImage


def mandelbrot(args):
    # configuracion de la imagen
    width = args.width or args.size[0]
    height = args.height or args.size[1]

    img = CartesianImage(args.xinterval, args.yinterval, width, height,
                         args.background_color)

    # porcentaje de colores
    r = (args.percent_red or args.percents[0]) / 100.0
    g = (args.percent_green or args.percents[1]) / 100.0
    b = (args.percent_blue or args.percents[2]) / 100.0

    pairs = [r, g, b]
    pairs.sort(reverse=True)
    limit = args.max_iteration
    strictLimit = limit * max(r, g, b)

    for i in range(height):
        for j in range(width):
            x, y = img.getCoordinate(j, i)

            c = complex(x, y)
            z = complex(0, 0)
            iteration = 0
            while (abs(z) < 2) and (iteration < strictLimit):
                z = (z ** 2) + c

                iteration += 1

            for color in pairs:
                if iteration < (color * limit):
                    img.putpixel((j, i), (
                        int(255.0 * iteration / (r * limit)) * (color == r),
                        int(255.0 * iteration / (g * limit)) * (color == g),
                        int(255.0 * iteration / (b * limit)) * (color == b)),
                        False)

    img.save(args.name_image)
    img.show()


def main():
    parser = ArgumentParser(description='Generates the fractal of mandelbrot')

    parser.add_argument('-n', '--name-image', default='mandelbrot.png',
                        metavar='FILENAME',
                        help='''name of output image.
                                Default value is mandelbrot.png''')
    parser.add_argument('--size', default=(360, 360), type=int, nargs=2,
                        metavar=('WIDTH', 'HEIGHT'),
                        help='''size of output image in pixels.
                                Default value is (360, 360)''')
    parser.add_argument('-w', '--width', default=0, type=int,
                        help='width of the output image')
    parser.add_argument('--height', default=0, type=int,
                        help='height of the output image')
    parser.add_argument('-x', '--xinterval', default=(-2, 2), nargs=2,
                        type=float, metavar=('xi', 'xf'),
                        help='''interval of visualisation in the X axis''')
    parser.add_argument('-y', '--yinterval', default=(-2, 2), nargs=2,
                        type=float, metavar=('yi', 'yf'),
                        help='''interval of visualisation in the Y axis''')
    parser.add_argument('-bc', '--background-color', metavar=('R', 'G', 'B'),
                        nargs=3, type=int, choices=range(0, 256),
                        default=(0, 0, 0))
    parser.add_argument('-p', '--percents', default=(12, 15, 20), type=float,
                        choices=(range(1, 101)), nargs=3,
                        metavar=('RED', 'GREEN', 'BLUE'),
                        help='''percents of each colors.
                                Default value is (12.0, 15.0, 20.0)''')
    parser.add_argument('-pr', '--percent-red', default=0, type=float,
                        metavar='RED', choices=(range(1, 101)),
                        help='percent of color red')
    parser.add_argument('-pg', '--percent-green', default=0, type=float,
                        metavar='GREEN', choices=(range(1, 101)),
                        help='percent of color green')
    parser.add_argument('-pb', '--percent-blue', default=0, type=float,
                        metavar='BLUE', choices=(range(1, 101)),
                        help='percent of color blue')
    parser.add_argument('-m', '--max-iteration', default=100, type=int,
                        help='maximum iteration. Default value is 100')

    args = parser.parse_args()

    mandelbrot(args)


if __name__ == '__main__':
    main()
