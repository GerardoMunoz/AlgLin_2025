# Solucionario
1. (2 puntos) Para la recta que pas por los puntos 
$P=\begin{pmatrix}1\\0\\2\end{pmatrix}$ y $Q=\begin{pmatrix}1\\1\\0\end{pmatrix}$, encontrar:
  * a. Ecuación vectorial $P+t\vec{v}$ (dibujar el punto $P$ y la flecha $\vec{v}$)

    * $\vec{v}=Q-P=\begin{pmatrix}1\\1\\0\end{pmatrix}-\begin{pmatrix}1\\0\\2\end{pmatrix}=\begin{pmatrix}0\\1\\-2\end{pmatrix}$

    * $\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}1\\0\\2\end{pmatrix}+t\begin{pmatrix}0\\1\\-2\end{pmatrix}$

  * b. Ecuaciones simétricas (dibujar la línea)
    *  $x=1$. Porque no permite despejar t.
    * $t=\frac{y-0}{1}=\frac{z-2}{-2}$

  * c. Dos planos (ecuaciones lineales) que se intersecan sobre la recta (dibujar los dos planos)
    * $1x + 0y + 0z =1$
    * $0x - 2y - 1z =-2$

2. (2 puntos) Para el plano que pasa por el punto $P'=\begin{pmatrix}2\\2\\2\end{pmatrix}$ y es perpendicular al vector $\vec{w}=\begin{pmatrix}1\\1\\1\end{pmatrix}$. encontrar:

  * Ecuación punto-perpendicular $(\vec{\chi}-P')\cdot \vec{w}=0$ (dibujar el punto y la flecha perpendicular)
    *  $\left(\begin{pmatrix}x\\y\\z\end{pmatrix}-\begin{pmatrix}2\\2\\2\end{pmatrix}\right)\cdot \begin{pmatrix}1\\1\\1\end{pmatrix}=0$

  * Ecuación lineal del plano (dibujar el plano)
    *  $1x+1y+1z-1{*}2-1{*}2-1{*}2=0$
    *  $1x+1y+1z=6$

  * Ecuación vectorial del plano $R + t_1\vec{v}_1 + t_2\vec{v}_2$ (dibujar $R$, $\vec{v}_1$, $\vec{v}_2$)
    * Variables líbres: $y=t_1$, $z=t_2$
    * Despeje de variables delanteras: $x=6-t_1-t_2$
    * Solución general: $\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}6\\0\\0\end{pmatrix}+t_1\begin{pmatrix}-1\\1\\0\end{pmatrix}+t_2\begin{pmatrix}-1\\0\\1\end{pmatrix}$ 
* Tres puntos en el plano (dibujar los tres puntos)
    * Solución particular trivial $(t_1,t_2)=(0,0)$:  $\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}6\\0\\0\end{pmatrix}$
    * 1° Solución particular básica $(t_1,t_2)=(1,0)$:  $\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}5\\1\\0\end{pmatrix}$
    * 2° Solución particular básica $(t_1,t_2)=(0,1)$:  $\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}5\\0\\1\end{pmatrix}$
    ```json
[
    {
        "tipo": "Punto",
        "nombre": "1a P",
        "data": {
            "pos": {
                "x": 1,
                "y": 0,
                "z": 2
            }
        }
    },
    {
        "tipo": "Flecha",
        "nombre": "1a v",
        "data": {
            "origin": {
                "x": 1,
                "y": 0,
                "z": 2
            },
            "dir": {
                "x": 0,
                "y": 1,
                "z": -2
            }
        }
    },
    {
        "tipo": "Línea",
        "nombre": "1b",
        "data": {
            "p1": {
                "x": 1,
                "y": 0,
                "z": 2
            },
            "p2": {
                "x": 1,
                "y": 1,
                "z": 0
            }
        }
    },
    {
        "tipo": "Plano",
        "nombre": "1c1",
        "data": {
            "a": 1,
            "b": 0,
            "c": 0,
            "d": 1
        }
    },
    {
        "tipo": "Plano",
        "nombre": "1c2",
        "data": {
            "a": 0,
            "b": -2,
            "c": -1,
            "d": -2
        }
    },
    {
        "tipo": "Flecha",
        "nombre": "2a w",
        "data": {
            "origin": {
                "x": 2,
                "y": 2,
                "z": 2
            },
            "dir": {
                "x": 1,
                "y": 1,
                "z": 1
            }
        }
    },
    {
        "tipo": "Punto",
        "nombre": "2a P'",
        "data": {
            "pos": {
                "x": 2,
                "y": 2,
                "z": 2
            }
        }
    },
    {
        "tipo": "Plano",
        "nombre": "2b",
        "data": {
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 6
        }
    },
    {
        "tipo": "Punto",
        "nombre": "2c R",
        "data": {
            "pos": {
                "x": 6,
                "y": 0,
                "z": 0
            }
        }
    },
    {
        "tipo": "Flecha",
        "nombre": "2c v_1",
        "data": {
            "origin": {
                "x": 6,
                "y": 0,
                "z": 0
            },
            "dir": {
                "x": -1,
                "y": 1,
                "z": 0
            }
        }
    },
    {
        "tipo": "Flecha",
        "nombre": "2c v_2",
        "data": {
            "origin": {
                "x": 6,
                "y": 0,
                "z": 0
            },
            "dir": {
                "x": -1,
                "y": 0,
                "z": 1
            }
        }
    },
    {
        "tipo": "Punto",
        "nombre": "2d R'",
        "data": {
            "pos": {
                "x": 5,
                "y": 1,
                "z": 0
            }
        }
    },
    {
        "tipo": "Punto",
        "nombre": "2d Q'",
        "data": {
            "pos": {
                "x": 5,
                "y": 0,
                "z": 1
            }
        }
    }
]
```
    





