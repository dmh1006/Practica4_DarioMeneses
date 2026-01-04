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


## Resultados obtenidos

En ambos ejercicios se han obtenido resultados consistentes y reproducibles, permitiendo comparar distintas configuraciones del algoritmo genético de forma objetiva.

Para cada configuración se han analizado:
- El coste final del recorrido.
- La evolución del fitness medio a lo largo de las generaciones.
- La evolución del mejor fitness alcanzado.
- El tiempo de ejecución y la generación de convergencia.
- La ruta óptima final representada sobre el mapa del hospital.

En el **Ejercicio 1**, las distintas configuraciones convergen hacia soluciones de coste similar, aunque se observan diferencias claras en la velocidad de convergencia. Algunas configuraciones alcanzan rápidamente una solución estable, mientras que otras mantienen una mayor exploración durante más generaciones antes de estabilizarse.

En el **Ejercicio 2**, el comportamiento es similar, aunque el hecho de tratarse de una ruta cerrada introduce una mayor dependencia global entre los puntos visitados. Esto hace que pequeñas variaciones en el orden de visita tengan un impacto más notable en el coste total del recorrido.

Las visualizaciones finales permiten comprobar que las rutas obtenidas son coherentes con la estructura real del hospital y respetan las restricciones impuestas por el mapa.

---

## Análisis y discusión

El análisis de los resultados pone de manifiesto la importancia de la elección de los parámetros del algoritmo genético. Configuraciones con una mayor probabilidad de mutación tienden a explorar durante más tiempo el espacio de soluciones, lo que puede retrasar la convergencia, pero reduce el riesgo de quedar atrapado en óptimos locales. Por el contrario, configuraciones con mayor presión selectiva suelen converger más rápidamente, aunque con menor diversidad genética.

Las gráficas de fitness medio y mejor fitness muestran que, en general, el algoritmo presenta un comportamiento estable y consistente, alcanzando soluciones de buena calidad en un número razonable de generaciones. En algunos casos, el mejor fitness se estabiliza pronto, mientras que el fitness medio continúa mejorando ligeramente, indicando una mejora progresiva del conjunto de la población.

Un aspecto destacable es que el orden de visita obtenido no siempre coincide con la intuición visual inicial. Esto se debe a que el coste real de desplazamiento depende de la estructura del hospital, los pasillos disponibles y las penalizaciones asociadas a determinadas zonas, factores que no se aprecian únicamente observando la proximidad geométrica entre puntos.

En el **Ejercicio 2**, este efecto es más acusado debido a que el recorrido es una ruta cerrada. El algoritmo genético optimiza el coste global del recorrido completo, por lo que algunas decisiones locales que parecen poco intuitivas resultan óptimas cuando se considera el conjunto total del trayecto.

---

## Conclusiones

En esta práctica se ha demostrado que la combinación del algoritmo A* con algoritmos genéticos constituye una herramienta eficaz para resolver problemas de planificación de rutas en entornos complejos como un hospital.

El uso de A* para el cálculo previo de los costes de desplazamiento permite modelar de forma realista el entorno y reduce significativamente el tiempo de evaluación del algoritmo genético. Por su parte, el algoritmo genético permite explorar de manera eficiente el espacio de posibles órdenes de visita, encontrando soluciones de bajo coste sin necesidad de evaluar exhaustivamente todas las combinaciones posibles.

Los resultados obtenidos son coherentes y justificables, y las visualizaciones finales permiten validar de forma clara las soluciones encontradas. Asimismo, el estudio comparativo de distintas configuraciones pone de manifiesto la influencia de los parámetros del algoritmo en su comportamiento y rendimiento.

En conjunto, la práctica cumple los objetivos planteados y muestra la aplicabilidad de las técnicas de inteligencia artificial estudiadas a problemas reales del ámbito hospitalario.

---
