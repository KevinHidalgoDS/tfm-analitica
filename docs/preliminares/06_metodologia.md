# Metodología

Esta investigación adopta un enfoque metodológico de tipo aplicado y cuantitativo, con un diseño
experimental que combina el desarrollo tecnológico de un artefacto de software (el marco de trabajo de
detección y su arquitectura de despliegue) con la evaluación empírica y comparativa de su
desempeño. Dada su modalidad de profundización, el trabajo enfatiza la construcción de una solución
funcional, documentada y evaluada bajo condiciones controladas, más que la generación de un aporte
puramente teórico. El desarrollo se organiza en cinco fases secuenciales, aunque con iteraciones
internas propias de un ciclo de desarrollo ágil: (1) revisión y selección de métodos, (2) diseño
del marco de trabajo de detección, (3) diseño e implementación de la arquitectura de microservicios
en la nube, (4) construcción del tablero de visualización, y (5) evaluación integral del sistema.

## Marco de trabajo propuesto para detectar observaciones atípicas

El marco de trabajo de detección se concibe como un esquema de comparación y posible ensamblado
de métodos estadísticos, de aprendizaje automático y de aprendizaje profundo para conjuntos de
datos tabulares procesados por lotes. La evaluación considerará como métodos estadísticos la
puntuación z robusta basada en la mediana y la desviación absoluta mediana, el rango intercuartílico y,
cuando la estructura de los datos lo permita, la distancia de Mahalanobis multivariante. Como
métodos de aprendizaje automático se evaluarán Isolation Forest y Local Outlier Factor. También
se implementará un autocodificador de arquitectura densa para la representación tabular, cuya
puntuación de atipicidad se calculará a partir del error de reconstrucción
[@sakurada2014autoencoders; @pang2021deep]. Se entrenará sin utilizar las etiquetas de
observaciones atípicas; las etiquetas de validación podrán apoyar la selección de configuraciones
y umbrales, y las de prueba se reservarán para la evaluación final. La arquitectura, la función de
pérdida compatible con la representación de entrada y los hiperparámetros se definirán y
documentarán usando únicamente los datos de entrenamiento y validación. La combinación se realizará
mediante votación por umbral o agregación de puntuaciones; la metodología
experimental especificará y justificará la estrategia seleccionada, así como la normalización de
las puntuaciones y los umbrales empleados. No se contempla un metamodelo supervisado. Para
presentar los resultados, se expondrán las puntuaciones de detección y las variables asociadas
según la información que proporcione cada método; no se presupone que todas las técnicas ofrezcan
explicaciones equivalentes.

## Carga y procesamiento del conjunto de datos

Para la fase de evaluación se emplearán conjuntos de datos de referencia utilizados en la
literatura sobre detección de observaciones atípicas (por ejemplo, conjuntos disponibles en el
repositorio ODDS, sigla de *Outlier Detection DataSets*, y en repositorios públicos de datos
tabulares etiquetados), seleccionados por permitir el cálculo de métricas de desempeño.
Se incorporará también, cuando sea posible, un conjunto de datos real o semisintético
representativo de un dominio de aplicación (por ejemplo, transacciones financieras o variables de
un proceso productivo), con el fin de valorar la aplicabilidad práctica del marco de trabajo. El proceso
de carga y preprocesamiento se ejecutará en un microservicio de ingesta independiente, responsable
de: (i) la validación de esquema y tipos de datos; (ii) el tratamiento de valores faltantes
mediante estrategias documentadas (imputación o exclusión, según el porcentaje de datos ausentes);
(iii) la normalización o estandarización de variables numéricas; (iv) la codificación de variables
categóricas cuando aplique; y (v) la partición de los datos en conjuntos de entrenamiento,
validación y prueba, preservando la proporción de observaciones atípicas mediante muestreo estratificado. Los
parámetros de imputación, escalado y codificación se ajustarán con el conjunto de entrenamiento y
se aplicarán sin reajuste a validación y prueba. Las etiquetas de observaciones atípicas no se utilizarán para
entrenar el autocodificador; se reservarán para seleccionar configuraciones o umbrales con validación
y para la evaluación final en prueba. Los datos procesados se almacenarán en un formato columnar
(Parquet) para optimizar su lectura por parte de los microservicios de detección.

## Arquitectura de microservicios en la nube

