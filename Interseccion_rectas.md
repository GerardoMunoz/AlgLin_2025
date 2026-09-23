# Intersecciones y ángulos en $\mathbb{R}^3$

## Objetivos

- Determinar cuándo dos rectas se intersectan, son paralelas o son alabeadas.
- Analizar la intersección de dos masas en movimiento cuando sus parámetros dependen de tiempos distintos.
- Determinar la intersección entre una recta y un plano.
- Determinar la intersección entre dos planos.
- Describir los ángulos entre conjuntos afines en  y caracterizar cuándo son ortogonales.

---

## 1. Conjuntos Afín en $\mathbb{R}^3$

Un **conjunto afín** en $R^3$ es un conjunto solución de un sistema de ecuaciones con 3 variables ($x, y, z$). Corresponden a puntos, rectas, planos, todo  $\mathbb{R}^3$ o incluso al conjunto vacío solo cuando el sistema es inconsistente.

* $\vec{v}$ es la **dirección de una recta** $$X=P + t\vec{v}$$ 

* $\vec{n}$ es la **dirección de un plano** $$(X-P) \cdot \vec{n}$$ en este último caso la dirección del plano es perpendicular al plano. 

El **ángulo entre dos conjuntos afines (con dirección)** es el ángulo entre sus direcciones. Por lo tanto, son **paralelos** o **perpendiculares** si sus direcciones son paralelas o perpendiculres respectivamente.

## 2. Dos rectas en $\mathbb{R}^3$

Sean dos rectas:

$$L_1 = \{ P_1 + t_1\vec{v}_1 \mid t_1\in \mathbb{R}\}, \ \ \ \ \ \ L_1 :  P_1 + t_1\vec{v}_1$$
$$L_2 = \{ P_2 + t_2\vec{v}_2 \mid t_2\in \mathbb{R}\}, \ \ \ \ \ \ L_2 :  P_2 + t_2\vec{v}_2$$



Hay tres posibilidades geométricas principales:

- **Se intersectan:** comparten exactamente un punto.
- **Son paralelas distintas:** tienen direcciones paralelas, pero no comparten puntos.
- **Son alabeadas:** no son paralelas y tampoco se intersectan.

> Dos rectas distintas en $\mathbb{R}^3$ pueden no cortarse aunque no sean paralelas. Este fenómeno no pasa en $\mathbb{R}^2$.

---

## 2.a. Intersección de dos rectas mediante ecuaciones de planos

Cada recta en $\mathbb{R}^3$ puede describirse como la intersección de dos planos no paralelos:


$$
L_1:
\begin{cases}
a_1x+b_1y+c_1z=d_1,\\
a_2x+b_2y+c_2z=d_2,
\end{cases}
$$

y

$$
L_2:
\begin{cases}
a_3x+b_3y+c_3z=d_3,\\
a_4x+b_4y+c_4z=d_4.
\end{cases}
$$

Para encontrar la intersección, basta resolver simultáneamente las cuatro ecuaciones:

$$
[A:\vec{b}]=
\begin{bmatrix}
a_1 & b_1 & c_1 & : & d_1 \\
a_2 & b_2 & c_2 & : & d_2 \\
a_3 & b_3 & c_3 & : & d_3 \\
a_4 & b_4 & c_4 & : & d_4 \\
\end{bmatrix}
$$


Como hay tres incógnitas se pueden tener esto casos:

- **Una única solución:** las dos rectas se intersectan en un punto.
- **Infinitas soluciones:** las rectas coinciden.
- **Ninguna solución:** las rectas no tienen puntos en común.


### Ventaja de este método

Es especialmente útil cuando las rectas ya están dadas como intersecciones de planos. El problema geométrico se transforma directamente en un problema de álgebra lineal.

---

## 2.b. Intersección de dos rectas mediante ecuaciones vectoriales

Escribimos

$$
X_1=P_1+t_1\vec{v}_1,
$$

$$
X_2=P_2+t_2\vec{v}_2,
$$

Aquí **cada recta tiene su propio parámetro**. Para encontrar una intersección debemos hallar $t_1$ y $t_2$, igualando $$X_1=X_2$$ 


luego pasamos pasamos las variables $t_1, t_2$ a la izquierda y las constantes a la derecha 

$$
t_1\vec{v}_1-t_2\vec{v}_2=P_2 - P1
$$

Esto produce un sistema de tres ecuaciones con dos incógnitas:

$$
\begin{cases}
t_1 v_{1x}- t_2v_{2x}=(P_{2x}-P_{1x}),\\
t_1 v_{1y}- t_2v_{2y}=(P_{2y}-P_{1y}),\\
t_1 v_{1z}- t_2v_{2z}=(P_{2z}-P_{1z}),\\
\end{cases}
$$

$$
[A:\vec{b}]=
\begin{bmatrix}
v_{1x} & -v_{2x} &  : & P_{2x}-P_{1x} \\
v_{1y} & -v_{2y} &  : & P_{2y}-P_{1y} \\
v_{1z} & -v_{2z} &  : & P_{2z}-P_{1z} \\
\end{bmatrix}
$$

### Casos

- **Existe una solución $(t_1,t_2)$:** las rectas se intersectan.
- **No existe solución y $\vec{v}_1$ es paralelo a $\vec{v}_2$:** son rectas paralelas distintas.
- **No existe solución y $\vec{v}_1$ no es paralelo a $\vec{v}_2$:** son rectas alabeadas.
- **Si $P_2-P_1$ es paralelo a la dirección común cuando $u\parallel v$:** las rectas coinciden.


---

## 3. Dos masas en movimiento

Consideremos dos masas puntuales que se mueven en el espacio:

$$
X_1=P_1+t\vec{v}_1,
$$

$$
X_2=P_2+t\vec{v}_2,
$$

La diferencia conceptual respecto al caso 1.b es importante:

- en una intersección geométrica de rectas, $t_1$ y $t_2$ son parámetros diferentes;
- en un problema de movimiento,  $t_1$ y $t_2$ representan **tiempo**.  $t_1=t_2=t$






## 3. Intersección de una recta y un plano

Para la intersección entre una recta y un plano podemo encontrar dos procedimientos dependiendo si la recta está escrita vectorialmente o como una intersección de planos. 

Se deja como ejercico explorar estos dos procedimientos.
