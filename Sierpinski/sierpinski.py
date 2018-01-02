from argparse import ArgumentParser, RawDescriptionHelpFormatter
from PIL import Image

# colores
COLORS = {'WHITE': (255, 255, 255), 'BLACK': (0, 0, 0), 'CYAN': (0, 255, 255),
          'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255), 'YELLOW': (255, 255, 0),
          'ORANGE': (255, 165, 0), 'MAGENTA': (255, 0, 255),
          'SILVER': (192, 192, 192), 'PURPLE': (128, 0, 128),
          'TEAL': (0, 128, 128), 'GRAY': (128, 128, 128), 'RED': (255, 0, 0),
          'BROWN': (165, 42, 42), 'GOLDEN': (255, 215, 0)}


def square(color, point, length):
    global img
    for x in range(length):
        for y in range(length):
            img.putpixel((point[0] + x, point[1] + y), color)


def sierpinski(tiles, deep, point, length):
    if deep:
        x, y = point
        nlength = length // 3
        square(tiles, (x + nlength, y + nlength), nlength)
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                sierpinski(tiles, deep - 1, (x + i * nlength, y + j * nlength),
                           nlength)


def main():
    global img

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

    parser = ArgumentParser(description='Generates the fractal of sierpinski',
                            formatter_class=RawDescriptionHelpFormatter,
                            epilog=epilog)

    parser.add_argument('-l', '--length', default=360, type=int,
                        help='''the output image has a rectangular shape,
                                this argument is the length of one of his
                                edges. Default value is 360''')
    parser.add_argument('-n', '--name-image', default='sierpinski.png',
                        type=str, help='''name of output image. Default value
                                          is sierpinski.png''')
    parser.add_argument('-b', '--background', default='BLACK', type=str,
                        choices=COLORS.keys(), metavar='COLOR',
                        help='color of background. Default value is BLACk')
    parser.add_argument('-t', '--tiles', default='WHITE', type=str,
                        choices=COLORS.keys(), metavar='COLOR',
                        help='color of the tiles. Default value is WHITE')
    parser.add_argument('-rl', '--recursion-level', default=3, type=int,
                        help='level of recursion. Default value is 3')

    args = parser.parse_args()

    length = args.length
    img = Image.new("RGB", (length, length))

    square(COLORS[args.background], (0, 0), length)
    sierpinski(COLORS[args.tiles], args.recursion_level, (0, 0), length)

    img.save(args.name_image)


if __name__ == '__main__':
    main()
