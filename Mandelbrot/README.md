# Mandelbrot

El conjunto de mandelbrot se define con la sucesión recursiva $$ z_{n+1} = z_{n} + c $$
donde z_0 = 0 y c es un punto arbitrario en el plano complejo, se dice que un punto
c pertenece al conjunto si la sucesion esta acotada. Este programa genera una imagen
(con formato png, jpg u otro manejado por PIL, modulo de python) que representa dicho
conjunto usando un algoritmo de escape en el que se itera sobre todos los puntos del
plano complejo c = x + iy donde -2 < x < 2 y -2 < y < 2. Para saber si un punto c esta en
el conjunto, se itera hasta un numero dado y dependiendo de cuantas iteraciones
sean necesarias para considerarla como una sucesion no acotada se le asigna un color.

El script principal es mandelbrot.py. Si se ejecuta sin argumentos da como
resultado la siguiente imagen:
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_default.png)

Los argumentos que permite son:

    * width, height: es un entero que especifica el ancho y alto de la
        imagen repectivamente
    * scale: numero de pixeles que representa el uno del plano complejo,
        es aconsejable que sea un cuarto de width o height.
    * name: nombre del archivo de salida
    * max-iteration: maxima iteración, entre mas alto sea este numero mas demora
        la ejecucion pero la imagen queda con mejor calidad.
    * percent-red, percent-green, percent-blue: porcentaje de iteraciones
        en el que se considera rojo, verde y azul respectivamente.


## Ejemplos

python mandelbrot.py -width 5000 -height 5000 -percent-red 60 -percent-green 40 -percent-blue 20 -scale 1250
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_5000.png)

python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 20 -percent-blue 1 -percent-green 1
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_red.png)

python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 1 -percent-blue 20 -percent-green 1
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_blue.png)

python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 1 -percent-blue 1 -percent-green 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_green.png)

python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 20 -percent-blue 20 -percent-green 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_gray.png)

python mandelbrot.py -max-iteration 1000 -percent-red 2 -percent-green 4 -percent-blue 6 -width 1000 -height 1000 -scale 250
![](https://github.com/Luispapiernik/Fractales/blob/master/Mandelbrot/Images/mandelbrot_good.png)
