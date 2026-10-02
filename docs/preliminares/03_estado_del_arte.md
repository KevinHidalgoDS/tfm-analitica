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

## Alcance de la revisión bibliográfica

Este estado del arte se elaboró mediante una búsqueda exploratoria de publicaciones en la web.
No se siguió un protocolo sistemático ni se mantuvo un registro exhaustivo de las plataformas
consultadas, las consultas exactas, las fechas de búsqueda o el proceso de selección. Por tanto,
esta revisión no pretende ser exhaustiva ni permite afirmar que las brechas identificadas sean
universales. Para organizar la síntesis se consideraron fuentes académicas pertinentes a los
métodos estadísticos y de aprendizaje automático para la detección de observaciones atípicas, así
como a la operación de sistemas de aprendizaje automático y al diseño de tableros. Las referencias
se citan según el estilo IEEE configurado para el documento. Los años de publicación de las fuentes
citadas reflejan su cobertura temporal, no un intervalo de búsqueda predefinido.

## Tipos de observaciones atípicas y dimensionalidad

Siguiendo la distinción conceptual de Hawkins [@hawkins1980identification] y la sistematización
de Chandola, Banerjee y Kumar [@chandola2009anomaly], en esta tesis una observación atípica
puntual es una observación individual que se desvía de manera marcada del patrón general de los
datos. Una observación atípica contextual es inusual únicamente bajo un contexto determinado,
definido por variables o condiciones de referencia, aunque pueda parecer normal en el conjunto
global. Una anomalía colectiva corresponde a un conjunto de observaciones que, considerado en
conjunto, presenta un patrón anómalo, aunque sus observaciones individuales no sean necesariamente
atípicas.

Estas categorías se utilizarán solo cuando estén representadas y etiquetadas en los conjuntos de
datos seleccionados. En particular, el formato tabular por lotes no garantiza por sí mismo la
presencia de anomalías contextuales o colectivas; su evaluación requerirá que las variables de
contexto o las relaciones entre observaciones estén disponibles en los datos.

Para el experimento factorial, la dimensionalidad se operacionalizará mediante el número de
variables predictoras: baja dimensionalidad (hasta 10 variables), dimensionalidad media (de 11 a
50) y alta dimensionalidad (más de 50). Estas categorías se construirán mediante la selección de
conjuntos de datos que pertenezcan a cada rango o, cuando un conjunto lo permita, mediante
selección de variables documentada aplicada únicamente dentro de cada partición de entrenamiento.
No se considerará la reducción de dimensionalidad como una categoría de dimensionalidad, sino como
una transformación que deberá mantenerse constante entre métodos dentro de cada escenario.

## Fundamentos estadísticos clásicos para detectar observaciones atípicas

La detección estadística de observaciones atípicas comprende procedimientos con supuestos
distintos, por lo que no conviene tratarla como una sola familia homogénea. El rango intercuartílico
y la puntuación z robusta describen desviaciones por variable mediante cuantiles o medidas robustas
de centro y dispersión [@aggarwal2017outlier]; suelen
resultar útiles como línea base para observaciones atípicas puntuales que se manifiestan en una o
varias variables por separado. No identifican necesariamente una fila inusual solo por la
combinación de
valores que, considerados individualmente, parecen plausibles. La distancia de Mahalanobis aborda
parte de esa limitación al incorporar la covarianza y puede señalar combinaciones multivariantes
atípicas, pero su utilidad depende de que la estimación de covarianza sea adecuada frente a la
dimensionalidad, la colinealidad y la contaminación por observaciones atípicas [@aggarwal2017outlier].

Estos procedimientos pueden ajustarse sin etiquetas de observaciones atípicas, pero requieren una
regla de corte para convertir sus puntuaciones en decisiones binarias; el corte puede basarse en
criterios estadísticos o seleccionarse con un conjunto de validación etiquetado. Grubbs se mantiene
como antecedente metodológico, pero no se incluye en la comparación de esta tesis. En datos
tabulares, el escalado, las distribuciones asimétricas y la decisión de analizar variables por
separado o conjuntamente afectan qué observaciones se señalan. Por ello, el bajo costo y la
interpretabilidad potencial de una regla estadística dependen del procedimiento y de su adecuación
a la representación de los datos; no son ventajas universales.

## Métodos de aprendizaje automático

Los métodos de aprendizaje automático considerados aquí también responden a nociones distintas de
rareza. Local Outlier Factor (LOF) compara la densidad local de una observación con la de sus
vecinas [@breunig2000lof]. Por ello, puede ser pertinente cuando una observación atípica es inusual
respecto
de un subgrupo local, aun si ese subgrupo no es excepcional en la distribución global. En
contrapartida, el significado de «vecino» depende de la métrica, el escalado y el número de vecinos:
un valor inadecuado de estos parámetros puede ocultar observaciones atípicas locales o alterar las
puntuaciones.
En tablas con muchas variables, las distancias pueden volverse menos discriminantes y las
categorías necesitan una codificación compatible con la métrica utilizada. LOF no requiere
etiquetas para estimar densidades, aunque estas sí son necesarias para medir rendimiento y pueden
usarse, sin contaminar la prueba final, al seleccionar parámetros o un umbral.

