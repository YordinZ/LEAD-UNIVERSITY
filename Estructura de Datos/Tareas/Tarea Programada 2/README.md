# Tarea Programada 2: Agencia de Seguridad del Reino

Solucion de dos problemas clasicos de Backtracking, desarrollada para el
curso de Estructuras de Datos / Algoritmos. LEAD University.

## Estructura del proyecto

```
agencia_seguridad_reino/
├── main.py            # Menu interactivo principal
├── n_reinas.py         # Problema 1: N-Reinas
├── subconjuntos.py     # Problema 2: Suma de subconjuntos
├── validaciones.py     # Validacion de entradas reutilizable
└── README.md
```

## Requisitos

- Python 3.8 o superior.
- No se requieren librerias externas (unicamente la libreria estandar).

## Ejecucion

```
python main.py
```

El programa muestra un menu con tres opciones:

1. **Vigilancia del Castillo (N-Reinas):** solicita el tamano del tablero
   N, resuelve el problema con Backtracking, muestra una solucion valida
   representada con `Q` (guardia) y `.` (casilla vacia), e indica el total
   de soluciones encontradas para ese N.
2. **Gestion de Recursos del Reino (Subconjuntos):** solicita una lista de
   enteros no negativos y una suma objetivo, y muestra todos los
   subconjuntos cuya suma sea exactamente igual al objetivo, ademas del
   total de soluciones encontradas.
3. **Salir:** termina el programa.

Ambas opciones permiten repetir el proceso con distintos valores sin
salir del programa, mediante una confirmacion (s/n) al finalizar cada
ejecucion.

## Algoritmos

### N-Reinas

Cada fila del tablero recibe un unico guardia. La posicion se representa
como una lista donde el indice es la fila y el valor es la columna
asignada. Antes de colocar un guardia se verifica que no exista conflicto
de columna ni de diagonal con guardias colocados en filas anteriores
(`es_posicion_segura`). Si una fila no admite ninguna columna valida, se
deshace la ultima decision y se prueba la siguiente opcion (backtrack).

### Suma de subconjuntos

Los recursos se ordenan de forma ascendente. El algoritmo recorre la
lista decidiendo, en cada paso, incluir o no el recurso actual en el
subconjunto que se esta construyendo. Si la suma parcial alcanza el
objetivo, el subconjunto se guarda como solucion. Si la suma parcial
supera el objetivo, se descarta esa rama sin seguir explorando (poda),
ya que el resto de los recursos solo puede aumentar la suma.

## Autor

Yordin Herrera (ChanchoxMonte)
