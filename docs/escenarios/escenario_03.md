---
title: Escenario 3
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

# Escenario 3

## Datos

<!-- prettier-ignore -->
| Dataset | Estructura de datos | Complejidad temporal | Potencial de anomalías | Encaje con modelos avanzados | Justificación |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Generación Real por Planta | Multivariado natural: N plantas × T horas × tipo de combustible (matriz de alta dimensión). Cada planta es una serie temporal con dinámica propia, y las correlaciones entre plantas capturan relaciones espaciales (congestión, despacho). | Alta: estacionalidad horaria, semanal y anual, más efectos de mantenimiento, hidrología y precio. Series no estacionarias con regímenes operativos cambiantes. | Muy alto: caídas súbitas de generación, desviaciones entre generación programada y real, fallas de equipos, indisponibilidades no reportadas. Anomalías que se propagan entre plantas por restricciones de red. | Excelente. LSTM multivariado, autoencoders (AE) sobre matrices planta×hora, transformers para capturar dependencias entre plantas, graph neural networks (GNN) para relaciones topológicas. La estructura N×T permite reconstrucción multivariada con error de reconstrucción como señal de anomalía. | Es el dataset con mayor dimensionalidad y riqueza estructural del SIMEM. Permite formular el problema como detección de anomalías en series multivariadas con dependencias cruzadas, que es exactamente el escenario donde los modelos profundos superan a los métodos univariados. Además, hay precedentes metodológicos directos en plantas hidroeléctricas colombianas. |

### 1. ¿Cuál es el problema?

<!-- prettier-ignore -->
<!-- El problema general de investigación radica en la incapacidad de las técnicas convencionales de
análisis de datos para detectar con precisión observaciones atípicas (anomalías) en series
temporales tabulares de alta dimensión, debido a su limitación para capturar dependencias no
lineales y multivariadas complejas sin incurrir en altas tasas de falsos positivos o en la omisión
de fallas críticas. Al contextualizar este desafío en el conjunto de datos de "Generación Real por
Planta" del SIMEM, el problema específico se manifiesta en la dificultad para identificar anomalías
operacionales (tales como caídas súbitas de generación, indisponibilidades no reportadas o
desviaciones en el despacho) inmersas en una matriz multivariada de alta dimensión ($N \text{
plantas} \times T \text{ horas} \times \text{tipo de combustible}$). En este entorno, las anomalías
raramente ocurren como desviaciones aisladas en una sola planta, sino como alteraciones sutiles en
las correlaciones temporales y espaciales cruzadas entre múltiples unidades interconectadas. Los
enfoques actuales fallan al evaluar las variables de manera independiente o aislada, lo que impide
detectar anomalías estructurales que se propagan por las restricciones de la red eléctrica y
distorsionan la confiabilidad de la información operativa del mercado. -->

<!-- prettier-ignore -->
<!-- El problema central radica en la incapacidad de los sistemas de monitoreo actuales para identificar
desviaciones operacionales sutiles y acopladas en la generación eléctrica, lo que compromete la
eficiencia económica y la confiabilidad del Mercado de Energía Mayorista. Abordar el conjunto de
datos de "Generación Real por Planta" del SIMEM (Sistema de Información del Mercado de Energía
Mayorista) presenta desafíos críticos por las siguientes razones:Impacto Económico y Operativo: Las
anomalías operacionales, como caídas súbitas de generación, indisponibilidades no reportadas a
tiempo o desviaciones del despacho programado, rara vez son eventos aislados. Cuando una planta
falla en entregar su energía, el sistema interconectado (gestionado por XM) debe compensar esta
deficiencia en tiempo real alterando el despacho económico, activando reservas o alterando los
flujos de potencia. Esto se traduce directamente en sobrecostos operativos, ineficiencias en la
formación de precios del mercado y riesgos para la estabilidad de la red.La Barrera Técnica (Por
qué los métodos actuales fallan): Los datos poseen una estructura de alta dimensión ($N\text{
plantas}\times T \text{horas} \times \text{tipo de combustible}$). Las técnicas convencionales
(análisis univariado, umbrales estáticos o reglas de negocio independientes por planta) fracasan
porque ignoran la naturaleza interconectada del sistema eléctrico. Una desviación en una unidad
provoca alteraciones en las demás debido a las leyes físicas (flujos de potencia) y a las reglas
del mercado (mérito económico y regulación de frecuencia).Fatiga de Alarmas y Puntos Ciegos: Al
evaluar cada serie temporal de forma independiente, los enfoques tradicionales generan altas tasas
de falsos positivos frente a dinámicas normales del sistema (como rampas de subida o cambios de
despacho generalizados), y simultáneamente presentan "puntos ciegos" ante fallas sistémicas
complejas que solo son evidentes al analizar la correlación espacio-temporal conjunta de las
plantas. En síntesis, el problema es la falta de modelos analíticos capaces de capturar las
dependencias no lineales y topológicas (físicas y de mercado) entre las plantas generadoras, lo que
impide una detección temprana, precisa y contextual de las anomalías operacionales en el sistema
colombiano. -->