Isolation Forest, propuesto por Liu et al. [@liu2008isolation], asigna puntuaciones a
partir de la longitud de las particiones aleatorias necesarias para aislar una observación. Su
mecanismo ofrece un contraste con LOF: en lugar de comparar densidades vecinales, busca
observaciones aislables mediante particiones, lo que puede ser útil para rarezas puntuales en
espacios de varias dimensiones. No modela explícitamente la vecindad ni todas las relaciones
dependientes entre variables, y su respuesta puede variar con el submuestreo, el número de
particiones, la representación de variables y el umbral de decisión. Como LOF, su ajuste no
requiere etiquetas, pero las etiquetas de validación permiten seleccionar configuraciones y las
de prueba deben reservarse para la evaluación. ECOD (método no supervisado basado en funciones de
distribución empírica acumulada) estima la atipicidad [@li2022ecod]; se conserva en esta revisión para contextualizar
otros métodos tabulares, pero no se evaluará. La comparación experimental se centrará en LOF e
Isolation Forest porque representan principios locales y de aislamiento distintos, no porque se
presuponga la superioridad de uno sobre otro.

## Aprendizaje profundo y autocodificadores

El aprendizaje profundo amplía el análisis al modelar representaciones no lineales. Sakurada y
Yairi [@sakurada2014autoencoders] estudian autocodificadores para detectar observaciones atípicas
mediante reducción no lineal de dimensionalidad, y Pang et al. [@pang2021deep] revisan distintas
estrategias de aprendizaje profundo. En el autocodificador previsto para esta tesis, el error de
reconstrucción servirá como puntuación: se espera que los patrones representados durante el
entrenamiento se reconstruyan mejor que ciertos patrones atípicos. A diferencia de los métodos
que puntúan directamente distancias o particiones, este enfoque depende de la arquitectura, la
función de pérdida, la regularización y el número de épocas; además, puede reconstruir bien algunas
observaciones atípicas o asignar errores altos a observaciones habituales. Por esa razón, el error
no se interpretará automáticamente como probabilidad de que una observación sea atípica.

El entrenamiento del autocodificador puede realizarse sin etiquetas, pero requiere datos de
entrenamiento representativos del comportamiento que se quiere modelar. Si esos datos contienen
muchas observaciones atípicas, el modelo podría aprender a reconstruirlas; por otra parte, las
etiquetas de validación pueden apoyar la elección de arquitectura, hiperparámetros y umbral,
mientras que las etiquetas de prueba se reservarán para la evaluación final. En datos tabulares, el escalado y la
codificación de variables categóricas, así como la definición de una pérdida compatible con la
representación de entrada, son decisiones relevantes. El autocodificador permite explorar relaciones
no lineales, pero exige más decisiones de entrenamiento y recursos que las reglas estadísticas
sencillas; la magnitud de esa diferencia se medirá en la configuración experimental y no se
presupondrá que sean necesarios grandes volúmenes de datos en todos los casos. En esta tesis se
evaluará un autocodificador de arquitectura densa para datos tabulares procesados por lotes.

Las revisiones de Choi et al. [@choi2021deep] y Blázquez-García et al. [@blazquez2021review]
abarcan ámbitos de datos y tareas más amplios que el de esta tesis. Se
refieren principalmente a series temporales y se consideran antecedentes generales sobre la
diversidad de técnicas y la dependencia del desempeño respecto del problema y de los datos, no
como evidencia directa del rendimiento esperado en datos tabulares.

## Hacia enfoques híbridos e integrados

Kumari et al. [@kumari2024comprehensive], en su revisión de métodos para detectar observaciones
atípicas entre 2019 y 2023, consideran la integración de técnicas estadísticas, de aprendizaje
automático y de aprendizaje profundo. Esta literatura contextualiza las posibles combinaciones entre familias
de métodos, pero no implica que todas deban formar parte de una implementación particular. En esta
tesis se explorará la combinación de métodos estadísticos y de aprendizaje automático con un
autocodificador aplicado a datos tabulares. Su contribución al desempeño del conjunto se determinará
mediante comparación experimental, no se presumirá de antemano.

## Arquitecturas de despliegue: de los algoritmos a los sistemas