La arquitectura propuesta se estructura en cinco microservicios desacoplados, comunicados mediante
interfaces de programación de aplicaciones (API, del inglés *application programming interface*)
que siguen el estilo de transferencia de estado representacional (REST, del inglés
*Representational State Transfer*) y, para los flujos de datos de mayor volumen o frecuencia,
mediante un bus de mensajería:
(1) un microservicio de ingesta y validación de datos; (2) un microservicio de preprocesamiento y
almacenamiento; (3) un microservicio de detección estadística; (4) un microservicio de detección
analítica que ejecutará los métodos de aprendizaje automático y el autocodificador e incluirá el
componente de ensamblado; y (5) un microservicio de exposición de resultados, responsable de servir
los datos consumidos por el tablero de visualización. Como plataforma de referencia se propone Amazon Web Services
(AWS), aprovechando servicios gestionados como Amazon S3 para el almacenamiento de datos originales y
procesados, contenedores desplegados mediante Amazon ECS o Amazon EKS (o, alternativamente,
funciones sin servidor mediante AWS Lambda para los componentes de menor carga computacional
continua), Amazon API Gateway para exponer los puntos de acceso, y Amazon CloudWatch para el
monitoreo de registros, métricas de uso de recursos y alertas operativas. No obstante, dado que la
arquitectura se diseña siguiendo principios de portabilidad basados en contenedores (Docker) y
orquestación estándar (Kubernetes), el marco de trabajo es funcionalmente trasladable a Microsoft Azure
(Azure Blob Storage, Azure Kubernetes Service, Azure Functions) o a Google Cloud Platform (Cloud
Storage, Google Kubernetes Engine, Cloud Run), documentándose dichas equivalencias como parte de
los productos de la tesis, de manera que la elección definitiva de proveedor pueda ajustarse a la
disponibilidad de recursos institucionales o de créditos académicos en la nube. Cada microservicio
se conteneriza de forma independiente, cuenta con su propio versionamiento y expone una interfaz
claramente definida (contrato de API), lo que permite escalar horizontalmente los componentes de
mayor demanda computacional (particularmente el microservicio de detección analítica) sin necesidad
de escalar la totalidad del sistema, así como actualizar o sustituir un método de detección sin
afectar a los demás componentes.

## Ejecución del análisis mediante los microservicios

El flujo de ejecución del análisis se desencadena mediante la carga de un conjunto de datos para su
procesamiento por lotes. El
microservicio de ingesta válida y encola los datos; el microservicio de preprocesamiento los
transforma y los persiste; los microservicios de detección estadística y de detección analítica se
ejecutan de manera paralela sobre los mismos datos preprocesados, cada uno generando sus
respectivas puntuaciones de atipicidad; el componente de ensamblado combina dichas puntuaciones y genera el
resultado final, que es persistido y expuesto mediante el microservicio de resultados. Este flujo
se orquestará mediante un mecanismo de colas o de eventos (publicación/suscripción), lo que permite
desacoplar temporalmente la ejecución de cada etapa y facilita la trazabilidad de cada análisis
mediante identificadores únicos de ejecución (ID de ejecución), insumo relevante para la reproducibilidad y
la auditoría del proceso analítico.

## Tablero de visualización de resultados

El tablero interactivo constituye la interfaz principal mediante la cual los usuarios consultarán
los resultados del marco de trabajo. Se propone que incluya, como mínimo, los siguientes
componentes: (i) un resumen de la distribución de los datos analizados, con las observaciones
señaladas como atípicas resaltadas; (ii) las puntuaciones de atipicidad asociadas a cada
observación; (iii) un desglose por variable cuando el método proporcione información que permita
asociarla con la detección; y (iv) métricas agregadas, como el número de observaciones señaladas y
los tiempos de procesamiento. El prototipo se desarrollará con Plotly Dash o Streamlit y consumirá
los datos expuestos por el microservicio de resultados mediante su API REST.

## Herramientas y tecnologías

La tabla 2 resume las principales herramientas y tecnologías consideradas para cada componente de
la solución. La selección definitiva podrá ajustarse durante el desarrollo del trabajo en función
de la disponibilidad de recursos y de los resultados de las pruebas técnicas preliminares, sin que
ello afecte la validez del diseño metodológico general.

<a id="tbl-herramientas"></a>

