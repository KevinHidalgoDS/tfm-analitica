# Escenario 2

## Datos

<!-- prettier-ignore -->
| Nombre del dataset | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace directo al portal |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demanda Comercial del SIN | Consumo real de energía facturado por los comercializadores en distintas regiones del país.<br><br>Periodicidad: Horaria.| Exhibe marcada estacionalidad. La detección de outliers permite identificar tempranamente fallas en infraestructura de medida, incremento en pérdidas no técnicas (fraude) o choques macroeconómicos modelando covariables de calendario. | Distribuidores y Operadores de Red (balanceo de carga, control de pérdidas), XM (planeación operativa), Investigadores (pronóstico de demanda). | Es vital minimizar el error de pronóstico operativo y asegurar la precisión absoluta en la liquidación de cuentas y cargos del mercado por parte del ASIC. | Reportes de XM sobre desviaciones operativas vs. comerciales; múltiples tesis académicas en repositorios (ej. UNAL) sobre pronóstico y limpieza de demanda usando RNNs. | [Catálogo - Información Comercial](https://www.google.com/search?q=https://www.simem.co/datos/informacion-comercial) |
Datasets a cruzar: Precio de Bolsa Nacional + Aportes Hídricos + Generación Real. Técnicas
posibles: Autoencoders Multivariados, Redes LSTMs (Long Short-Term Memory) o Transformers para
series de tiempo.

- **Por qué:** La demanda eléctrica es fuertemente estacional. El principal reto analítico aquí es
  separar el ruido (efectos de fines de semana, festivos, olas de calor) de las verdaderas
  anomalías.

- **El enfoque:** Para establecer un punto de partida sólido, las herramientas orientadas al ajuste
  de distribuciones y pruebas estadísticas clásicas de outliers (usando el ecosistema de
  scipy.stats, distfit, numpy y pandas) funcionan excelente como línea base univariada.
  Posteriormente, se puede escalar a un modelo profundo que incorpore la estacionalidad como
  tensores de entrada para identificar caídas abruptas en el consumo que representen pérdidas no
  técnicas (fraude o robo de energía a gran escala) o fallas sistémicas de medición.

### 1. ¿Cuál es el problema?

El problema consiste en identificar de manera precisa las verdaderas anomalías en la Demanda
Comercial del SIN (como fallas sistémicas de medición o robo de energía) separándolas del fuerte
ruido estacional inherente al consumo eléctrico, como efectos de fines de semana, festivos u olas
de calor. Aunque existen múltiples algoritmos en la literatura para abordar esto, el reto principal
radica en que llevar estos métodos a una solución utilizable requiere superar problemas de
integración, mantenimiento y despliegue. Es decir, el problema no es solo aislar la estacionalidad,
sino diseñar una solución basada en microservicios que procese estos datos tabulares por lotes y
entregue los resultados en un tablero interpretable para los operadores.

### 2. ¿Por qué es importante?

En el contexto del sector eléctrico, resolver esto es vital para minimizar el error de pronóstico
operativo de entidades como XM y asegurar una precisión absoluta en la liquidación de cuentas y
cargos del mercado por parte del ASIC. Desde la perspectiva metodológica, la validez de la
analítica de datos y de la toma de decisiones depende directamente de la calidad de los datos.
Identificar tempranamente observaciones atípicas originadas por errores de medición, fraudes
(pérdidas no técnicas) o eventos excepcionales permite fortalecer la vigilancia de los indicadores
operativos de la red eléctrica.

### 3. ¿Por qué no ha sido suficiente?

No ha sido suficiente porque utilizar únicamente herramientas de ajuste de distribuciones y pruebas
estadísticas clásicas univariadas (usando ecosistemas como `scipy.stats`, `distfit`, `numpy` y
`pandas`) sirve como un excelente punto de partida, pero puede quedarse corto ante relaciones
multivariadas o patrones complejos. Los métodos estadísticos tradicionales difieren en sus
supuestos y no siempre logran detectar observaciones atípicas definidas por relaciones entre
múltiples variables, como los tensores de estacionalidad. Además, disponer de algoritmos avanzados
aislados es insuficiente si no se integran bajo una arquitectura estructurada de operaciones de
sistemas de aprendizaje automático (MLOps) que permita escalar el análisis y facilitar la consulta
de los usuarios finales.

### 4. ¿Cuál es la propuesta?

La propuesta es utilizar el registro de la Demanda Comercial del SIN como el conjunto de datos real
representativo del dominio de aplicación. Sobre estos datos, se implementará un marco de trabajo
híbrido que partirá de la línea base univariada y estadística, y escalará hasta integrar algoritmos
de aprendizaje automático y un modelo profundo (autocodificador) capaz de incorporar la
estacionalidad para identificar caídas abruptas. Las puntuaciones de estos métodos se combinarán
mediante una agregación ponderada. Todo este ecosistema analítico operará sobre una arquitectura de
microservicios en la nube, la cual alimentará un tablero interactivo diseñado para que los
investigadores y operadores de red analicen visualmente las anomalías detectadas.

### 5. ¿Qué se espera encontrar?

Se espera que este marco híbrido logre aislar correctamente el ruido estacional y alcance un
desempeño de clasificación de anomalías (medido en F1) superior al de las pruebas estadísticas
clásicas o modelos individuales aplicados por separado. Operativamente, se anticipa que el esquema
reduzca la tasa de falsos positivos frente a los métodos individuales (evitando alertar falsos
fraudes durante festivos), sin incrementar los falsos negativos en más de cinco puntos
porcentuales. Finalmente, se espera que la arquitectura de microservicios soporte el procesamiento
por lotes de los datos horarios sin degradar su latencia frente a un sistema tradicional, y que los
operadores interpreten las alertas de infraestructura o fraude con mayor exactitud y rapidez
gracias al tablero de visualización.
