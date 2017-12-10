from Args import Args
from PIL import Image


def mandelbrot(args):
    limit = args['max_iteration']
    r = args['percent_red'] / 100
    g = args['percent_green'] / 100
    b = args['percent_blue'] / 100
    limit2 = max(r, g, b) * limit
    x, y = args['width'], args['height']
    scale = args['scale']
    img = Image.new("RGB", (x, y))
    for y0 in range(0, x):
        for x0 in range(0, y):
            z0 = complex((x0 - (x / 2)) / scale, (y0 - (y / 2)) / scale)
            z = complex(0, 0)
            iteration = 0
            while (abs(z) < 2) and (iteration <= limit2):
                z = (z ** 2) + z0
                iteration += 1
            if iteration < (r * limit):
                img.putpixel((x0, y0),
                             (int(255 * iteration / (r * limit)), 0, 0))
            elif iteration < (g * limit):
                img.putpixel((x0, y0),
                             (0, int(255 * iteration / (g * limit)), 0))
            elif iteration < (b * limit):
                img.putpixel((x0, y0),
                             (0, 0, int(255 * iteration / (b * limit))))
            else:
                img.putpixel((x0, y0), (0, 0, 0))
    img.save(args['name'])
    img.show()


def main():
    args = Args({'width': 360, 'height': 360, 'scale': 90.0,
                 'name': 'mandelbrot.png', 'max_iteration': 100,
                 'percent_red': 30, 'percent_green': 50, 'percent_blue': 60})
    mandelbrot(args)


if __name__ == '__main__':
    main()
