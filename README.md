# Práctica 4 — Planificación de rutas hospitalarias mediante Algoritmos Genéticos

**Autor:**

- Darío Meneses Hernández  

**Asignatura:** Sistemas Inteligentes Aplicados a la Salud  
**Curso:** 4º Año — 1er Cuatrimestre  
**Centro:** Universidad de Burgos  

---

## Descripción del proyecto

En esta práctica se aborda el problema de la **optimización de recorridos dentro de un hospital**, empleando **algoritmos genéticos** combinados con el algoritmo de búsqueda **A\*** para el cálculo realista de los costes de desplazamiento.

El hospital se modela como un mapa con pasillos, obstáculos y diferentes servicios clínicos y logísticos. De este modo, el coste entre dos puntos no depende únicamente de la distancia geométrica, sino de la estructura real del entorno hospitalario, que se tiene en cuenta mediante la búsqueda A\*.

La práctica se divide en **dos ejercicios independientes**, ambos resueltos siguiendo la metodología explicada en clase y utilizando la librería **DEAP** para la implementación del algoritmo genético.

---

## Objetivos de la práctica

Los objetivos principales de esta práctica son:

- Aplicar algoritmos genéticos a problemas reales de planificación de rutas.
- Analizar la influencia de los parámetros del algoritmo genético en la calidad de las soluciones.
- Comparar distintas configuraciones experimentales mediante métricas objetivas.
- Representar visualmente las rutas óptimas obtenidas sobre el mapa del hospital.
- Interpretar los resultados en un contexto realista de planificación hospitalaria.

---

## Ejercicio 1 — Ronda clínica simulada

En el primer ejercicio se simula una **ronda clínica** en la que un médico debe:

- Partir de un despacho concreto.
- Visitar un conjunto determinado de habitaciones.
- Finalizar el recorrido en la UCI.

El problema consiste en **optimizar el orden de visita** para minimizar el coste total del recorrido. Para ello, se prueban varias configuraciones del algoritmo genético, variando operadores y parámetros como la probabilidad de cruce, mutación, tamaño de población y número de generaciones.

Los costes entre habitaciones se calculan previamente mediante el algoritmo A\*, teniendo en cuenta la estructura real del hospital.

---

## Ejercicio 2 — Planificación logística automatizada

En el segundo ejercicio se simula el comportamiento de un **robot logístico hospitalario** encargado de repartir material.

El robot:
- Parte de la farmacia.
- Debe visitar distintos servicios (RX, AP, LAB, Q1, Q2, UE1, UE2, UCI1 y UCI2).
- Regresa finalmente a la farmacia.

Este ejercicio se plantea como una **ruta cerrada**, lo que añade complejidad al problema, ya que el coste total depende del conjunto completo del recorrido y no solo de decisiones locales.

Al igual que en el ejercicio anterior, se comparan distintas configuraciones del algoritmo genético, evitando repetir exactamente las mismas configuraciones usadas en el ejercicio 1.

---

## Entorno y dependencias

Para garantizar la correcta ejecución de la práctica y la reproducibilidad de los resultados, el proyecto se ha desarrollado utilizando el siguiente entorno de trabajo:

```yaml
entorno:
  lenguaje: Python
  version_python: ">=3.10"

dependencias:
  - nombre: numpy
    descripcion: Operaciones numéricas y manejo de arrays
  - nombre: pandas
    descripcion: Manipulación y análisis de datos
  - nombre: matplotlib
    descripcion: Generación de gráficas y visualización de resultados
  - nombre: deap
    descripcion: Implementación del algoritmo genético
  - nombre: functools
    descripcion: Utilidades del lenguaje (LRU cache)
  - nombre: time
    descripcion: Medición de tiempos de ejecución

ejecucion:
  notebook_principal: Practica4-Resolucion.ipynb
  modo_ejecucion: "Ejecución secuencial de todas las celdas (Run All)"
  salida:
    - Tablas comparativas de resultados
    - Gráficas de convergencia
    - Visualización de rutas óptimas sobre el mapa del hospital


Toda la implementación y los experimentos se encuentran en el notebook:

