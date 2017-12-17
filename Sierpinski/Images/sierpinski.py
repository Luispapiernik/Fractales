from PIL import Image
from Args import Args

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

    args = Args({'length': 360, 'name': 'sierpinski.png', 'deep': 3,
                 'background': 'BLACK', 'tiles': 'WHITE'})

    length = args['length']
    img = Image.new("RGB", (length, length))

    square(COLORS[args['background']], (0, 0), length)
    sierpinski(COLORS[args['tiles']], args['deep'], (0, 0), length)

    img.save(args['name'])


if __name__ == '__main__':
    main()
