from argparse import ArgumentParser, RawDescriptionHelpFormatter
from PIL import Image, ImageDraw

# colors
COLORS = {'WHITE': (255, 255, 255), 'BLACK': (0, 0, 0), 'CYAN': (0, 255, 255),
          'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255), 'YELLOW': (255, 255, 0),
          'ORANGE': (255, 165, 0), 'MAGENTA': (255, 0, 255),
          'SILVER': (192, 192, 192), 'PURPLE': (128, 0, 128),
          'TEAL': (0, 128, 128), 'GRAY': (128, 128, 128), 'RED': (255, 0, 0),
          'BROWN': (165, 42, 42), 'GOLDEN': (255, 215, 0)}


def sierpinski(deep, point, length):
    global painter, tiles

    if deep:
        x, y = point
        nlength = length // 3
        x0, y0 = x + nlength, y + nlength
        painter.rectangle([x0, y0, x0 + nlength, y0 + nlength], tiles, tiles)
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                sierpinski(deep - 1, (x + i * nlength, y + j * nlength),
                           nlength)


def main():
    global painter, tiles

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

    parser.add_argument('-n', '--name-image', default='sierpinski.png',
                        type=str, help='''name of output image. Default value
                                          is sierpinski.png''')
    parser.add_argument('-l', '--length', default=360, type=int,
                        help='''the output image has a square shape,
                                this argument is the length of one of his
                                edges. Default value is 360''')
    parser.add_argument('-b', '--background', default='BLACK',
                        type=lambda x: x.upper(),
                        choices=COLORS.keys(), metavar='COLOR',
                        help='color of background. Default value is BLACk')
    parser.add_argument('-t', '--tiles', default='WHITE',
                        type=lambda x: x.upper(),
                        choices=COLORS.keys(), metavar='COLOR',
                        help='color of the tiles. Default value is WHITE')
    parser.add_argument('-rl', '--recursion-level', default=3, type=int,
                        help='level of recursion. Default value is 3')
    parser.add_argument('--show', action='store_true',
                        help='show the image')

    args = parser.parse_args()

    length = args.length
    tiles = COLORS[args.tiles]
    img = Image.new("RGB", (length, length), COLORS[args.background])
    painter = ImageDraw.Draw(img)

    sierpinski(args.recursion_level, (0, 0), length)

    img.save(args.name_image)

    if args.show:
        img.show()


if __name__ == '__main__':
    main()
