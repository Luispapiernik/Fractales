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

Los argumentos que permite son:

 * **-n o --name-image**: nombre de la imagen de salida.
 * **--size**: dupla que indica el tamaño de la imagen de salida.
 * **-w o --width**: entero que indica el ancho de la imagen de salida.
 * **--height**: entero que indica el alto de la imagen de salida.
 * **--scale**: número de pixeles que representa el uno del plano complejo,
     es conveniente que sea un cuarto del ancho o alto de la imagen.
 * **-p, --percents**: tupla con los porcentaje de iteraciones
     en el que se considera rojo, verde y azul.
 * **-pr o --percent-red, -pg o --percent-green, -pb o --percent-blue**: indica el mismo
     valor que el argumento percents, solo que separado para cada color
 * **-m o --max-iteration**: maxima iteración, entre mas alto sea este número mas demora
     la ejecución pero el conjunto queda mejor representado.
 * **-h o --help**: ayuda.
 * **--version**: muestra la versión.


## Ejemplos

Funciona con python 3 y python 2

python mandelbrot.py --percent-red 1

![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/add.png)

python mandelbrot.py --size 5000 5000 --scale 1250 --percents 60 40 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_5000.png)

python mandelbrot.py --size 1000 1000 --scale 250 --percents 20 1 1
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_red.png)

python mandelbrot.py --size 1000 1000 --scale 250 --percents 1 1 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_blue.png)

python2 mandelbrot.py --size 1000 1000 --scale 250 --percents 1 20 1
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_green.png)

python2 mandelbrot.py --size 1000 1000 --scale 250 --percents 20 20 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_gray.png)

python2 mandelbrot.py --size 1000 1000 --scale 250 --percents 2 4 6 -m 1000
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_good.png)
