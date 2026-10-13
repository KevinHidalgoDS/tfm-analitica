---
title: Metodología
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

# Metodología

Esta investigación adopta un enfoque metodológico de tipo aplicado y cuantitativo, con un diseño
experimental que combina el desarrollo de un artefacto de software (el marco de trabajo de
detección y una API local para su ejecución) con la evaluación empírica y comparativa de su
desempeño. Dada su modalidad de profundización, el trabajo enfatiza la construcción de una solución
funcional, documentada y evaluada bajo condiciones controladas, más que la generación de un aporte
puramente teórico.

El desarrollo se organiza en cinco fases secuenciales, aunque con iteraciones internas propias de
un ciclo de desarrollo ágil: (1) revisión y selección de métodos, (2) diseño del marco de trabajo
de detección, (3) implementación de una API local para ejecutar el análisis y exponer resultados,
(4) construcción del tablero de visualización, y (5) evaluación integral del sistema.

## Marco de trabajo propuesto para la clasificación de anomalías

El marco de trabajo de clasificación de anomalías se concibe como un esquema de comparación y
posible ensamblado de métodos estadísticos, de aprendizaje automático y de aprendizaje profundo
para conjuntos de datos tabulares procesados por lotes. La evaluación considerará como métodos
estadísticos la puntuación z robusta basada en la mediana y la desviación absoluta mediana, el
rango intercuartílico y, cuando la estructura de los datos lo permita, la distancia de Mahalanobis
multivariante.

Como métodos de aprendizaje automático se evaluarán Isolation Forest y Local Outlier Factor.
También se implementará un autocodificador de arquitectura densa para la representación tabular,
cuya puntuación de atipicidad se calculará a partir del error de reconstrucción
[@sakurada2014autoencoders; @pang2021deep].

Se entrenará sin utilizar las etiquetas de observaciones atípicas; las etiquetas de validación
podrán apoyar la selección de configuraciones y umbrales, y las de prueba se reservarán para la
evaluación final. La arquitectura, la función de pérdida compatible con la representación de
entrada y los hiperparámetros se definirán y documentarán usando únicamente los datos de
entrenamiento y validación. Cada método producirá una puntuación continua de anomalía; la
clasificación binaria se obtendrá al aplicar un umbral definido con los datos de validación.

La combinación se realizará mediante la agregación ponderada de puntuaciones de anomalía
normalizadas. Las ponderaciones, la regla de normalización y el umbral de decisión se seleccionarán
exclusivamente con los datos de entrenamiento y validación; no se contempla un metamodelo
supervisado. La estrategia se evaluará frente a cada detector individual y frente al mejor detector
individual seleccionado mediante la medida F1 en validación. Para presentar los resultados, se
expondrán las puntuaciones de detección y las variables asociadas según la información que
proporcione cada método; no se presupone que todas las técnicas ofrezcan explicaciones
equivalentes.

Para asignar niveles de alerta, cada detector aplicable emitirá como máximo un voto binario por
observación. Los dos detectores unidimensionales (1D) serán la puntuación z robusta, que señalará
valores con $|z_{\mathrm{robusto}}| > 3$, y el rango intercuartílico (IQR), que aplicará las vallas
de Tukey $x < Q_1 - 1{,}5\,\mathrm{IQR}$ o $x > Q_3 + 1{,}5\,\mathrm{IQR}$. Si un detector 1D
señala una o más variables de una observación, emitirá un único voto positivo para ella. Los
detectores multidimensionales (MD) serán Mahalanobis cuando sea aplicable, Isolation Forest, Local
Outlier Factor y el autocodificador denso; cada uno emitirá un voto según su umbral, seleccionado
exclusivamente con los datos de entrenamiento y validación. Un detector no aplicable a un conjunto
de datos no se contará como voto.

