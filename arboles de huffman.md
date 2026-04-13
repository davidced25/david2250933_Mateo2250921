Árboles de Huffman
==================

**Integrantes:**
- **David Cediel - 2250933**
- **Mateo Amaya - 2250921**

---

## Introducción

Los **árboles de Huffman** son una técnica utilizada en informática para la **compresión de datos sin pérdida**, desarrollada por **David A. Huffman en 1952**. Su propósito principal es representar información de forma más eficiente reduciendo la cantidad de bits necesarios.

Este método asigna **códigos más cortos a los símbolos más frecuentes** y códigos más largos a los menos frecuentes, logrando así una mejor optimización del almacenamiento.

---

### ¿Qué es el algoritmo de Huffman?

El algoritmo de Hufman construye un **arbol binario** donde:

- Cada hoja representa un símbolo.
- Cada camino desde la raíz hasta una hoja genera un código binario.
- Se cumple la propiedad de **prefijo**, es decir, ningún código es inicio de otro.

> "El algoritmo asigna códigos de longitud variable a los caracteres según su frecuencia."
> — GeeksforGeeks

---

## Funcionamiento del algoritmo

El algoritmo sigue un enfoque **voraz (greedy)**:

1. Se calculan las frecuencias de cada símbolo.
2. Se crean nodos individuales.
3. Se seleccionan los dos nodos con menor frecuencia.
4. Se combinan en un nuevo nodo.
5. Se repite el proceso hasta obtener un único árbol.

> "Se toman los dos árboles de menor frecuencia y se combinan en uno nuevo."
> — Wikipedia

---

### Ejemplo

<div align="center">

| Simbolo | Frecuencia |
|:------:|:----------:|
| A      | 5          |
| B      | 9          |
| C      | 12         |
| D      | 13         |
| E      | 16         |
| F      | 45         |

</div>

Después de aplicar el algoritmo:

<div align="center">

| Símbolo | Código |
|:------:|:------:|
| F      | 0      |
| C      | 100    |
| D      | 101    |
| A      | 1100   |
| B      | 1101   |
| E      | 111    |

</div>

---

## Características importantes

- **Compresión sin pérdida de información**
- Uso de **árboles binarios**
- Basado en la **frecuencia de aparición**
- Utiliza **códigos de longitud variable**
- Garantiza **codificación sin ambigüedad**

---

## Fundamentación teórica

El algoritmo de Huffman se basa en la idea de optimizar la codificación de datos:

> "Los códigos más cortos se asignan a los caracteres más frecuentes."
> — MDPI

Esto permite:

- Reducir el tamaño total de los datos.
- Optimizar la transmisión de información.
- Mejorar el almcenamiento.

---

## Checklist de uso con md

### ¿Para qué sirve?

- [x] Compresión de archivos (ZIP)
- [x] Imágenes (JPEG, PNG)
- [x] Audio (MP3)
- [x] Transmisión de datos
- [x] Codificación de texto

### ¿Qué lo hace útil?

- [x] Reduce el tamaño de los datos
- [x] No pierde información
- [x] Es eficiente
- [x] Es ampliamente utilizado

---

## Ventajas y desventajas

<div align="center">

| Ventajas | Desventajas |
|:--------:|:-----------:|
| **Alta compresión** | Requiere conocer frecuencias |
| **Sin perdida de datos** | No siempre es el más óptimo |
| **Algoritmo eficiente** | Se debe almacenar el árbol |

</div>

---

## Referencias

- https://www.geeksforgeeks.org/dsa/huffman-coding-greedy-algo-3/
- https://www.mdpi.com/2624-800X/6/1/1
- https://es.wikipedia.org/wiki/Algoritmo_de_Huffman 

---
