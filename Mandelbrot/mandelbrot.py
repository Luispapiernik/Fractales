from Args import Args
from PIL import Image


def mandelbrot(args):
    lim = args['max-iteration']
    r = args['percent-red'] / 100
    g = args['percent-green'] / 100
    b = args['percent-blue'] / 100
    pairs = [r, g, b]
    pairs.sort(reverse=True)
    lim2 = max(r, g, b) * lim
    x, y = args['width'], args['height']
    scale = args['scale']
    img = Image.new("RGB", (x, y))
    for x0 in range(0, x):
        for y0 in range(0, y):
            z0 = complex((x0 - (x / 2)) / scale, (y0 - (y / 2)) / scale)
            z = complex(0, 0)
            level = 0
            while (abs(z) < 2) and (level <= lim2):
                z = (z ** 2) + z0
                level += 1
            for i in pairs:
                if level < (i * lim):
                    img.putpixel((x0, y0),
                                 (int(255 * level / (r * lim)) * (i == r),
                                  int(255 * level / (g * lim)) * (i == g),
                                  int(255 * level / (b * lim)) * (i == b)))
    img.save(args['name'])
    img.show()


def main():
    args = Args({'width': 360, 'height': 360, 'scale': 90.0,
                 'name': 'mandelbrot.png', 'max-iteration': 100,
                 'percent-red': 12, 'percent-green': 15, 'percent-blue': 20})
    mandelbrot(args)


if __name__ == '__main__':
    main()
