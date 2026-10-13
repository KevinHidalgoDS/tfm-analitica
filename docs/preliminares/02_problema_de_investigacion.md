---
title: Problema de Investigación
author: "Kevin Ferney Hidalgo Higuita"
date: "8 de Septiembre de 2026"
institute: "Universidad Nacional de Colombia, Sede Medellín"
description: "None."
# --- Configuraciones para Pandoc (PDF) ---
lang: es-CO
bibliography: referencias.bib
csl: ieee.csl
# Formato visual del PDF (LaTeX)
geometry:
  - top=2.5cm
  - bottom=2.5cm
  - left=3cm
  - right=2.5cm
fontsize: 12pt
linestretch: 1.15
papersize: letter
toc: true
toc-depth: 2
---

# Problema de Investigación

## Planteamiento del problema

La literatura ha desarrollado y sistematizado diversos métodos para detectar observaciones
atípicas, con enfoques y supuestos distintos [@chandola2009anomaly; @pang2021deep]. En una solución
aplicada, es necesario evaluar el desempeño de detección y facilitar la consulta de los resultados
por parte de sus usuarios. Esta tesis aborda la integración de métodos de detección y su evaluación
en un contexto delimitado de análisis por lotes.

En términos concretos, el problema de investigación se formula mediante la siguiente pregunta
principal: ¿cómo integrar y evaluar métodos estadísticos, de aprendizaje automático y de
aprendizaje profundo para detectar observaciones atípicas en conjuntos de datos tabulares
procesados por lotes, y cómo presentar sus resultados para facilitar su consulta e interpretación
por parte de los usuarios?

Esta pregunta se desglosa en dos preguntas específicas:

1. ¿Qué desempeño de detección alcanzan los métodos estadísticos clásicos, los métodos de
   aprendizaje automático seleccionados y un autocodificador de aprendizaje profundo aplicado a
   datos tabulares, de manera individual y mediante el esquema de combinación definido, sobre
   conjuntos etiquetados?
2. ¿En qué medida un tablero con puntuaciones de atipicidad y variables explicativas mejora la
   comprensión, la exactitud y el tiempo de interpretación de los resultados frente a una lista de
   observaciones detectadas?

## Antecedentes y alcance de la contribución

La revisión de antecedentes, que se ampliará en el estado del arte, organiza el contexto de la
investigación. Para delimitar la contribución propuesta, se consideran tres dimensiones de trabajo:

- **Integración de métodos:** se comparará el desempeño de los métodos estadísticos, los métodos de
  aprendizaje automático seleccionados y un autocodificador de aprendizaje profundo para datos
  tabulares, tanto de manera individual como mediante un esquema de ensamblado por agregación
  ponderada de puntuaciones normalizadas. La comparación se realizará sobre los conjuntos
  etiquetados seleccionados para el estudio. La utilidad del ensamblado se evaluará empíricamente;
  no se presupone que una familia sea superior o más interpretable que otra. Los criterios de
  normalización, ponderación y selección del umbral se especificarán en la metodología y se
  determinarán sin utilizar el conjunto de prueba.
- **Implementación del análisis:** se integrarán los métodos seleccionados en un marco de trabajo
  ejecutable mediante una API local para procesar datos por lotes y exponer resultados al tablero.
- **Presentación de resultados:** se implementará un tablero para consultar los resultados de
  detección. Usuarios no especializados en estadística, con experiencia básica en análisis de
  datos, realizarán tareas definidas previamente: cargar un conjunto tabular, ejecutar la
  detección, localizar observaciones señaladas e inspeccionar las variables asociadas a estas. Se
  registrarán la proporción de respuestas correctas, el tiempo de respuesta, los errores y la
  comprensión percibida, y se aplicará el cuestionario System Usability Scale (SUS) para medir la
  usabilidad percibida [@brooke1996sus]. Estas medidas operacionalizan la efectividad, la
  eficiencia y la satisfacción de uso [@iso9241-11-2018]. La evaluación se refiere a la interfaz y
  a la presentación de resultados; no pretende medir la interpretabilidad intrínseca de los
  modelos. El diseño del tablero seguirá principios de comunicación visual de información
  [@few2006dashboard].

Esta tesis, en su modalidad de profundización, busca implementar y evaluar la solución integrada
para conjuntos de datos tabulares procesados por lotes. Su aporte se circunscribe a los métodos,
componentes de software, datos, escenarios y participantes incluidos en la evaluación; no propone
un algoritmo novedoso ni pretende generalizar sus resultados más allá de esas condiciones.

## Justificación

La pertinencia de este trabajo de profundización radica en el diseño, la integración y la
evaluación contextualizada de una solución aplicada para detectar observaciones atípicas en datos
tabulares procesados por lotes. En la dimensión académica, se reportarán resultados comparativos de
los métodos seleccionados en los conjuntos de datos y bajo las condiciones experimentales
definidas. En la dimensión tecnológica, se implementará y documentará una API local para ejecutar
el análisis. En la dimensión aplicada, se desarrollará un tablero para consultar los resultados y
se evaluará su utilidad con usuarios representativos. Las conclusiones se limitarán a las técnicas,
los conjuntos de datos, las cargas y los participantes incluidos; no se afirmará una generalización
a otros contextos sin evidencia adicional.

## Referencias

\bibliography
