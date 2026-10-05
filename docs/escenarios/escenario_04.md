# Escenario 4

## Datos

<!-- prettier-ignore -->
| Dataset | Estructura de datos | Complejidad temporal | Potencial de anomalías | Encaje con modelos avanzados | Justificación de prioridad |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Precio de Bolsa Nacional (horario) | Univariado en su forma básica, pero fácilmente multivariado al incorporar variables exógenas: demanda, generación, aportes hídricos, disponibilidad. La serie horaria tiene alta frecuencia y muchos valores atípicos. | Muy alta: resolución horaria, con picos extremos, cambios de régimen y efectos de mercado (ofertas, contratos). No estacionaria con clustering de volatilidad. | Muy alto: picos anómalos, manipulación de precios, comportamientos atípicos en horas de alta demanda/baja oferta, cambios estructurales en formación de precios. Es la variable más crítica para la transparencia del mercado. | Excelente. LSTM/GRU para capturar dependencias temporales largas, autoencoders variacionales (VAE) para detección de anomalías en precios, CNN-LSTM híbridos para extraer patrones espacio-temporales, isolation forests como baseline. | Aunque univariado en origen, su valor para deep learning explota al integrarlo con otros datasets (demanda, generación, aportes). El Banco de la República ya desarrolló una metodología de detección de anomalías en ofertas de agentes pivotales usando machine learning, lo que valida la aproximación y su relevancia regulatoria. |

### 1. ¿Cuál es el problema?

El problema central es la dificultad técnica y operativa de identificar observaciones
verdaderamente atípicas (como posibles manipulaciones o picos anómalos) en el **Precio de Bolsa
Nacional**, una variable que posee una complejidad temporal muy alta, no estacionariedad, clústeres
de volatilidad y cambios de régimen. Aunque existen modelos teóricos para analizar esto, llevar
estos métodos a una solución funcional aplicable —que estructure los datos horarios y exógenos en
un formato tabular procesado por lotes, evalúe las anomalías y las presente de forma comprensible a
los usuarios— constituye un reto significativo de MLOps y diseño de interfaces.

### 2. ¿Por qué es importante?

Este análisis es vital porque el precio de bolsa es la **variable más crítica para la transparencia
del mercado eléctrico**. Detectar comportamientos atípicos en horas de alta demanda o baja oferta
no es un mero ejercicio estadístico, sino una necesidad de vigilancia regulatoria. La importancia
de este enfoque ya ha sido validada por instituciones como el Banco de la República, que ha
desarrollado metodologías de _machine learning_ para monitorear ofertas de agentes pivotales.
Proveer un sistema escalable y una interfaz visual adecuada democratiza el acceso a este nivel de
escrutinio para analistas y entes de control.

### 3. ¿Por qué no ha sido suficiente?

Hasta ahora, no ha sido suficiente porque los enfoques tradicionales a menudo analizan la serie de
forma estrictamente univariada o mediante métodos estadísticos clásicos aislados, los cuales
fracasan ante las características no estacionarias y los efectos de mercado subyacentes. Por otro
lado, aunque existen modelos avanzados de frontera (como VAEs, LSTM, o híbridos), estos suelen
quedarse en entornos de investigación (entornos locales en cuadernos de experimentación) y carecen
de un empaquetamiento en arquitecturas de microservicios robustas. Faltan soluciones integradas que
apliquen ensambles ponderados de detección y, lo más importante, que logren traducir la salida de
modelos complejos (como un _Autoencoder_ o un _Isolation Forest_) en un **tablero interactivo**
(deseable) que un usuario no especializado en estadística profunda pueda interpretar.

### 4. ¿Cuál es la propuesta?

La propuesta es adaptar este conjunto de datos, estructurándolo de forma multivariada (integrando
variables exógenas como demanda, generación y aportes hídricos en formato tabular), para inyectarlo
en el **marco de trabajo híbrido** diseñado en la tesis. Se propone:

- Desplegar una **arquitectura de microservicios** (ingesta, preprocesamiento, detección
  estadística y analítica).
- Procesar los datos de bolsa por lotes, aplicando un ensamble ponderado que combina líneas base
  robustas (estadística clásica e _Isolation Forest_) con métodos de aprendizaje profundo
  (_Autoencoders densos_).
- Exponer los resultados a través de un **tablero interactivo** (deseable) que desglosará las
  puntuaciones de atipicidad del precio y resaltará las variables exógenas que más influyeron en la
  detección de la anomalía, permitiendo a los usuarios contextualizar los "picos" del mercado.

### 5. ¿Qué se espera encontrar?

Se espera encontrar que el esquema híbrido de detección reduzca la tasa de falsos positivos frente
a la volatilidad normal del mercado, distinguiendo exitosamente los picos normales de escasez
hídrica de las anomalías estructurales o posibles manipulaciones. Operativamente, se espera que la
solución basada en microservicios demuestre ser capaz de procesar eficientemente los altos
volúmenes de datos horarios integrados. Finalmente, desde la experiencia del usuario, se espera
comprobar empíricamente que el uso del tablero visual (con puntuaciones y variables explicativas
del mercado) mejorará la comprensión, exactitud y rapidez con la que los analistas logran
interpretar por qué una hora específica de la bolsa fue catalogada como anómala, superando
ampliamente a las listas tradicionales de resultados.
