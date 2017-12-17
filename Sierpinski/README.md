# Cuadro de Sierpinski

El script principal es sierpinski.py (se neccesita Args.py para funcionar) cuando
se ejecuta sin argumentos da como resultado la siguiente imagen

![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/sierpinski.png)

Los argumentos que permiten son:
  * **length**: es un entero que especifica el tamaño de la imagen de salida.
  * **name**: nombre de la imagen de salida
  * **deep**: indica el nivel de recursión para la construcción de la imagen
  * **background**: color de fondo de la imagen.
  * **tiles**: color de los cuadros
  
  
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
  
  python sierpinski.py -background WHITE -tiles RED -deep 6
  
  ![](https://github.com/Luispapiernik/Fractales/blob/master/Sierpinski/Images/sierpinski_red.png)
