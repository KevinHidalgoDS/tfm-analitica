# Metodología

Esta investigación adopta un enfoque metodológico de tipo aplicado y cuantitativo, con un diseño
experimental que combina el desarrollo tecnológico de un artefacto de software (el framework de
detección y su arquitectura de despliegue) con la evaluación empírica y comparativa de su
desempeño. Dada su modalidad de profundización, el trabajo enfatiza la construcción de una solución
funcional, documentada y evaluada bajo condiciones controladas, más que la generación de un aporte
puramente teórico. El desarrollo se organiza en cinco fases secuenciales, aunque con iteraciones
internas propias de un ciclo de desarrollo ágil: (1) revisión y selección de métodos, (2) diseño
del framework de detección, (3) diseño e implementación de la arquitectura de microservicios en la
nube, (4) construcción del dashboard de visualización, y (5) evaluación integral del sistema.

## Framework propuesto para la detección de anomalías

El framework de detección se concibe como un esquema de ensamblado en dos capas. La primera capa
aplica métodos estadísticos clásicos (z-score robusto basado en la mediana y la desviación absoluta
mediana, rango intercuartílico y, cuando la variable lo permita, distancia de Mahalanobis
multivariante) sobre variables individuales o grupos de variables con comportamiento
aproximadamente conocido, generando un primer conjunto de puntajes de anomalía interpretables y
computacionalmente económicos. La segunda capa aplica métodos de analítica avanzada —Isolation
Forest y Local Outlier Factor como algoritmos base, y un autoencoder como componente de aprendizaje
profundo para escenarios de alta dimensionalidad o datos con estructura temporal— generando
puntajes de anomalía adicionales que capturan relaciones no lineales y patrones multivariantes
complejos. Los puntajes resultantes de ambas capas se combinan mediante un esquema de ensamblado
configurable (promedio ponderado, votación por umbral o un metamodelo supervisado entrenado sobre
un subconjunto de datos etiquetados, cuando dicha información esté disponible), produciendo un
puntaje de anomalía final y una clasificación binaria (o de severidad) para cada observación. El
diseño del framework contempla, además, un módulo de explicabilidad basado en la contribución
relativa de cada variable al puntaje de anomalía (por ejemplo, mediante SHAP para los modelos de
aprendizaje automático y mediante la desviación estandarizada para los métodos estadísticos),
insumo central para el dashboard.

## Carga y procesamiento del conjunto de datos

Para la fase de evaluación se emplearán conjuntos de datos de referencia ampliamente utilizados en
la literatura de detección de anomalías (por ejemplo, conjuntos disponibles en el repositorio ODDS
y en benchmarks públicos de detección de anomalías tabulares y de series de tiempo), seleccionados
por contar con anomalías etiquetadas que permiten el cálculo de métricas de desempeño supervisadas.
Se incorporará también, cuando sea posible, un conjunto de datos real o semisintético
representativo de un dominio de aplicación (por ejemplo, transacciones financieras o variables de
un proceso productivo), con el fin de valorar la aplicabilidad práctica del framework. El proceso
de carga y preprocesamiento se ejecutará en un microservicio de ingesta independiente, responsable
de: (i) la validación de esquema y tipos de datos; (ii) el tratamiento de valores faltantes
mediante estrategias documentadas (imputación o exclusión, según el porcentaje de datos ausentes);
(iii) la normalización o estandarización de variables numéricas; (iv) la codificación de variables
categóricas cuando aplique; y (v) la partición de los datos en conjuntos de entrenamiento,
validación y prueba, preservando la proporción de anomalías mediante muestreo estratificado. Los
datos procesados se almacenarán en un formato columnar (Parquet) para optimizar su lectura por
parte de los microservicios de detección.

## Arquitectura de microservicios en la nube

