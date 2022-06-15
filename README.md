# Fractal Generator <!-- no toc -->

This is a solution that allows you to generate various fractals in an efficient way.

- [About fractals](#about-fractals)
  - [Mandelbrot](#mandelbrot)
  - [Barnsley](#barnsley)
  - [Sierpinski](#sierpinski)
- [Usage](#usage)
  - [Some Examples](#some-examples)
  - [TODO](#todo)

## About fractals
A [fractal](https://en.wikipedia.org/wiki/Fractal) is a term used to describe geometric shapes containing detailed structure at arbitrarily small scales. Because of the trouble involved in finding one definition for fractals, according to Falconer, fractals should be only generally characterized by a gestalt of the following features:
- **Self-similarity**, which may include:
  - **Exact self-similarity**: identical at all scales.
  - **Quasi self-similarity**: approximates the same pattern at different scales; may contain small copies of the entire fractal in distorted and degenerate forms.
  - **Statistical self-similarity**: repeats a pattern stochastically so numerical or statistical measures are preserved across scales.
  - **Qualitative self-similarity**: as in a time series.
  - **Multifractal scaling**: characterized by more than one fractal dimension or scaling rule
- **Fine** or **detailed structure** at arbitrarily small scales.
- **Irregularity locally** and **globally** that cannot easily be described in the language of traditional Euclidean geometry other than as the limit of a recursively defined sequence of stages.

### Mandelbrot
![](./images/mandelbrot.png)

The [Mandelbrot](https://en.wikipedia.org/wiki/Mandelbrot_set) set is the set of complex numbers $c$ for which the function $f_{c}(z)=z^{2}+c$ does not diverge to infinity when iterated from $z = 0$, i.e., for which the sequence $f_c(0), f_c(f_c(0))$, $\ \dots$, remains bounded in absolute value. Thus, a complex number $c$ is a member of the Mandelbrot set if, when starting with $z_{0}=0$ and applying the iteration repeatedly, the absolute value of $z_{n}$ remains bounded (falls in a circle of a fixed radius $r$) for all $n > 0$.

### Barnsley
![](./images/barnsley.png)

The [Barnsley](https://en.wikipedia.org/wiki/Barnsley_fern) Fern is a fractal named after the British mathematician Michael Barnsley, which is an example of an iterated function system ([IFS](https://en.wikipedia.org/wiki/Iterated_function_system)) to create a fractal. He made it to resemble the black spleenwort using four affine transformations of the form:

$$
f(x,y) =
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
\end{bmatrix}
+
\begin{bmatrix}
e\\
f\\
\end{bmatrix}
$$

given by the values of the following table

w|a|b|c|d|e|f|p|Portion generated
---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---:
$f_1$|0 |	0 |	0 |	0.16| 	0 |	0 	|0.01| 	Stem
$f_2$ |	0.85 |	0.04 |	−0.04 |	0.85 |	0 |	1.60 |	0.85 |	Successively smaller leaflets
$f_3$ |	0.20 |	−0.26 |	0.23 |	0.22 |	0 	|1.60 	|0.07 |	Largest left-hand leaflet
$f_4$ |	−0.15 |	0.28 |	0.26 |	0.24 |	0 |	0.44 |	0.07 |	Largest right-hand leaflet

specifically, the transformations have the form

$$
f_1(x,y) =
\begin{bmatrix}
0 & 0\\
0 & 0.16\\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
\end{bmatrix}
$$

$$
f_2(x,y) =
\begin{bmatrix}
0.85 & 0.04\\
-0.04 & 0.85\\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
\end{bmatrix}
+
\begin{bmatrix}
0\\
1.6\\
\end{bmatrix}
$$

$$
f_3(x,y) =
\begin{bmatrix}
0.2 & -0.26\\
0.23 & 0.22\\
\end{bmatrix}
\begin{bmatrix}
0\\
1.6\\
\end{bmatrix}
+
\begin{bmatrix}
e\\
f\\
\end{bmatrix}
$$


$$
f_4(x,y) =
\begin{bmatrix}
-0.15 & 0.28\\
0.26 & 0.24\\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
\end{bmatrix}
+
\begin{bmatrix}
0\\
0.44\\
\end{bmatrix}
$$

### Sierpinski
![](./images/sierpinski.png)

The [Sierpiński carpet](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_carpet) is a plane fractal that generalize the Cantor set to two dimensions.

## Usage
The complete set of options is given by

```bash
usage: main.py [--help] [-o FILENAME] [-im IMAGE MODE] [--size WIDTH HEIGHT] [-w WIDTH] [-h HEIGHT] [-bc COLOR] [-c COLOR] [--show] [-v] [--version] [-x xi xf] [-y yi yf] [-m MAX_ITERATION]
               [-pn PALETTE_NAME] [-pnd COLOR [COLOR ...]] [-nw NODES_WEIGHTS [NODES_WEIGHTS ...]] [-i] [--barnsley] [--mandelbrot] [-er ESCAPE_RADIUS] [-s] [-p PROCESS_NUMBER] [--sierpinski]

Generates multiples fractals

optional arguments:
  --help                show this help message and exit

General args:
  -o FILENAME, --output-file FILENAME
                        name of output image. (default: fractal.png)
  -im IMAGE MODE, --image-mode IMAGE MODE
                        mode of the output image. This specify what color schema must be applied. (default: L)
  --size WIDTH HEIGHT   size of output image in pixels. (default: (512, 512))
  -w WIDTH, --width WIDTH
                        width of the output image in pixels. (default: None)
  -h HEIGHT, --height HEIGHT
                        height of the output image in pixels. (default: None)
  -bc COLOR, --background-color COLOR
                        background color of the output image. (default: 0)
  -c COLOR, --color COLOR
                        color to paint the fractal in a solid way. (default: 255)
  --show                show the generated fractal. (default: False)
  -v, --verbose
  --version             show program's version number and exit

Geometrical args:
  -x xi xf, --x-interval xi xf
                        interval of visualisation in the X axis (default: (-2, 2))
  -y yi yf, --y-interval yi yf
                        interval of visualisation in the Y axis (default: (-2, 2))
  -m MAX_ITERATION, --max-iteration MAX_ITERATION
                        maximum iteration or recursion level acording to the selected fractal. (default: 20)

Palette args:
  -pn PALETTE_NAME, --palette-name PALETTE_NAME
                        name of the palette to select, all matplotlib palettes are supported. (default: None)
  -pnd COLOR [COLOR ...], --palette-nodes COLOR [COLOR ...]
                        nodes to create a linear segmented palette. (default: None)
  -nw NODES_WEIGHTS [NODES_WEIGHTS ...], --nodes-weights NODES_WEIGHTS [NODES_WEIGHTS ...]
                        weight of the nodes. it must be acomulative up to 1 (default: None)
  -i, --invert-palette  invert the order of the palette colors. (default: False)

Barnsley args:
  --barnsley            generated the barnsley fractal. (default: False)

Mandelbrot args:
  --mandelbrot          generated the mandelbrot fractal. (default: False)
  -er ESCAPE_RADIUS, --escape-radius ESCAPE_RADIUS
                        escape radius of the mandelbrot set. (default: 1000)
  -s, --smooth-bands    smooth the transition between colors in the fractal. (default: False)
  -p PROCESS_NUMBER, --process-number PROCESS_NUMBER
                        number of process for the paralelization, if zero is passed the maximum number allowed will be used. (default: 0)

Sierpinkski args:
  --sierpinski          generated the sierpinski fractal. (default: False)
```

### Some Examples
```bash
python main.py --mandelbrot --smooth-bands -pnd black black red -nw 0 0.5 1 -im P
```
![](./images/example_1.png)


```bash
python main.py --mandelbrot --smooth-bands -pn turbo -im P -i
```
![](./images/example_2.png)

```bash
python main.py --sierpinski -m 3
```
![](./images/example_3.png)

```bash
python main.py --barnsley -m 100000 --x-interval -5 5 --y-interval 0 10 -c green -im RGB
```
![](./images/example_4.png)

### TODO
- Add parameters to control affine transformations of the barnsley fractal.
- Improve the definition of all the fractals and how it is related to the code implementation.