Sean $k_{1D}$ y $k_{MD}$ los números de votos positivos de los detectores 1D y MD, respectivamente,
y $k = k_{1D} + k_{MD}$. Si $k = 0$, la observación no recibirá nivel de alerta; si $1 \leq k \leq
2$, recibirá el nivel **Warning**; y si $k \geq 3$, recibirá el nivel **Red Flag**. En particular,
un voto 1D y uno MD producen **Warning**, mientras que un voto 1D y dos MD producen **Red Flag**.
El puntaje ponderado normalizado se conservará para ordenar o comparar observaciones; la asignación
de niveles se basará en los votos y no autorizará por sí misma la imputación ni otra modificación
de los datos.

## Carga y procesamiento del conjunto de datos

Para la fase de evaluación se emplearán conjuntos de datos de referencia utilizados en la
literatura sobre detección de observaciones atípicas (por ejemplo, conjuntos disponibles en el
repositorio ODDS, sigla de _Outlier Detection DataSets_, y en repositorios públicos de datos
tabulares etiquetados), seleccionados por permitir el cálculo de métricas de desempeño. Se
incorporará también, cuando sea posible, un conjunto de datos real o semisintético representativo
de un dominio de aplicación (por ejemplo, transacciones financieras o variables de un proceso
productivo), con el fin de valorar la aplicabilidad práctica del marco de trabajo.

El proceso de carga y preprocesamiento se ejecutará localmente como parte del flujo de análisis y
será responsable de: (i) la validación de esquema y tipos de datos; (ii) el tratamiento de valores
faltantes mediante estrategias documentadas (imputación o exclusión, según el porcentaje de datos
ausentes); (iii) la normalización o estandarización de variables numéricas; (iv) la codificación de
variables categóricas cuando aplique; y (v) la partición de los datos en conjuntos de
entrenamiento, validación y prueba, preservando la proporción de observaciones atípicas mediante
muestreo estratificado.

Los parámetros de imputación, escalado y codificación se ajustarán con el conjunto de entrenamiento
y se aplicarán sin reajuste a validación y prueba. Las etiquetas de observaciones atípicas no se
utilizarán para entrenar el autocodificador; se reservarán para seleccionar configuraciones o
umbrales con validación y para la evaluación final en prueba. Los datos procesados se almacenarán
en un formato columnar (Parquet) para facilitar su procesamiento reproducible.

Los conjuntos de datos reales se seleccionarán según los siguientes criterios: disponibilidad de
etiquetas de anomalía, documentación del proceso de generación de los datos, proporción de la clase
anómala, número y tipo de variables, ausencia de duplicados entre particiones y pertinencia para
datos tabulares procesados por lotes. Los datos sintéticos se utilizarán únicamente para controlar
factores que no estén suficientemente representados en los datos reales. Se generarán mediante
contaminación controlada de observaciones habituales, especificando el mecanismo de generación, la
proporción de anomalías, el nivel de contaminación, la distribución de las variables y la semilla
aleatoria. Las etiquetas sintéticas serán conocidas por construcción y no se utilizarán para
ajustar los modelos; solo se emplearán en validación y prueba conforme al protocolo establecido. La
similitud entre anomalías sintéticas y fenómenos plausibles se justificará para cada escenario, y
los resultados sintéticos se presentarán separados de los resultados reales o semisintéticos.

Para prevenir fuga de información, ninguna observación de prueba participará en el ajuste de
imputadores, transformadores, hiperparámetros, ponderaciones, umbrales o selección de variables.
Las transformaciones se ajustarán en entrenamiento y se aplicarán sin reajuste en validación y
prueba. Se comprobará además que no existan duplicados, identificadores compartidos o información
derivada de la etiqueta entre las particiones.

## Protocolo de reproducibilidad y control de sesgos

