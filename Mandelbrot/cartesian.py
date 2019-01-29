from __future__ import division

from PIL import Image
import numpy as np


class Cartesian(object):
    """Esta clase maneja las conversiones entre coordenandas de una matriz y
       coordenadas del plano cartesionano en una region rectangular definida"""

    def __init__(self, xinterval, yinterval, width, height):
        """xinterval: (int, int), yinterval: (int, int), width: int,
        height: int"""
        self.xinterval = xinterval
        self.yinterval = yinterval
        self.height = height
        self.width = width

    def bijection(self, x, y):
        """No es una biyeccion en el sentido matematico"""
        x = (x + self.width / 2) * (self.xinterval[1] - self.xinterval[0]
                                    ) / self.width + self.xinterval[0]
        y = (y + self.height / 2) * (self.yinterval[1] - self.yinterval[0]
                                     ) / self.height + self.yinterval[0]
        return x, y

    def inverse_bijection(self, x, y):
        """No es una biyeccion en el sentido matematico"""
        x = (x - self.xinterval[0]) * self.width / \
            (self.xinterval[1] - self.xinterval[0]) - self.width / 2
        y = (y - self.yinterval[0]) * self.height / \
            (self.yinterval[1] - self.yinterval[0]) - self.height / 2
        return x, y

    def getCoordinate(self, column, row):
        """retorna la coordenada (x, y) en el plano, dada una posicion en la
           matriz"""
        x = column - self.width / 2
        y = -row + self.height / 2
        return self.bijection(x, y)

    def getPosition(self, x, y):
        """retorna una posicion en la matrix dada unas coordenadas (x, y)"""
        x, y = self.inverse_bijection(x, y)
        column = x + self.width / 2
        row = self.height / 2 - y
        return int(column), int(row)


class CartesianImage(Cartesian):
    """Esta clase representa una imagen en el plano cartesiano"""

    def __init__(self, xinterval, yinterval, width, height, color=0,
                 mode='RGB'):
        """El argmento color puede ser especificado con el formato (R, G, B)
           xinterval: (int, int), yinterval: (int, int), width: int,
           height: int"""
        super(CartesianImage, self).__init__(xinterval, yinterval, width,
                                             height)

        self._image = Image.new(mode, (width, height), color)

    def __getattr__(self, key):
        if key == '_image':
            raise AttributeError()
        if key == 'putpixel':
            return getattr(self, key)

        return getattr(self._image, key)

    def putpixel(self, pos, color, toInt=True):
        """pos: (float, float), color: (int, int, int)"""
        if toInt:
            pos = self.getPosition(*pos)
        self._image.putpixel(pos, color)


def testSin():
    image = CartesianImage((-2 * np.pi, 2 * np.pi), (-2, 2), 300, 300)

    for x in np.arange(-2 * np.pi, 2 * np.pi, 0.0001):
        image.putpixel((x, np.sin(x)), (255, 255, 255))

    image.save('seno.png')


def main():
    print('Este programa debe generar la grafica de seno en seno.png')
    testSin()


if __name__ == '__main__':
    main()
