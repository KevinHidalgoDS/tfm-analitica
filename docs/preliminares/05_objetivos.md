---
title: Objetivos
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

# Objetivos

## Objetivos generales

Diseñar, implementar y evaluar un marco de trabajo híbrido para detectar observaciones atípicas
que integre métodos estadísticos clásicos, métodos de aprendizaje automático y un autocodificador,
con una API local y un tablero de visualización, para evaluar el desempeño de detección y la utilidad
de los resultados en conjuntos de datos tabulares procesados por lotes.

## Objetivos específicos

1. Revisar y sistematizar de manera crítica los métodos estadísticos, de aprendizaje automático y
   de aprendizaje profundo existentes para detectar observaciones atípicas, identificando sus
   supuestos, fortalezas, limitaciones y condiciones de aplicabilidad, con el fin de fundamentar la
   selección de las técnicas que integrará el marco de trabajo propuesto.
2. Diseñar e implementar un marco de trabajo para detectar observaciones atípicas que combine,
   mediante la agregación ponderada de puntuaciones de atipicidad normalizadas, métodos estadísticos
   clásicos, métodos de aprendizaje automático y un autocodificador, y evaluar su desempeño
   comparativo según el método, el tipo de observación atípica y la dimensionalidad (precisión,
   exhaustividad, medida F1, área bajo la curva ROC (AUC-ROC) y área bajo la curva de
   precisión-exhaustividad (AUC-PR)) sobre conjuntos de referencia tabulares con observaciones
   atípicas etiquetadas.
3. Implementar una API local que permita ejecutar el marco de trabajo de detección sobre conjuntos
   tabulares procesados por lotes y exponer sus resultados al tablero de visualización.
4. Construir un tablero interactivo de visualización que presente los resultados de detección en
   indicadores comprensibles para sus usuarios, y evaluar mediante un experimento entre sujetos la
   comprensión, exactitud, tiempo de interpretación y utilidad percibida frente a una lista de
   resultados, con usuarios no especializados en estadística.
