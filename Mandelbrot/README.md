# Mandelbrot

El conjunto de mandelbrot se define con la sucesion recursiva z_{n + 1} = z_n + c
donde z_0 = 0 y c es un punto arbitrario en el plano complejo, se dice que un punto
c pertenece al conjunto si la sucesion esta acotada. Este programa genera una imagen
(formato png, jpg u otro manejado por PIL, modulo de python) que representa dicho
conjunto usando un algoritmo de escape en el que se itera sobre todos los puntos del
plano complejo x + iy donde -2 < x < 2 y -2 < y < 2. Para saber si un punto c esta en
el conjunto, se itera hasta un numero maximo y dependiendo de cuantas iteraciones
sean necesarias para considerarla como una sucesion no acotada se le asigna un color.

El script principal es mandelbrot.py. Si se ejecuta sin argumentos da como
resultado la siguiente imagen:
![](mandelbrot_default.png)

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
Imagen generada con el comando:
python mandelbrot.py -width 5000 -height 5000 -percent_red 60 -percent_green 40 -percent_blue 20 -scale 1250
![](mandelbrot_e1.png)

Imagen generada con el comando:
python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 20 -percent-blue 1 -percent-green 1
![](mandelbrot_red.png)

Imagen generada con el comando:
python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 1 -percent-blue 20 -percent-green 1
![](mandelbrot_blue.png)

Imagen generada con el comando:
python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 1 -percent-blue 1 -percent-green 20
![](mandelbrot_green.png)

Imagen generada con el comando:
python mandelbrot.py -width 1000 -height 1000 -scale 250 -percent-red 20 -percent-blue 20 -percent-green 20
![](mandelbrot_gray.png)

Imagen generada con el comando:
python mandelbrot.py -max-iteration 1000 -percent-red 2 -percent-green 4 -percent-blue 6 -width 1000 -height 1000 -scale 250
![](mandelbrot_good.png)