|      Componente     |      Herramientas / tecnologías propuestas     |      Función principal     |
|:---:|:---:|:---:|
|     Lenguaje y librerías   analíticas    |     Python 3.x; pandas, NumPy, SciPy, scikit-learn, PyOD (Python Outlier   Detection), statsmodels, PyTorch o TensorFlow    |     Implementación de los   métodos estadísticos, de aprendizaje automático y del autocodificador    |
|     Orquestación y contenedores    |     Docker para la   contenerización de cada microservicio; Kubernetes (o alternativa gestionada)   para orquestación y escalamiento    |     Empaquetado, despliegue y   escalamiento independiente de los microservicios    |
|     Plataforma en la nube    |     Proveedor de referencia:   AWS (Amazon S3, AWS Lambda / Amazon ECS o EKS, Amazon API Gateway, Amazon   CloudWatch); se documentarán equivalencias con Azure (Blob Storage, Azure   Functions/AKS) y Google Cloud (Cloud Storage, Cloud Run/GKE) para mantener   flexibilidad de implementación    |     Almacenamiento de datos,   cómputo escalable, exposición de servicios y monitoreo de la infraestructura    |
|     Mensajería y procesamiento   asíncrono    |     Apache Kafka o Amazon   Kinesis (según disponibilidad) para la coordinación de tareas por lotes entre   microservicios    |     Comunicación asíncrona   entre los servicios de ingesta, procesamiento y detección    |
|     Base de datos y almacenamiento de resultados    |     PostgreSQL para metadatos y resultados estructurados; almacenamiento de objetos (S3 o equivalente) para conjuntos de datos originales y modelos serializados    |     Persistencia de los datos de entrada, los modelos entrenados y los resultados de detección    |
|     API y comunicación entre   servicios    |     FastAPI (Python) para exponer servicios web y sus operaciones REST; documentación mediante OpenAPI/Swagger    |     Exposición de las funcionalidades de ingesta, detección y consulta de resultados    |
|     Visualización    |     Plotly Dash o Streamlit para el prototipo del tablero interactivo; alternativamente Power BI o Grafana para paneles de monitoreo operativo    |     Presentación interactiva de los resultados de detección de observaciones atípicas    |
|     Control de versiones e integración y entrega continuas (CI/CD)    |     Git/GitHub; GitHub Actions para integrar y desplegar los microservicios    |     Gestión del ciclo de vida del código y automatización del despliegue    |
|     Pruebas de carga y   desempeño    |     Locust o Apache JMeter    |     Evaluación de la   escalabilidad y los tiempos de respuesta de la arquitectura bajo distintos   volúmenes de datos    |

_Tabla 2: Herramientas y tecnologías propuestas por componente._

## Diseño de la evaluación experimental

La evaluación del marco de trabajo se realizará mediante un diseño experimental comparativo en el
que se contrastará el desempeño del esquema de ensamblado propuesto frente a: (a) cada método
estadístico aplicado de forma aislada; (b) cada algoritmo de aprendizaje automático aplicado de
forma aislada; y (c) el autocodificador, sobre los mismos conjuntos de datos y bajo las mismas
particiones de entrenamiento, validación y prueba. El autocodificador se entrenará sin etiquetas de
observaciones atípicas; las etiquetas de validación podrán utilizarse para seleccionar configuraciones y
umbrales, mientras que las etiquetas de prueba se reservarán para la evaluación final. Las
métricas de desempeño incluirán
precisión, exhaustividad, medida F1, área bajo la curva ROC (AUC-ROC) y área bajo la curva
de precisión-exhaustividad (AUC-PR), esta última especialmente relevante dado el desbalance
característico entre observaciones habituales y atípicas. Las diferencias de desempeño entre métodos
se contrastarán mediante pruebas estadísticas no paramétricas (por ejemplo, la prueba de Friedman
con post-hoc de Nemenyi) adecuadas para la comparación de múltiples algoritmos sobre múltiples
conjuntos de datos. La evaluación de la arquitectura de microservicios se realizará mediante
pruebas de carga que midan la latencia y el caudal de procesamiento del sistema bajo volúmenes crecientes de
datos. La evaluación del tablero incorporará una prueba con tareas estandarizadas y una muestra
intencional de usuarios representativos del perfil previsto, como analistas o científicos de datos.
Las tareas incluirán cargar un conjunto tabular, ejecutar la detección, localizar observaciones
señaladas e inspeccionar las variables asociadas. Se registrarán la proporción de tareas
completadas, el tiempo requerido y los errores observados; además, se aplicará el cuestionario
System Usability Scale (SUS, escala de usabilidad del sistema) y preguntas de utilidad percibida.
Estas medidas permitirán describir
la efectividad, la eficiencia y la satisfacción de uso en la muestra evaluada
[@iso9241-11-2018; @brooke1996sus]. Los resultados se interpretarán de forma descriptiva y
contextualizada, sin extrapolarlos a poblaciones más amplias.