La arquitectura propuesta se estructura en cinco microservicios desacoplados, comunicados mediante
API REST y, para los flujos de datos de mayor volumen o frecuencia, mediante un bus de mensajería:
(1) un microservicio de ingesta y validación de datos; (2) un microservicio de preprocesamiento y
almacenamiento; (3) un microservicio de detección estadística (capa 1 del framework); (4) un
microservicio de detección analítica/aprendizaje automático (capa 2 del framework), que incluye el
componente de ensamblado; y (5) un microservicio de exposición de resultados, responsable de servir
los datos consumidos por el dashboard. Como plataforma de referencia se propone Amazon Web Services
(AWS), aprovechando servicios gestionados como Amazon S3 para el almacenamiento de datos crudos y
procesados, contenedores desplegados mediante Amazon ECS o Amazon EKS (o, alternativamente,
funciones serverless mediante AWS Lambda para los componentes de menor carga computacional
continua), Amazon API Gateway para la exposición de los endpoints, y Amazon CloudWatch para el
monitoreo de logs, métricas de uso de recursos y alertas operativas. No obstante, dado que la
arquitectura se diseña siguiendo principios de portabilidad basados en contenedores (Docker) y
orquestación estándar (Kubernetes), el framework es funcionalmente trasladable a Microsoft Azure
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

El flujo de ejecución del análisis se desencadena mediante la llegada de nuevos datos (en modo por
lotes o en modo de streaming simulado para efectos de la evaluación de escalabilidad). El
microservicio de ingesta válida y encola los datos; el microservicio de preprocesamiento los
transforma y los persiste; los microservicios de detección estadística y de detección analítica se
ejecutan de manera paralela sobre los mismos datos pre-procesados, cada uno generando sus
respectivos puntajes de anomalía; el componente de ensamblado combina dichos puntajes y genera el
resultado final, que es persistido y expuesto mediante el microservicio de resultados. Este flujo
se orquestará mediante un mecanismo de colas o de eventos (publicación/suscripción), lo que permite
desacoplar temporalmente la ejecución de cada etapa y facilita la trazabilidad de cada análisis
mediante identificadores únicos de ejecución (run ID), insumo relevante para la reproducibilidad y
la auditoría del proceso analítico.

## Dashboard de visualización de resultados

El dashboard interactivo constituye la interfaz principal mediante la cual los usuarios de negocio
interactúan con los resultados del framework. Se propone que incluya, como mínimo, los siguientes
componentes: (i) un panel general con la serie temporal o distribución de los datos analizados,
resaltando las observaciones clasificadas como anómalas; (ii) un indicador del puntaje de anomalía
y su evolución en el tiempo; (iii) un desglose por variable de la contribución relativa a cada
anomalía detectada (explicabilidad), que permita a un usuario no especializado comprender por qué
una observación fue señalada como atípica; (iv) métricas agregadas de desempeño del sistema (número
de anomalías detectadas por periodo, tasa de falsos positivos estimada cuando existan datos de
validación, tiempos de procesamiento); y (v) un mecanismo de retroalimentación mediante el cual el
usuario pueda confirmar o descartar una anomalía detectada, insumo que podrá emplearse para la
recalibración futura del modelo. El prototipo del dashboard se desarrollará utilizando Plotly Dash
o Streamlit, consumiendo los datos expuestos por el microservicio de resultados a través de su API
REST.

## Herramientas y tecnologías

La tabla 2 resume las principales herramientas y tecnologías consideradas para cada componente de
la solución. La selección definitiva podrá ajustarse durante el desarrollo del trabajo en función
de la disponibilidad de recursos y de los resultados de las pruebas técnicas preliminares, sin que
ello afecte la validez del diseño metodológico general.

<a id="tbl-herramientas"></a>