<!-- prettier-ignore -->
<!--El Sistema Interconectado Nacional (SIN) y el Mercado de Energía Mayorista de Colombia (MEM),
operados y administrados por XM, conforman una infraestructura crítica donde la confiabilidad
operativa y la eficiencia económica están estrechamente acopladas. En este entorno, las anomalías
operacionales en el parque generador —tales como caídas súbitas de generación, indisponibilidades
no reportadas a tiempo o desviaciones sistemáticas respecto al despacho programado— rara vez
constituyen eventos aislados. Debido a las leyes físicas que rigen los flujos de potencia y a las
reglas de mérito económico del despacho, la falla o alteración en una unidad generadora obliga al
sistema a compensar la deficiencia en tiempo real, propagando el impacto hacia otras plantas
interconectadas [@xm2023informe]. -->

<!-- prettier-ignore -->
<!--A pesar del riesgo sistémico que representan estas anomalías, los sistemas de monitoreo
tradicionales y los enfoques analíticos convencionales enfrentan una severa limitación técnica:
evalúan las series temporales de generación de forma independiente o mediante umbrales estáticos
univariados. Esta aproximación resulta inadecuada para el conjunto de datos de "Generación Real por
Planta" del Sistema de Información del Mercado de Energía Mayorista (SIMEM), el cual posee una alta
dimensionalidad ($N\:\text{plantas}\:\times\:\text{horas}\:\times\text{tipo de combustible}$). Al
ignorar las dependencias topológicas, físicas y de mercado, los métodos tradicionales generan altas
tasas de falsos positivos frente a dinámicas sistémicas normales (como rampas de generación o
reconfiguraciones de red) y, paradójicamente, presentan "puntos ciegos" ante fallas incipientes que
solo son detectables al analizar la correlación espacio-temporal conjunta [@audibert2020usad]. -->

<!-- prettier-ignore -->
<!--En el ámbito de la investigación local, existe una brecha metodológica significativa. Mientras que
la literatura enfocada en el mercado eléctrico colombiano ha explotado exhaustivamente los datos
del SIMEM para el pronóstico del precio de bolsa y la demanda, el problema de la detección de
anomalías operacionales ha sido relegado a procesos de limpieza de datos mediante métodos
estadísticos básicos (Z-score, rangos intercuartílicos). No existen marcos metodológicos
consolidados en el contexto colombiano que implementen arquitecturas de aprendizaje profundo
diseñadas explícitamente para el modelado de dependencias en grafos dinámicos o la reconstrucción
de subespacios no lineales, enfoques que han demostrado superioridad en la reducción de falsos
positivos en infraestructuras críticas complejas [@deng2021graph]. -->

<!-- prettier-ignore -->
<!--En consecuencia, el problema fundamental radica en la ausencia de modelos analíticos multivariados
y "conscientes del mercado" (Market-Aware) capaces de capturar las dependencias no lineales y
estructurales entre las múltiples plantas del parque generador colombiano. Esta carencia impide la
detección temprana, precisa y contextual de anomalías operacionales, limitando la capacidad de
anticipar eventos que comprometen la seguridad del suministro y la formación eficiente de precios
en el mercado. -->

