---
title: Introducción
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

# Introducción

La transformación digital de las organizaciones ha producido un incremento sostenido en el volumen,
la velocidad y la variedad de los datos generados en sectores tan diversos como las finanzas, la
salud, la industria manufacturera, las telecomunicaciones y el comercio electrónico. En este
contexto, la analítica de datos permite transformar información en evidencia para apoyar la toma de
decisiones. La validez de los análisis depende, entre otros factores, de la calidad de los datos
utilizados. Esta puede verse afectada por la presencia de observaciones atípicas, entendidas en
este trabajo como observaciones que se desvían de manera significativa del comportamiento esperado
de un conjunto de datos y que pueden originarse por errores de medición, fraude, fallas de
sistemas, eventos excepcionales genuinos o procesos generadores de datos heterogéneos
[@chandola2009anomaly].

La detección de anomalías, entendida como el proceso de identificar patrones que no se
ajustan a la noción de comportamiento normal dentro de un conjunto de datos, cuenta con
antecedentes en los trabajos de la estadística clásica sobre pruebas de discordancia y detección de
valores extremos, como el procedimiento propuesto por Grubbs [@grubbs1969procedures]. La expansión
en esta tesis se utilizará «anomalía» como término general para referirse a una observación cuyo
comportamiento se desvía del patrón esperado, y «clasificación de anomalías» para la decisión
binaria obtenida al aplicar un umbral a la puntuación continua producida por un método. La expresión
«observación atípica» se conservará cuando se describan las fuentes bibliográficas o las etiquetas
originales de los conjuntos de datos. La expansión
de los macrodatos y el aumento de la dimensionalidad han ampliado los desafíos de esta tarea, pues
exigen considerar tanto las propiedades de los datos como la capacidad de los métodos para
identificar distintos tipos de comportamiento atípico [@chandola2009anomaly; @aggarwal2017outlier].
Entre los métodos estadísticos se encuentran reglas univariadas basadas en medidas robustas,
como el rango intercuartílico, que identifica valores alejados de los cuartiles sin requerir el
supuesto de normalidad [@aggarwal2017outlier]. La prueba de Grubbs, en cambio, contrasta valores
extremos bajo dicho supuesto [@grubbs1969procedures]. Por tanto, estos procedimientos difieren en
sus fundamentos y condiciones de aplicación. Los métodos univariados pueden ofrecer resultados
directos cuando la atipicidad se manifiesta en variables individuales, pero no necesariamente
detectan observaciones definidas por relaciones entre variables. En general, la validez de cada
procedimiento depende de que sus supuestos sean razonables para los datos analizados. Los métodos
de aprendizaje automático y profundo ofrecen alternativas para otras estructuras, aunque su
selección también depende de los requisitos analíticos.

Entre estos métodos, Isolation Forest separa observaciones mediante particiones aleatorias;
la máquina de vectores de soporte de una clase (One-Class Support Vector Machine, denominada
One-Class SVM) estima una frontera que delimita la región de los datos considerados habituales; y el
factor local de observaciones atípicas (Local Outlier Factor, LOF) asigna puntuaciones elevadas a
observaciones cuya densidad local es menor que la de sus vecinas 
[@liu2008isolation; @scholkopf2001estimating; @breunig2000lof]. Los autocodificadores
(*autoencoders*), una técnica de aprendizaje profundo, aprenden a reconstruir los datos y pueden
señalar observaciones con errores de reconstrucción elevados
[@sakurada2014autoencoders; @pang2021deep], mientras que ECOD es un método no supervisado basado en
funciones de distribución empírica acumulada que estima el grado de atipicidad [@li2022ecod]. En
esta tesis se explorará y evaluará un autocodificador para datos tabulares, comparándolo con métodos
estadísticos y de aprendizaje automático seleccionados. Estos
métodos difieren en sus supuestos, parámetros, requisitos computacionales y capacidades; por ello,
su selección y eventual combinación deberán justificarse y evaluarse en el contexto de los datos
[@aggarwal2017outlier; @pang2021deep]. La solución integrará los métodos seleccionados y expondrá
sus resultados para facilitar su consulta e interpretación.

Para responder a estos requisitos de integración y operación, la computación en la nube y las
arquitecturas de microservicios ofrecen una alternativa para separar componentes de ingesta,
procesamiento, modelado y visualización. Esta separación puede facilitar su mantenimiento y
despliegue independiente, así como la adaptación de los recursos a las necesidades de cada
componente [@newman2021microservices; @kreuzberger2023mlops]. Las revisiones sobre detección de
observaciones atípicas describen las definiciones del problema, las familias de métodos y sus
ámbitos de aplicación [@chandola2009anomaly; @pang2021deep]. Por su parte, los trabajos sobre
operación de sistemas de aprendizaje automático describen retos de mantenimiento, integración y
despliegue en producción [@sculley2015hidden; @kreuzberger2023mlops]. Estos ámbitos ofrecen
perspectivas complementarias para estudiar la integración de métodos de detección en una solución
aplicada y la presentación de resultados mediante un tablero orientado a sus usuarios, siguiendo
principios de comunicación visual de información [@few2006dashboard]. En consecuencia, la
contribución propuesta se centra en integrar los métodos seleccionados y los componentes de
software en una solución evaluable, no en asumir que una arquitectura distribuida mejora por sí
misma la detección. La revisión bibliográfica del estado del arte permitirá precisar el alcance de
esta brecha y situar la contribución del trabajo.

En este marco, la tesis, desarrollada en la modalidad de profundización, aborda la integración de
métodos y componentes de software para la detección de observaciones atípicas en conjuntos de datos
tabulares procesados por lotes, en particular aquellos que los usuarios cargan para su análisis. En
este escenario, el reto no consiste únicamente en identificar observaciones inusuales, sino también
en ofrecer un medio integrado para ejecutar métodos de detección y facilitar la interpretación de
sus resultados. Por tanto, el trabajo no pretende resolver la detección de observaciones atípicas
en flujos de datos en tiempo real ni especializarse en un sector económico particular.

Con ese alcance, la tesis contempla un desarrollo progresivo. En una primera etapa, se implementará
una interfaz de programación de aplicaciones (API, del inglés _application programming interface_)
que integre métodos estadísticos clásicos, métodos de aprendizaje automático y un autocodificador
para detectar observaciones atípicas en los conjuntos de datos tabulares cargados por los usuarios.
En una segunda etapa, se desarrollará una interfaz gráfica con un tablero de visualización que
permita interactuar con la API y examinar e interpretar sus resultados. Finalmente, estos
componentes se integrarán en una solución basada en una arquitectura de microservicios desplegada
en la nube. El marco de trabajo será, por tanto, el resultado de esa integración. La evaluación
contemplará tres dimensiones: el desempeño de los métodos de detección, medido mediante precisión,
exhaustividad, medida F1, área bajo la curva de características operativas del receptor (ROC, del
inglés *Receiver Operating Characteristic*; AUC-ROC) y área bajo la curva de precisión-exhaustividad
(PR, del inglés *Precision-Recall*; AUC-PR)
sobre conjuntos de referencia con observaciones atípicas etiquetadas; el comportamiento operativo
de la solución, considerando tiempos de respuesta y escalabilidad ante distintos volúmenes de
datos; y la utilidad percibida del tablero de visualización, valorada mediante una validación con
usuarios representativos. De este modo, el trabajo no se limita a proponer o comparar algoritmos,
sino que busca articularlos en una solución cuya efectividad analítica, capacidad operativa y
utilidad puedan evaluarse con criterios explícitos, articulando la selección de métodos de
detección con el diseño y la evaluación de una solución de software.
