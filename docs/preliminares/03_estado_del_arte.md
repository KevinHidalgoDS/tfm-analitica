---
title: Estado del arte
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

# Estado del Arte

## Fundamentos estadísticos clásicos de la detección de datos atípicos

La detección de datos atípicos tiene sus raíces en la estadística clásica, con antecedentes que se
remontan a las pruebas de discordancia formuladas desde mediados del siglo XX para identificar
observaciones que se apartan significativamente de una muestra bajo un modelo probabilístico
asumido, tales como la prueba de Grubbs y los criterios basados en el rango intercuartílico. Estos
métodos, fundamentados en supuestos distribucionales (habitualmente normalidad univariante) o en
medidas robustas de dispersión, continúan siendo ampliamente empleados en el control estadístico de
procesos y en la depuración inicial de conjuntos de datos, debido a su simplicidad computacional y
a la claridad de su interpretación estadística. La extensión multivariante de estos enfoques,
mediante medidas como la distancia de Mahalanobis, permitió abordar la detección de anomalías
considerando la estructura de covarianza entre variables, aunque persisten limitaciones frente a
distribuciones no gaussianas y datos de alta dimensionalidad.

## Métodos de aprendizaje automático

El desarrollo del aprendizaje automático amplió sustancialmente el repertorio de técnicas
disponibles. Métodos basados en distancia y densidad, como el Local Outlier Factor y los algoritmos
de vecinos más cercanos, permitieron capturar anomalías de carácter local o contextual, es decir,
observaciones que resultan anómalas en relación con su vecindad aunque no lo sean respecto de la
distribución global de los datos. Por su parte, los métodos de ensamblado basados en árboles de
aislamiento, entre los que destaca Isolation Forest, propuesto originalmente por Liu, Ting y Zhou
(2008)[@liu2008isolation], ofrecieron una alternativa computacionalmente eficiente y con buen
desempeño en espacios de alta dimensionalidad, al aislar observaciones mediante particiones
aleatorias recursivas, asumiendo que las anomalías requieren, en promedio, menos particiones para
ser aisladas que las observaciones normales. Más recientemente, se han propuesto métodos no
paramétricos fundamentados en la función de distribución empírica acumulada, como ECOD y COPOD, que
buscan combinar la eficiencia computacional de los métodos estadísticos con la flexibilidad de los
métodos de aprendizaje automático, prescindiendo de hiperparámetros complejos y logrando un
desempeño competitivo en bancos de pruebas (benchmarks) recientes de detección de anomalías
tabulares.

## Aprendizaje profundo para la detección de anomalías

En paralelo, el aprendizaje profundo ha impulsado el desarrollo de arquitecturas especializadas
para la detección de anomalías, particularmente en datos de alta dimensionalidad, series de tiempo,
imágenes y datos secuenciales complejos. Pang, Shen, Cao y Van Den Hengel (2021)[@pang2021deep]
ofrecen una revisión sistemática de estas técnicas, destacando el uso de autoencoders, modelos
generativos antagónicos (GAN) y arquitecturas de representación profunda para identificar anomalías
a partir del error de reconstrucción o de la verosimilitud estimada. En el ámbito específico de las
series de tiempo, la revisión de Darban, Webb, Pan, Aggarwal y Salehi (2024)[@darban2024deep],
publicada en ACM Computing Surveys, ofrece una taxonomía exhaustiva de los modelos de aprendizaje
profundo aplicados a la detección de anomalías temporales, clasificándolos según su estrategia de
detección (basada en pronóstico, en reconstrucción, en representación o híbrida) y evidenciando la
creciente sofisticación de arquitecturas basadas en redes recurrentes, convolucionales y
transformadores.

De manera relevante para esta investigación, Choi, Yi, Park y Yoon (2021)[@choi2021deep] y
Blázquez-García et al. (2021)[@blazquez2021review] advierten que, si bien los métodos de
aprendizaje profundo alcanzan desempeños sobresalientes en determinados benchmarks, su superioridad
no es universal: estudios comparativos recientes, como el desarrollado en el marco del reto HUMS
2023 sobre señales de vibración de componentes mecánicos, han mostrado que técnicas clásicas de
procesamiento de señales pueden superar a algoritmos de aprendizaje profundo quando los datos de
entrenamiento disponibles son limitados, lo que subraya la importancia de no descartar los métodos
clásicos y de evaluar de manera contextual la técnica más adecuada según las características del
conjunto de datos.

## Hacia enfoques híbridos e integrados

