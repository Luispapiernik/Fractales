#!/usr/bin/python

from argparse import ArgumentParser
from PIL import Image


def mandelbrot(args):
    lim = args.max_iteration
    r = (args.percent_red or args.percents[0]) / 100.0
    g = (args.percent_green or args.percents[1]) / 100.0
    b = (args.percent_blue or args.percents[2]) / 100.0
    pairs = [r, g, b]
    pairs.sort(reverse=True)
    lim2 = max(r, g, b) * lim
    x, y = args.width or args.size[0], args.height or args.size[1]
    scale = args.scale
    img = Image.new("RGB", (x, y))
    for x0 in range(0, x):
        for y0 in range(0, y):
            z0 = complex((x0 - (x / 2.0)) / scale, (y0 - (y / 2.0)) / scale)
            z = complex(0, 0)
            level = 0
            while (abs(z) < 2) and (level <= lim2):
                z = (z ** 2) + z0
                level += 1
            for i in pairs:
                if level < (i * lim):
                    img.putpixel((x0, y0),
                                 (int(255.0 * level / (r * lim)) * (i == r),
                                  int(255.0 * level / (g * lim)) * (i == g),
                                  int(255.0 * level / (b * lim)) * (i == b)))
    img.save(args.name_image)
    img.show()


def main():
    parser = ArgumentParser(description='Generates the fractal of mandelbrot')

    parser.add_argument('-n', '--name-image', default='mandelbrot.png',
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
    parser.add_argument('--scale', default=90, type=float,
                        help='''number of pixels that represent the number
                                one in the real number line
                                Default value is 90''')
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
    parser.add_argument('--version', action='version', version='%(prog)s 2.0',
                        help='shows version information and ends')

    args = parser.parse_args()

    mandelbrot(args)


if __name__ == '__main__':
    main()