La literatura sobre operaciones de sistemas de aprendizaje automático (MLOps, del inglés
*Machine Learning Operations*) aborda retos de mantenimiento, integración y despliegue
[@sculley2015hidden; @kreuzberger2023mlops], mientras que los textos sobre
microservicios describen la separación de componentes como una opción de diseño con implicaciones
para su despliegue y operación [@newman2021microservices]. Estas fuentes ofrecen principios
generales de ingeniería; no demuestran por sí solas ventajas específicas para sistemas de
detección de observaciones atípicas. En esta tesis se aplicarán dichos principios al diseño de una
solución por lotes y se evaluará su comportamiento operativo bajo las condiciones establecidas en
la metodología.

## Síntesis y posicionamiento de la investigación

La tabla 1 sintetiza los métodos que se prevé evaluar en esta tesis y sus principios generales.
No incluye otros procedimientos mencionados como antecedentes —por ejemplo, la prueba de Grubbs
o ECOD— porque no forman parte de la comparación experimental definida en la metodología. Las
características y limitaciones se presentan como tendencias sujetas al algoritmo concreto, los
datos y la implementación, no como propiedades universales.

<a id="tbl-sintesis-comparativa"></a>

| Enfoque | Métodos que se prevé evaluar | Principio general | Condiciones y limitaciones relevantes |
|:--|:--|:--|:--|
| Estadístico clásico, univariante y multivariante | Puntuación z robusta, rango intercuartílico y distancia de Mahalanobis [@aggarwal2017outlier] | Los dos primeros identifican desviaciones por variable mediante estadísticos robustos; Mahalanobis considera la covarianza entre variables | El alcance depende del procedimiento: las reglas univariantes no capturan por sí solas relaciones entre variables, mientras que Mahalanobis depende de una estimación adecuada de la covarianza y puede ser sensible a la dimensionalidad y a las observaciones atípicas |
| Densidad local | Local Outlier Factor (LOF) [@breunig2000lof] | Compara la densidad local de una observación con la de sus vecinas | Puede ser útil cuando una observación atípica es relativa a una vecindad significativa; sus resultados dependen de la métrica, el escalado y el tamaño de vecindad seleccionados |
| Aislamiento mediante particiones | Isolation Forest [@liu2008isolation] | Asigna puntuaciones según la facilidad con que particiones aleatorias aíslan las observaciones | El resultado depende de la estructura de los datos, el muestreo y los parámetros; no se presupone que identifique mejor toda clase de observación atípica |
| Aprendizaje profundo | Autocodificador para datos tabulares [@sakurada2014autoencoders; @pang2021deep] | Puede usar el error de reconstrucción como puntuación de atipicidad | La utilidad de esa puntuación depende de los patrones aprendidos, la arquitectura, el preprocesamiento y la función de pérdida; las observaciones atípicas no necesariamente presentan errores mayores y el costo de entrenamiento debe medirse en la configuración utilizada |

_Tabla 1: Síntesis comparativa de métodos para detectar observaciones atípicas._

A partir de la comparación, la tesis selecciona métodos que ofrecen criterios complementarios de
atipicidad en vez de asumir una ventaja universal de una familia. La puntuación z robusta y el rango
intercuartílico proporcionan líneas base univariantes; Mahalanobis permite examinar desviaciones
en la covarianza conjunta cuando la estructura y el tamaño de los datos permiten estimarla; LOF
representa observaciones atípicas locales; Isolation Forest aporta un criterio de aislamiento; y el
autocodificador permite explorar patrones no lineales mediante reconstrucción. La investigación
evalúa observaciones atípicas en datos tabulares procesados por lotes; la detección de patrones
colectivos o temporales dependería de
que esas estructuras estuvieran representadas y etiquetadas en los conjuntos de datos, y no se
inferirá solo a partir del formato tabular. Todos los métodos se ajustarán sin etiquetas de
observaciones atípicas, mientras que las etiquetas disponibles se usarán en validación para las
decisiones
metodológicas que lo requieran y, en prueba, para la comparación final. ECOD y la prueba de Grubbs
se mantienen como contexto bibliográfico, pero no como métodos experimentales.

La combinación de puntuaciones se tratará como una hipótesis empírica: las diferencias de escala y
significado entre métodos exigen normalización y una regla de ensamblado documentadas, y la
combinación podría no mejorar los resultados individuales. La tesis evaluará los métodos por
separado y frente al esquema de agregación ponderada de puntuaciones normalizadas definido en la
metodología, en conjuntos tabulares etiquetados procesados por lotes. La solución expondrá los resultados mediante una API y un
tablero; también se medirá el comportamiento operativo y la utilidad de consulta. Las conclusiones
se limitarán a los datos, configuraciones, cargas y participantes incluidos en la evaluación.

## Referencias

\bibliography

<!-- Las referencias a la [Tabla 1](#tbl-sintesis-comparativa) funcionarán como hipervínculos internos tanto en la página web generada por MkDocs como en el PDF generado por Pandoc. -->
