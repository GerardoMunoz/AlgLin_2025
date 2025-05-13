### Pregunta 1 

**Tema:** Curva de Bézier (2D)

Una curva de Bézier cuadrática se define usando tres puntos y se calcula para un parámetro $ t \in [0, 1] $ mediante la fórmula:

$$
B(t) = (1 - t)^2 P_0 + 2(1 - t)t P_1 + t^2 P_2
$$

Dado el conjunto de puntos:

- $ P_0 = (1, 0) $
- $ P_1 = (0, 1) $
- $ P_2 = (1, 2) $

**Solicitado:**

1. Calcule el punto sobre la curva para $ t = 0.3 $.
2. Calcule el punto sobre la curva para $ t = 0.7 $.

Presente los resultados como coordenadas con 3 cifras decimales.

---


### Pregunta 2 

**Tema:** Actualización Matricial en una Red Neuronal Lineal

Una red neuronal lineal con 3 entradas y 2 salidas (sin activación) utiliza la siguiente regla de actualización para ajustar la matriz de pesos $ W $:

$$
W_{i+1} = W_i + \eta X^T (Y_r - X W_i)
$$

Donde:
- $ W_i \in \mathbb{R}^{3 \times 2} $ es la matriz de pesos actual,
- $ X \in \mathbb{R}^{1 \times 3} $ es el vector de entrada,
- $ Y_r \in \mathbb{R}^{1 \times 2} $ es la salida esperada,
- $ \eta \in \mathbb{R} $ es la tasa de aprendizaje (learning rate).

Considere los siguientes valores:

- $ W_0 = \begin{bmatrix} 1 & 0 \\ -1 & 2 \\ 0 & -1 \end{bmatrix} $
- $ X = \begin{bmatrix} 2 & 1 & -1 \end{bmatrix} $
- $ Y_r = \begin{bmatrix} 1 & 2 \end{bmatrix} $
- $ \eta = 0.1 $

**Solicitado:**

* a) Calcule el producto $ X W_0 $  
* b) Calcule el error $ E = Y_r - X W_0 $  
* c) Calcule la transpuesta de $ X $, es decir $ X^T $  
* d) Calcule el producto $ X^T E $  
* e) Calcule $ \eta (X^T E) $
* f) Calcule la nueva matriz de pesos $ W_1 = W_0 + \eta (X^T E) $

---

### Pregunta 3

**Tema:** Pseudoinversa de una Matriz

Dada la matriz $ A \in \mathbb{R}^{2 \times 3} $:

$$
A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

La pseudoinversa de Moore-Penrose de una matriz $ A $ se puede calcular como:

$$
A^+ = (A^T A)^{-1} A^T
$$

**Solicitado:**

a) Calcule la matriz transpuesta $ A^T $  
b) Calcule el producto $ A^T A $  
c) Halle la inversa de $ A^T A $, si existe  
d) Calcule la pseudoinversa $ A^+ = (A^T A)^{-1} A^T $


Ahora, considere que la matriz $ A $ representa un conjunto de **entradas** y se tiene una matriz de **salidas**:

$$
B = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

e) Calcule la matriz de pesos $ W = A^{+T} B $


---

### Pregunta 4 

**Tema:** Ortogonalidad, Ángulo y Distancia entre Vectores

Dado el siguiente conjunto de vectores en $ \mathbb{R}^3 $:

- $ u = (1, 2, -1) $
- $ w = (0, 1, 1) $
- $ v_1 = (2, -1, 0) $
- $ v_2 = (-1, 2, 1) $
- $ v_3 = (1, 1, 1) $

**Solicitado:**

a) Encuentre un vector $ x \in \mathbb{R}^3 $ que sea ortogonal a **ambos vectores** $ u $ y $ w $.  
b) Determine cuál de los vectores $ v_1, v_2, v_3 $ forma el **menor ángulo** con el vector $ u $.  
c) Determine cuál de los vectores $ v_1, v_2, v_3 $ está a la **menor distancia** del vector $ w $.  