Kumari et al. (2024)[@kumari2024comprehensive], en su investigación comprehensiva sobre métodos de
detección de anomalías entre 2019 y 2023, señalan que la integración de distintas técnicas
—estadísticas, de aprendizaje automático y de aprendizaje profundo— dentro de un mismo sistema
puede potenciar las fortalezas particulares de cada enfoque y mitigar sus debilidades individuales,
dando lugar a sistemas híbridos más robustos frente a la heterogeneidad de los datos y a los
distintos tipos de anomalías (puntuales, contextuales y colectivas). Esta perspectiva de
integración constituye uno de los fundamentos conceptuales centrales del framework propuesto en la
presente tesis.

## Arquitecturas de despliegue: de los algoritmos a los sistemas

Mientras la investigación algorítmica ha avanzado sustancialmente, la literatura sobre la
operacionalización de estos modelos en arquitecturas de software escalables es comparativamente más
limitada dentro del campo específico de la detección de anomalías. Las prácticas de MLOps y las
arquitecturas de microservicios en la nube —ampliamente documentadas en la literatura de ingeniería
de software e ingeniería de datos— permiten desacoplar los componentes de ingesta,
preprocesamiento, entrenamiento, inferencia y visualización, facilitando el escalamiento
independiente de cada componente, la actualización incremental de los modelos y la integración con
fuentes de datos empresariales. La presente investigación retoma estos principios arquitectónicos y
los aplica específicamente al dominio de la detección de datos atípicos, un aspecto todavía poco
sistematizado en la literatura revisada.

## Síntesis y posicionamiento de la investigación

La tabla 1 sintetiza los principales enfoques identificados en la revisión de literatura, sus
métodos representativos, fortalezas y limitaciones, y sirve como base para la selección de las
técnicas que integrará el framework propuesto.

<a id="tbl-sintesis-comparativa"></a>

|                           Enfoque                            |                                              Métodos representativos                                              |                                                           Fortalezas                                                           |                                                      Limitaciones                                                       |
| :----------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |
|       Estadístico clásico (univariante/multivariante)        | Z-score, rango intercuartílico (IQR), prueba de Grubbs, distancia de Mahalanobis, control estadístico de procesos |        Alta interpretabilidad; bajo costo computacional; fundamentos teóricos sólidos; útil para variables individuales        | Supone distribuciones conocidas (a menudo normalidad); pierde eficacia en alta dimensionalidad y relaciones no lineales |
|                Basado en distancia y densidad                |                         Local Outlier Factor (LOF), k-vecinos más cercanos (kNN), DBSCAN                          |                         No requiere supuestos distribucionales; captura anomalías locales/contextuales                         |           Sensible a la elección de parámetros (k, epsilon); costo computacional elevado en grandes volúmenes           |
|               Basado en árboles y ensamblados                |                     Isolation Forest, Extended Isolation Forest, Random Forest para detección                     |                 Buen desempeño en alta dimensionalidad; eficiente computacionalmente; requiere pocos supuestos                 |           Menor interpretabilidad directa; desempeño variable ante anomalías agrupadas (clustered anomalies)            |
| Basado en distribución empírica y estadística no paramétrica |                                                 ECOD, COPOD, HBOS                                                 |                  Sin hiperparámetros complejos; rápidos y escalables; buen desempeño en benchmarks recientes                   |                             Pueden subestimar dependencias entre variables correlacionadas                              |
|                     Aprendizaje profundo                     |      Autoencoders, Variational Autoencoders, GAN-based, modelos basados en Transformers, modelos de difusión      | Capturan patrones altamente no lineales y temporales; adecuados para datos de alta dimensionalidad e imágenes/series de tiempo |             Requieren grandes volúmenes de datos y cómputo; menor interpretabilidad; riesgo de sobreajuste              |

_Tabla 1: Síntesis comparativa de enfoques de detección de datos atípicos._

A partir de esta revisión, se identifica una oportunidad clara de investigación: el diseño,
implementación y evaluación de un framework que combine deliberadamente métodos estadísticos
clásicos (para variables con comportamiento aproximadamente conocido y como capa de detección
rápida y explicable) con métodos de aprendizaje automático (Isolation Forest, LOF, métodos basados
en distribución empírica) y, de forma complementaria, técnicas de aprendizaje profundo para
escenarios de alta dimensionalidad o datos secuenciales, todo ello desplegado sobre una
arquitectura de microservicios en la nube y comunicado mediante un dashboard de visualización
orientado a usuarios de negocio.

## Referencias

\bibliography

<!-- Las referencias a la [Tabla 1](#tbl-sintesis-comparativa) funcionarán como hipervínculos internos tanto en la página web generada por MkDocs como en el PDF generado por Pandoc. -->
