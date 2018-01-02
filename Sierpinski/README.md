# Cuadro de Sierpinski

Cuando se ejecuta el script sin argumentos da como resultado la siguiente imagen

![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/sierpinski.png)

Los argumentos permitidos son:
  * **-l o --length**: es un entero que especifica el tamaño de la imagen de salida.
  * **-n o --name-image**: nombre de la imagen de salida
  * **-rl o --recursion-level**: indica el nivel de recursión para la construcción de la imagen
  * **-b o --background**: color de fondo de la imagen.
  * **-t o --tiles**: color de los cuadros
  
  
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
  
  python sierpinski.py -b WHITE --tiles RED -rl 6
  
  ![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/sierpinski_red.png)