El Sistema Interconectado Nacional (SIN) y el Mercado de Energía Mayorista de Colombia (MEM),
operados y administrados por XM, conforman una infraestructura crítica donde la confiabilidad
operativa y la eficiencia económica están estrechamente acopladas. En este entorno, las anomalías
operacionales en el parque generador —tales como caídas súbitas de generación, indisponibilidades
no reportadas a tiempo o desviaciones sistemáticas respecto al despacho programado— rara vez
constituyen eventos aislados. Debido a las leyes físicas que rigen los flujos de potencia y a las
reglas de mérito económico del despacho, la falla o alteración en una unidad generadora obliga al
sistema a compensar la deficiencia en tiempo real, propagando el impacto hacia otras plantas
interconectadas. Esta vulnerabilidad ante la simultaneidad de eventos e indisponibilidades ha sido
documentada en los balances de confiabilidad y desempeño operativo del sistema [@xm2023informe].

A pesar del riesgo sistémico que representan estas anomalías, los sistemas de monitoreo
tradicionales y los enfoques analíticos convencionales enfrentan una severa limitación técnica:
evalúan las series temporales de generación de forma independiente o mediante umbrales estáticos
univariados. Esta aproximación resulta inadecuada para el conjunto de datos de "Generación Real por
Planta" del Sistema de Información del Mercado de Energía Mayorista (SIMEM), el cual posee una alta
dimensionalidad ($N$ plantas $\times$ $T$ horas $\times$ tipo de combustible). Al ignorar las
dependencias topológicas, físicas y de mercado, los métodos tradicionales generan altas tasas de
falsos positivos frente a dinámicas sistémicas normales (como rampas de generación o
reconfiguraciones de red) y, paradójicamente, presentan "puntos ciegos" ante fallas incipientes que
solo son detectables al analizar la correlación espacio-temporal conjunta [@audibert2020usad].

En el ámbito de la investigación local, existe una brecha metodológica significativa. La literatura
académica e industrial enfocada en el mercado eléctrico colombiano ha explotado exhaustivamente los
datos del SIMEM, pero con un enfoque predominantemente predictivo. Estudios recientes se han
concentrado en el desarrollo de modelos para el pronóstico del precio de bolsa y la estimación de
la demanda mediante redes neuronales y modelos econométricos (ARIMA, LSTM), relegando la detección
de anomalías a procesos de limpieza estadística previa [lopez2021precio].

Aunque han surgido estudios en la literatura económica nacional orientados a la identificación de
anomalías operacionales y el poder de mercado en el sector eléctrico colombiano mediante Machine
Learning —como los desarrollados en la serie de Borradores de Economía del Banco de la República
[riascos2022deteccion]— estas importantes iniciativas aún no consolidan arquitecturas
que integren explícitamente las dependencias en grafos dinámicos o la reconstrucción de subespacios
no lineales, enfoques que han demostrado superioridad en la reducción de falsos positivos en
infraestructuras críticas complejas [@deng2021graph].

En consecuencia, el problema fundamental radica en la ausencia de modelos analíticos multivariados
y "conscientes del mercado" (Market-Aware) capaces de capturar las dependencias no lineales y
estructurales entre las múltiples plantas del parque generador colombiano. Esta carencia impide la
detección temprana, precisa y contextual de anomalías operacionales, limitando la capacidad de
anticipar eventos que comprometen la seguridad del suministro y la formación eficiente de precios
en el mercado.

### 2. ¿Por qué es importante?

La calidad de los datos es fundamental, pues de ella depende la validez de los análisis analíticos
que apoyan la toma de decisiones, pudiendo verse afectada por errores de medición, fallas de
sistemas o eventos excepcionales genuinos. En el contexto del dataset de "Generación Real por
Planta", abordar este problema es de suma importancia porque el potencial de anomalías es muy alto:
se presentan caídas súbitas de generación, desviaciones entre la generación programada y la real,
fallas de equipos e indisponibilidades no reportadas que terminan propagándose entre las distintas
plantas debido a las restricciones de la red eléctrica.

