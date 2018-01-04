# Barnsley Fern

Si se ejecuta el programa sin argumentos la imagen obtenida es:
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/barnsley.png)

 * **-n o --name-image**: nombre de la imagen de salida.
 * **--size**: dupla que indica el tamaño de la imagen de salida.
 * **-w o --width**: entero que indica el ancho de la imagen de salida.
 * **--height**: entero que indica el alto de la imagen de salida.
 * **-c o --color**: color del fractal.
 * **-b o --background**: color de fondo de la imagen.
 * **-z o --zoom**: el fractal queda muy pequeño en la imagen. este parametro es para
    hacerlo visible.
 * **-i o --iteration**: numero de iteraciones que realiza el programa.
    Probablemente sea la misma cantidad de puntos con la que se relice el fractal.
 * **-h o --help**: ayuda.
 * **--version**: muestra la versión.
 
## Ejemplos

Funciona con python 3 y python 2

python barnsley.py -z 20
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/ej1.png)

python barnsley.py --size 3200 3200 --color RED -z 400 -i 10000000
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/ej2.png)

python barnsley.py --size 3200 3200 --color GREEN -z 400 -i 40000000
![](https://github.com/Luispapiernik/Fractales/blob/master/Barnsley/Images/ej3.png)