Cada ejecución registrará la semilla aleatoria, las versiones de código y dependencias, el entorno
de ejecución local, los parámetros de preprocesamiento, los hiperparámetros, el umbral de decisión,
las ponderaciones del ensamblado y el identificador de los datos utilizados. Los métodos
estocásticos se ejecutarán con un número predefinido de repeticiones y las particiones se generarán
mediante un procedimiento reproducible. La selección de hiperparámetros se realizará exclusivamente
con entrenamiento y validación, mediante validación cruzada dentro del conjunto de entrenamiento
cuando el tamaño de los datos lo permita; la prueba se mantendrá intacta hasta el análisis final.

Se informarán los valores faltantes, las reglas de imputación o exclusión, la normalización y la
codificación categórica para cada conjunto. Los resultados se reportarán con intervalos de
confianza obtenidos mediante remuestreo cuando sea apropiado, junto con tamaños de efecto y el
número de repeticiones. El repositorio incluirá archivos de configuración, semillas, esquemas de
datos, especificaciones de API, versiones de modelos y scripts necesarios para reproducir cada
experimento. Las decisiones metodológicas se fijarán antes de consultar las etiquetas de prueba
para reducir el riesgo de sobreajuste del protocolo a los resultados observados.

## API local para la ejecución del análisis

La API local permitirá cargar conjuntos de datos tabulares, ejecutar el flujo de validación,
preprocesamiento, detección y ensamblado, y consultar los resultados para su visualización. El
flujo se ejecutará en el entorno local de forma reproducible. La API expondrá los resultados al
tablero y registrará un identificador por ejecución junto con la configuración y los parámetros
utilizados para facilitar la trazabilidad y reproducción del análisis.

## Tablero de visualización de resultados

El tablero interactivo constituye la interfaz principal mediante la cual los usuarios consultarán
los resultados del marco de trabajo. Se propone que incluya, como mínimo, los siguientes
componentes: (i) un resumen de la distribución de los datos analizados, con las observaciones
señaladas como atípicas resaltadas; (ii) las puntuaciones de atipicidad asociadas a cada
observación; (iii) un desglose por variable cuando el método proporcione información que permita
asociarla con la detección; y (iv) métricas agregadas, como el número de observaciones señaladas y
los tiempos de procesamiento. Para cada observación mostrará el nivel **Warning** o **Red Flag**
asignado por la regla de votos, como orientación para su revisión y sin recomendar una imputación
automática. El prototipo se desarrollará con Plotly Dash o Streamlit y consumirá los datos
expuestos por la API local.

## Herramientas y tecnologías

La tabla 2 resume las principales herramientas y tecnologías consideradas para cada componente de
la solución. La selección definitiva podrá ajustarse durante el desarrollo del trabajo en función
de la disponibilidad de recursos y de los resultados de las pruebas técnicas preliminares, sin que
ello afecte la validez del diseño metodológico general.

<a id="tbl-herramientas"></a>
<!-- prettier-ignore -->
| Componente | Herramientas / tecnologías propuestas | Función principal |
|:---:|:---:|:---:|
| Lenguaje y librerías   analíticas | Python 3.x; pandas, NumPy, SciPy, scikit-learn, PyOD (Python Outlier   Detection), statsmodels, PyTorch o TensorFlow | Implementación de los   métodos estadísticos, de aprendizaje automático y del autocodificador |
| API local | FastAPI (Python), con documentación OpenAPI | Ejecución local del análisis por lotes y exposición de resultados al tablero |
| Persistencia de resultados | Archivos Parquet y formatos tabulares según las necesidades del experimento | Conservación reproducible de los datos procesados y resultados de detección |
| Visualización | Plotly Dash o Streamlit para el prototipo del tablero interactivo | Presentación interactiva de los resultados de detección de observaciones atípicas |

_Tabla 2: Herramientas y tecnologías propuestas por componente._

## Diseño de la evaluación experimental