|      Componente     |      Herramientas / tecnologías propuestas     |      Función principal     |
|:---:|:---:|:---:|
|     Lenguaje y librerías   analíticas    |     Python 3.x; pandas, NumPy, SciPy, scikit-learn, PyOD (Python Outlier   Detection), statsmodels; TensorFlow/PyTorch para componentes de aprendizaje   profundo    |     Implementación de los   métodos estadísticos, de aprendizaje automático y de aprendizaje profundo del   framework    |
|     Orquestación y contenedores    |     Docker para la   contenerización de cada microservicio; Kubernetes (o alternativa gestionada)   para orquestación y escalamiento    |     Empaquetado, despliegue y   escalamiento independiente de los microservicios    |
|     Plataforma en la nube    |     Proveedor de referencia:   AWS (Amazon S3, AWS Lambda / Amazon ECS o EKS, Amazon API Gateway, Amazon   CloudWatch); se documentarán equivalencias con Azure (Blob Storage, Azure   Functions/AKS) y Google Cloud (Cloud Storage, Cloud Run/GKE) para mantener   flexibilidad de implementación    |     Almacenamiento de datos,   cómputo escalable, exposición de servicios y monitoreo de la infraestructura    |
|     Mensajería y procesamiento   de flujos    |     Apache Kafka o Amazon   Kinesis (según disponibilidad) para la ingesta y el streaming de datos entre   microservicios    |     Comunicación asíncrona   entre los servicios de ingesta, procesamiento y detección    |
|     Base de datos y   almacenamiento de resultados    |     PostgreSQL para metadatos y   resultados estructurados; almacenamiento de objetos (S3 o equivalente) para   conjuntos de datos crudos y modelos serializados    |     Persistencia de los datos   de entrada, los modelos entrenados y los resultados de detección    |
|     API y comunicación entre   servicios    |     FastAPI (Python) para   exponer endpoints REST de cada microservicio; documentación mediante   OpenAPI/Swagger    |     Exposición de las   funcionalidades de ingesta, detección y consulta de resultados    |
|     Visualización y dashboard    |     Plotly Dash o Streamlit   para el prototipo del dashboard interactivo; alternativamente Power BI o   Grafana para paneles de monitoreo operativo    |     Presentación interactiva de   los resultados de detección de anomalías    |
|     Control de versiones y   CI/CD    |     Git/GitHub; GitHub Actions   para integración y despliegue continuo de los microservicios    |     Gestión del ciclo de vida   del código y automatización del despliegue    |
|     Pruebas de carga y   desempeño    |     Locust o Apache JMeter    |     Evaluación de la   escalabilidad y los tiempos de respuesta de la arquitectura bajo distintos   volúmenes de datos    |

_Tabla 2: Herramientas y tecnologías propuestas por componente._

## Diseño de la evaluación experimental

La evaluación del framework se realizará mediante un diseño experimental comparativo en el que se
contrastará el desempeño del esquema híbrido propuesto frente a: (a) cada método estadístico
aplicado de forma aislada; (b) cada algoritmo de aprendizaje automático aplicado de forma aislada;
y (c) el componente de aprendizaje profundo aplicado de forma aislada, sobre los mismos conjuntos
de datos y bajo las mismas particiones de entrenamiento/prueba. Las métricas de desempeño incluirán
precisión, exhaustividad (recall), F1-score, área bajo la curva ROC (AUC-ROC) y área bajo la curva
de precisión-exhaustividad (AUC-PR), esta última especialmente relevante dado el desbalance
característico entre observaciones normales y anómalas. Las diferencias de desempeño entre métodos
se contrastarán mediante pruebas estadísticas no paramétricas (por ejemplo, la prueba de Friedman
con post-hoc de Nemenyi) adecuadas para la comparación de múltiples algoritmos sobre múltiples
conjuntos de datos. La evaluación de la arquitectura de microservicios se realizará mediante
pruebas de carga que midan la latencia y el throughput del sistema bajo volúmenes crecientes de
datos, mientras que la evaluación del dashboard incorporará una validación cualitativa con un grupo
reducido de usuarios (expertos de dominio o compañeros del programa de maestría), mediante un
cuestionario breve de usabilidad y utilidad percibida.
