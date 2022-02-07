# Fractales

Recopilación de scripts creados en python con el uso de la librería estándar
para generar algunos fractales.

## Imagenes
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_red.png)
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/fractal.png)
![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/fractal.png)
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot.png)


# Examples
python main.py --mandelbrot --size 1000 1000 -s --show -vvv --image-mode P -pnd black red
python main.py --mandelbrot --size 1000 1000 -s --show -vvv --image-mode P -pnd black yellow red black





# MANDELBROT
# Mandelbrot

El conjunto de mandelbrot se define con la sucesión recursiva

![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/ecuacion.png)

donde c es un punto arbitrario en el plano complejo, se dice que un punto
c pertenece al conjunto si la sucesión esta acotada. Este programa genera una imagen
(con formato png, jpg u otro manejado por PIL, modulo de python) que representa dicho
conjunto, usando un algoritmo de escape en el que se itera sobre todos los puntos del
plano complejo c = x + iy donde -2 < x < 2 y -2 < y < 2. Para saber si un punto c esta en
el conjunto, se itera hasta un número dado y dependiendo de cuantas iteraciones
sean necesarias para considerarla como una sucesión no acotada, se le asigna un color.

Si se ejecuta sin argumentos da como resultado la siguiente imagen:
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_default.png)

usage:

     mandelbrot.py [-h] [-n FILENAME] [--size WIDTH HEIGHT] [-w WIDTH]
                     [--height HEIGHT] [-x xi xf] [-y yi yf] [-bc R G B]
                     [-p RED GREEN BLUE] [-pr RED] [-pg GREEN] [-pb BLUE]
                     [-m MAX_ITERATION]

optional arguments:

     -h, --help            show this help message and exit
     -n FILENAME, --name-image FILENAME
                        name of output image. Default value is mandelbrot.png
     --size WIDTH HEIGHT   size of output image in pixels. Default value is (360,
                        360)
     -w WIDTH, --width WIDTH
                        width of the output image
     --height HEIGHT       height of the output image
     -x xi xf, --xinterval xi xf
                        interval of visualisation in the X axis
     -y yi yf, --yinterval yi yf
                        interval of visualisation in the Y axis
     -bc R G B, --background-color R G B
     -p RED GREEN BLUE, --percents RED GREEN BLUE
                        percents of each colors. Default value is (12.0, 15.0,
                        20.0)
     -pr RED, --percent-red RED
                        percent of color red
     -pg GREEN, --percent-green GREEN
                        percent of color green
     -pb BLUE, --percent-blue BLUE
                        percent of color blue
     -m MAX_ITERATION, --max-iteration MAX_ITERATION
                        maximum iteration. Default value is 100


## Ejemplos

Funciona con python 3

python mandelbrot.py --percent-red 1

![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/add.png)

python mandelbrot.py --size 5000 5000 --percents 60 40 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_5000.png)

python mandelbrot.py --size 1000 1000 --percents 20 1 1
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_red.png)

python mandelbrot.py --size 1000 1000 --percents 1 1 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_blue.png)

python mandelbrot.py --size 1000 1000 --percents 1 20 1
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_green.png)

python mandelbrot.py --size 1000 1000 --percents 20 20 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_gray.png)

python mandelbrot.py --size 1000 500 --percents 2 4 6 -m 1000 -x -2 2 -y 0 2
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_good.png)


# BARNSLEY

# Barnsley Fern


Si se ejecuta el programa sin argumentos la imagen obtenida es:

![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/barnsley.png)

## Ejemplos

Funciona con python 3

python barnsley.py --size 1024 1024 --color RED -i 100000
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/ej2.png)

python barnsley.py --size 1024 1024 --color Green -i 500000 -n ej3.png
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/ej3.png)

python barnsley.py --size 1024 1024 -x 0 2.5 -y 5 7.5 -i 1000000
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/ej4.png)


# SIERPINSKI
# Alfombra de Sierpinski

Cuando se ejecuta el script sin argumentos da como resultado la siguiente imagen

![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/sierpinski.png)

Los argumentos permitidos son:
  * **-n o --name-image**: nombre de la imagen de salida
  * **-l o --length**: es un entero que especifica el tamaño de la imagen de salida.
  * **-b o --background**: color de fondo de la imagen.
  * **-t o --tiles**: color de los cuadros
  * **-rl o --recursion-level**: indica el nivel de recursión para la construcción de la imagen
  * **-h o --help**: ayuda.
  * **--version**: muestra versión.


Los colores permitidos son:
  * WHITE
  * BLACK
  * CYAN
  * GREEN
  * BLUE
  * YELLOW
  * ORANGE
  * MAGENTA
  * SILVER
  * PURPLE
  * TEAL
  * GRAY
  * RED
  * BROWN
  * GOLDEN

  ## Ejemplo.
  Funciona con python 2 y python 3.

  python sierpinski.py -b WHITE --tiles RED -rl 6

  ![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/sierpinski_red.png)
