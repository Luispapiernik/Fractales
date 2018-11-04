from argparse import ArgumentParser, RawDescriptionHelpFormatter
from cartesian import CartesianImage
from random import choice


COLORS = {'WHITE': (255, 255, 255), 'BLACK': (0, 0, 0), 'CYAN': (0, 255, 255),
          'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255), 'YELLOW': (255, 255, 0),
          'ORANGE': (255, 165, 0), 'MAGENTA': (255, 0, 255),
          'SILVER': (192, 192, 192), 'PURPLE': (128, 0, 128),
          'TEAL': (0, 128, 128), 'GRAY': (128, 128, 128), 'RED': (255, 0, 0),
          'BROWN': (165, 42, 42), 'GOLDEN': (255, 215, 0)}


def barnsley(args):
    # configuracion de la imagen
    width = args.width or args.size[0]
    height = args.height or args.size[1]

    img = CartesianImage(args.xinterval, args.yinterval, width, height,
                         args.background_color)

    function = [lambda x, y: (0, 0.16 * y),
                lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6),
                lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6),
                lambda x, y: (-0.15 * x + 0.28 * y,
                              0.26 * x + 0.24 * y + 0.44)]

    x0, y0 = 0, 0
    for k in range(args.iterations):
        i, j = img.getPosition(x0, y0)
        if (0 <= i < width) and (0 <= j < height):
            img.putpixel((i, j), COLORS[args.color], False)

        x0, y0 = function[choice([0, 1, 2, 3])](x0, y0)

    img.save(args.name_image)
    img.show()


def main():
    epilog = '''The colors available are:
    - WHITE
    - BLACK
    - CYAN
    - GREEN
    - BLUE
    - YELLOW
    - ORANGE
    - MAGENTA
    - SILVER
    - PURPLE
    - TEAL
    - GRAY
    - RED
    - BROWN
    - GOLDEN'''

    parser = ArgumentParser(description='generates the barnsley fern',
                            formatter_class=RawDescriptionHelpFormatter,
                            epilog=epilog)

    parser.add_argument('-n', '--name-image', default='barnsley.png', type=str,
                        help='name of the output image')
    parser.add_argument('-s', '--size', default=(360, 360), nargs=2, type=int,
                        metavar=('WIDTH', 'HEIGHT'),
                        help='size of the output image. Default is (600, 600')
    parser.add_argument('-w', '--width', default=0, type=int,
                        help='width of the output image')
    parser.add_argument('--height', default=0, type=int,
                        help='height of the output image')
    parser.add_argument('-x', '--xinterval', default=(-5, 5), nargs=2,
                        type=float, metavar=('xi', 'xf'),
                        help='''interval of visualisation in the X axis''')
    parser.add_argument('-y', '--yinterval', default=(0, 10), nargs=2,
                        type=float, metavar=('yi', 'yf'),
                        help='''interval of visualisation in the Y axis''')
    parser.add_argument('-c', '--color', default='WHITE',
                        type=lambda x: x.upper(),
                        choices=COLORS.keys(), metavar='COLOR',
                        help='color of the fern')
    parser.add_argument('-bc', '--background-color', default='BLACK',
                        type=lambda x: x.upper(),
                        choices=COLORS.keys(), metavar='COLOR',
                        help='background color of image')

    parser.add_argument('-i', '--iterations', default=200000, type=int,
                        help='''limit of iterations that the program do.
                                if you want an image with good resolution,
                                probably you want that this number be big.
                                Default is 20000''')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0',
                        help='shows version information and ends')

    args = parser.parse_args()

    barnsley(args)


if __name__ == '__main__':
    main()