La evaluación de HE2 seguirá un diseño factorial en el que los factores serán el método de
detección, el tipo de observación atípica y la dimensionalidad. Los métodos incluidos serán la
puntuación z robusta, el rango intercuartílico, la distancia de Mahalanobis cuando sea aplicable,
Isolation Forest, Local Outlier Factor y el autocodificador denso. Los tipos de anomalía se
clasificarán como puntual, contextual o colectiva únicamente cuando esa estructura esté presente y
etiquetada en el conjunto correspondiente. La dimensionalidad se definirá por el número de
variables predictoras: baja (hasta 10), media (11--50) y alta (más de 50).

La dimensionalidad se variará mediante conjuntos de datos pertenecientes a esos rangos o mediante
selección de variables documentada dentro del entrenamiento; no se utilizará la reducción de
dimensionalidad para crear artificialmente una categoría. Se analizarán los efectos principales y
la interacción entre los tres factores sobre la medida F1, con precisión, exhaustividad y AUC-PR
como medidas secundarias.

La evaluación del marco de trabajo se realizará mediante un diseño experimental comparativo en el
que se contrastará el desempeño del esquema de ensamblado propuesto frente a: (a) cada método
estadístico aplicado de forma aislada; (b) cada algoritmo de aprendizaje automático aplicado de
forma aislada; y (c) el autocodificador. También se comparará, para cada conjunto de datos y
escenario, con el mejor método individual seleccionado exclusivamente mediante la medida F1
obtenida en el conjunto de validación.

Todas las comparaciones se realizarán sobre los mismos conjuntos de datos y bajo las mismas
particiones de entrenamiento, validación y prueba; el conjunto de prueba no se utilizará para
seleccionar el método de referencia. El autocodificador se entrenará sin etiquetas de observaciones
atípicas; las etiquetas de validación podrán utilizarse para seleccionar configuraciones y
umbrales, mientras que las etiquetas de prueba se reservarán para la evaluación final. Las métricas
de desempeño incluirán precisión, exhaustividad, medida F1, área bajo la curva ROC (AUC-ROC) y área
bajo la curva de precisión-exhaustividad (AUC-PR), esta última especialmente relevante dado el
desbalance característico entre observaciones habituales y atípicas.

Las diferencias de desempeño entre métodos se contrastarán mediante pruebas estadísticas no
paramétricas (por ejemplo, la prueba de Friedman con post-hoc de Nemenyi) adecuadas para la
comparación de múltiples algoritmos sobre múltiples conjuntos de datos. Para HE1, se evaluará la
reducción de la tasa de falsos positivos frente a cada referencia y la no inferioridad de la tasa
de falsos negativos con un margen $\delta = 0{,}05$, fijado antes de la evaluación.

La evaluación del tablero incorporará un diseño entre sujetos con dos condiciones: tablero con
puntuaciones y variables explicativas, y lista de observaciones detectadas sin dicho componente. La
población objetivo estará compuesta por usuarios no especializados en estadística, con experiencia
básica en análisis de datos; se seleccionará una muestra intencional cuyo tamaño y criterios de
inclusión se documentarán antes de la prueba. Las tareas incluirán identificar observaciones
señaladas, seleccionar la variable asociada más influyente e interpretar la puntuación de
atipicidad. Se registrarán la proporción de respuestas correctas, los errores, el tiempo de
respuesta y la confianza o comprensión percibida mediante una escala definida previamente.

Se asignarán los participantes a una sola condición para evitar efectos de aprendizaje y
contaminación entre interfaces. También se aplicará el cuestionario System Usability Scale (SUS) y
preguntas de utilidad percibida basadas en Davis [@davis1989use]. Estas medidas se analizarán
descriptivamente y mediante una comparación entre condiciones, sin extrapolar los resultados a
poblaciones más amplias. Estas medidas permitirán describir la efectividad, la eficiencia y la
satisfacción de uso en la muestra evaluada [@iso9241-11-2018; @brooke1996sus]. Los resultados se
interpretarán de forma descriptiva y contextualizada, sin extrapolarlos a poblaciones más amplias.