### 3. ¿Por qué no ha sido suficiente?

Metodológicamente, los métodos estadísticos univariados (como el rango intercuartílico o la
puntuación z robusta) identifican desviaciones variable por variable, pero no necesariamente logran
detectar las observaciones anómalas que se definen por relaciones conjuntas entre múltiples
variables. Esto resulta insuficiente para la "Generación Real por Planta", dado que su complejidad
temporal es alta (estacionalidad horaria, semanal, anual y cambios por mantenimiento, hidrología o
precio) y produce series no estacionarias con regímenes operativos cambiantes. Las dependencias
espaciales cruzadas hacen que un simple enfoque univariado o aislado ignore la riqueza estructural
del comportamiento del sistema interconectado.

Adicionalmente, la presencia no tratada de outliers u observaciones anómalas en este tipo de series
temporales genera impactos severos que justifican la insuficiencia de los enfoques convencionales:

- **Incremento del Ruido (_Noise_):** Los outliers operacionales y errores de telemetría aumentan
  el ruido en la matriz N × T, lo que dificulta la detección de patrones reales y la extracción de
  insights operativos valiosos.
- **Inducción de Deriva de Datos (_Data Drift_):** Los outliers no aislados influyen sobre el
  patrón general de la serie de tiempo, provocando una deriva en la distribución que disminuye
  drásticamente la precisión de los modelos predictivos y su capacidad de generalización.
- **Generación de Sesgos (_Biases_):** La presencia de datos atípicos introduce sesgos sistemáticos
  en las métricas de la serie temporal, afectando la estimación del comportamiento regular de la
  red.
- **Fuga de Información (_Data Leakage_):** Los outliers contienen información extrema o no
  representativa que, si se utiliza de manera inadecuada durante el preprocesamiento o
  entrenamiento, lleva a la sobreestimación o subestimación de las predicciones y del error de
  reconstrucción.
- **Condicionamiento en la Selección de Modelos:** La vulnerabilidad de los algoritmos ante la
  presencia de outliers condiciona críticamente la selección de los modelos para los pronósticos y
  la detección, descartando esquemas lineales o univariados simples.

### 4. ¿Cuál es la propuesta?

La propuesta investigativa es diseñar, implementar y evaluar un marco de trabajo híbrido para la
detección de anomalías que combine métodos estadísticos clásicos, métodos de aprendizaje automático
(como Isolation Forest y Local Outlier Factor) y un autocodificador (autoencoder) de aprendizaje
profundo, operado en una arquitectura de microservicios en la nube con un tablero interactivo.

Dado que la presencia de outliers condiciona severamente la selección de los modelos, la estructura
multivariada N × T permite emplear autoencoders (AE) sobre las matrices de planta × hora, así como
LSTMs multivariados, transformers o Graph Neural Networks (GNN). Estas arquitecturas avanzadas
permiten realizar una reconstrucción donde el error de reconstrucción funja directamente como señal
de anomalía multivariada, blindando al sistema frente al ruido, neutralizando el _data drift_ y
evitando que los sesgos o la fuga de datos distorsionen el diagnóstico operativo.

### 5. ¿Qué se espera encontrar?

Se espera que el esquema híbrido propuesto logre un desempeño de detección (medido en F1, precisión
y exhaustividad) superior al de los métodos individuales aislados, reduciendo la tasa de falsos
positivos sin incrementar significativamente los falsos negativos. Específicamente, al integrar la
idea del dataset del SIMEM, se espera corroborar empíricamente que, debido a la inmensa
dimensionalidad y las dependencias cruzadas de la matriz N×T, el componente de modelos profundos
supere con creces a los métodos univariados tradicionales, mitigando activamente los efectos de
_data drift_, sesgos, ruido y _data leakage_. Así mismo, se espera que el tablero de visualización
mejore notablemente el tiempo de interpretación y la comprensión de estos resultados complejos por
parte de los usuarios no especialistas.

## Referencias

\bibliography
