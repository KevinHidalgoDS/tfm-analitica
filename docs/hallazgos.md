# Hallazgos de la propuesta de investigación

Este documento sintetiza la información disponible en los archivos de `preliminares`. Distingue
entre lo que la propuesta ya define y aquello que todavía requiere evidencia o decisiones
concretas; las afirmaciones sobre resultados se entienden como expectativas, no como hallazgos
empíricos.

## 1. ¿Cuál es el problema?

La propuesta aborda el diseño, la implementación y la evaluación de una solución integrada para
detectar observaciones atípicas en conjuntos de datos tabulares procesados por lotes. El problema
no se limita a identificar observaciones inusuales: también comprende integrar métodos con
principios distintos en una API, operar la solución mediante microservicios en la nube y presentar
los resultados en un tablero que facilite su consulta e interpretación.

La pregunta principal plantea cómo construir esa solución y evaluar tres dimensiones: el desempeño
de detección de los métodos individuales y del ensamblado; el comportamiento operativo de los
microservicios frente a una implementación monolítica equivalente; y la utilidad del tablero frente
a una lista de resultados. El alcance excluye la detección en tiempo real y la especialización en
un sector económico.

**Completitud: suficiente.** El problema, sus dimensiones, la pregunta de investigación y sus
límites están formulados explícitamente.

## 2. ¿Por qué es importante?

La calidad de los datos condiciona la validez de los análisis y decisiones organizacionales. Las
observaciones atípicas pueden originarse en errores de medición, fraude, fallas de sistemas,
eventos excepcionales o procesos heterogéneos; por ello, detectarlas puede apoyar actividades como
el monitoreo de calidad de datos, el control de procesos y la detección temprana de situaciones
inusuales.

La importancia de la investigación también radica en que una solución aplicada debe atender más que
la métrica algorítmica: necesita integrar y operar sus componentes, responder a distintos volúmenes
de datos y comunicar los resultados a personas no especializadas. La propuesta busca aportar
evidencia contextualizada sobre esos aspectos y un artefacto funcional, sin afirmar que los
resultados se generalizarán a cualquier dominio.

**Completitud: suficiente.** Se presentan razones académicas, tecnológicas y prácticas, y se
delimita el alcance de las conclusiones. La justificación podría ganar fuerza con un caso de uso y
una necesidad organizacional concretos, pero no son indispensables para comprender la pertinencia
declarada.

## 3. ¿Qué se ha hecho?

La literatura citada ha desarrollado y sistematizado enfoques diversos para la detección de
observaciones atípicas: reglas estadísticas univariantes y multivariantes, métodos de densidad
local como LOF, métodos de aislamiento como Isolation Forest y técnicas de aprendizaje profundo
como los autocodificadores. También existen revisiones sobre detección de anomalías y trabajos
sobre operación de sistemas de aprendizaje automático, microservicios y diseño de tableros.

La propuesta señala que estos enfoques difieren en supuestos, sensibilidad a la representación de
los datos, parámetros y necesidades de cómputo; por tanto, no da por sentada la superioridad de una
familia. El estado del arte declara que se elaboró mediante una búsqueda exploratoria en la web,
sin protocolo sistemático ni registro exhaustivo de fuentes, consultas, fechas y selección. Los
documentos no reportan todavía experimentos propios ni una implementación concluida: describen el
trabajo que se propone realizar.

**Completitud: parcial.** Se identifican familias de métodos y antecedentes pertinentes, pero la
revisión no es sistemática y aún no aporta resultados empíricos propios. Falta consolidar la
búsqueda y precisar qué evidencia comparable existe sobre la integración de detección, operación y
presentación de resultados en una misma solución.

## 4. ¿Por qué no ha sido suficiente?

Los antecedentes descritos cubren métodos y retos relacionados, pero no resuelven por sí solos el
problema aplicado que plantea la tesis. En particular, la diversidad de supuestos y comportamientos
hace necesario comparar los métodos en datos y escenarios definidos; la literatura general de MLOps
y microservicios no demuestra qué comportamiento tendrá esta solución; y la existencia de
resultados analíticos no garantiza que usuarios no especializados puedan interpretarlos con
eficacia.

La propuesta, por tanto, identifica una necesidad de integración y evaluación conjunta: contrastar
métodos individuales y un ensamblado, medir la operación de microservicios frente a un monolito y
evaluar el tablero frente a una lista de resultados. Sin embargo, el estado del arte reconoce que
su búsqueda fue exploratoria y no permite afirmar que la brecha sea universal. Los preliminares
tampoco documentan aún una comparación sistemática que establezca con precisión qué soluciones
integradas existentes cubren —o dejan sin cubrir— esas tres dimensiones.

**Completitud: parcial.** La insuficiencia está razonada como motivación de la propuesta, pero la
brecha de conocimiento requiere mayor sustento bibliográfico antes de presentarse como una
conclusión sobre el estado de la literatura.

## 5. ¿Cuál es la propuesta?

Diseñar, implementar y evaluar un marco de trabajo híbrido para conjuntos tabulares procesados por
lotes. Se compararán la puntuación z robusta, el rango intercuartílico, la distancia de Mahalanobis
cuando sea aplicable, Isolation Forest, LOF y un autocodificador denso. Cada método producirá una
puntuación continua; el ensamblado combinará puntuaciones normalizadas mediante agregación
ponderada. Las ponderaciones, los umbrales y las configuraciones se seleccionarán con entrenamiento
y validación, reservando la prueba para la evaluación final.

La solución se desplegará como microservicios contenerizados en la nube e incluirá ingesta,
preprocesamiento, detección estadística, detección analítica con ensamblado y exposición de
resultados. AWS se propone como plataforma de referencia, con equivalencias documentadas para Azure
y Google Cloud. Un tablero interactivo presentará las puntuaciones, las observaciones señaladas,
las variables asociadas cuando estén disponibles y métricas agregadas.

La evaluación comparará los métodos mediante precisión, exhaustividad, F1, AUC-ROC y AUC-PR;
analizará la interacción del método con el tipo de anomalía y la dimensionalidad; comparará
microservicios con un monolito bajo cargas controladas; y contrastará el tablero con una lista de
resultados mediante tareas con usuarios no especializados. Las conclusiones se limitarán a los
conjuntos de datos, configuraciones, cargas y participantes incluidos.

**Completitud: suficiente.** La solución, sus componentes principales, comparadores, métricas y
alcance están descritos. Permanecen por concretar decisiones de ejecución —por ejemplo, los
conjuntos de datos definitivos, el proveedor de nube y la configuración detallada del ensamblado—,
pero la dirección metodológica está definida.

## 6. ¿Qué se espera encontrar?

Se espera obtener evidencia empírica sobre cuándo el ensamblado ponderado ofrece ventajas o no
frente a sus métodos individuales y al mejor método individual seleccionado con validación. También
se espera identificar si el desempeño varía según el tipo de observación atípica y la
dimensionalidad. Las hipótesis anticipan una posible reducción de falsos positivos sin un aumento
de falsos negativos superior a cinco puntos porcentuales, así como diferencias de desempeño entre
escenarios; son hipótesis por contrastar, no resultados asegurados.

En la dimensión operativa, se medirán latencia, caudal y uso de CPU y memoria de microservicios y
monolito bajo distintos volúmenes y niveles de concurrencia. En la dimensión de uso, se espera que
el tablero con puntuaciones y variables explicativas mejore la comprensión e interpretación frente
a una lista, evaluando respuestas correctas, tiempo, comprensión percibida, usabilidad y utilidad.

Como productos, se prevén un marco de trabajo funcional y documentado, evidencia comparativa en al
menos tres conjuntos de referencia etiquetados, una arquitectura desplegada, un prototipo de
tablero y un repositorio reproducible. La propuesta reconoce limitaciones potenciales por
disponibilidad y calidad de etiquetas, presupuesto de nube y tamaño de la muestra de usuarios.

**Completitud: parcial.** Los resultados que se medirán, las comparaciones y las hipótesis están
definidos; no existen todavía datos que permitan anticipar qué métodos o arquitectura obtendrán
mejores resultados. También faltan detalles operativos finales para que las expectativas sean
plenamente verificables, como los conjuntos y cargas definitivos, los criterios de éxito de
escalabilidad y el tamaño de muestra del estudio con usuarios.

## Plan de Acción

1. **Sustentar y delimitar la brecha de investigación.** Completar la búsqueda del estado del arte
   con un protocolo reproducible: bases consultadas, cadenas de búsqueda, periodo, criterios de
   inclusión y exclusión, y registro de selección. Comparar estudios directamente relacionados con
   ensamblado de detectores, despliegue operativo y evaluación de interfaces; luego precisar qué
   contribución integrada y acotada aporta esta tesis.
2. **Fijar el protocolo experimental antes de evaluar.** Seleccionar y documentar los conjuntos de
   datos definitivos, sus etiquetas, los tipos de anomalía representados y la cobertura de rangos
   de dimensionalidad. Definir las particiones, la regla de normalización, la estrategia de
   ponderación, los umbrales y el análisis estadístico, manteniendo intactas las etiquetas de
   prueba.
3. **Convertir las hipótesis operativas en criterios verificables.** Especificar volúmenes, niveles
   de concurrencia, recursos equivalentes, repeticiones y umbrales de latencia/caudal para comparar
   arquitecturas. Revisar además que cada hipótesis nula y su regla de decisión se correspondan con
   las métricas y análisis definidos.
4. **Cerrar el diseño de evaluación con usuarios.** Definir el tamaño de muestra y sus criterios de
   inclusión, las tareas, la escala de comprensión/confianza, el instrumento de utilidad y el plan
   de análisis entre condiciones; documentar cómo se controlarán sesgos y limitaciones de la
   muestra.
5. **Revisar la coherencia y el alcance de las afirmaciones.** Mantener separados los resultados
   esperados de los resultados observados y limitar las conclusiones a las condiciones evaluadas.
   Tras ejecutar los experimentos, reemplazar las expectativas por hallazgos respaldados por datos
   e informar resultados no favorables o inconclusos, así como limitaciones.

## Gemini

<!-- prettier-ignore -->
| Nombre del dataset | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace directo al portal |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Precio de Bolsa Nacional (Mercado Spot) | Precio horario al que se tranza la energía mayorista, determinado por la intersección de oferta y demanda.<br><br>Periodicidad: Horaria. | Altamente volátil ante choques climáticos. Requiere modelos avanzados (ej. Autoencoders, LSTMs) multivariados (cruzando con hidrología y disponibilidad térmica) para detectar spikes atípicos, cambios de régimen abruptos o manipulación de ofertas. | Traders (gestión de riesgo financiero), CREG y SIC (monitoreo de poder de mercado e Índice de Oferta Residual), Generadores (optimización de estrategias de oferta). | Impacta directamente la formación de tarifas para el usuario final y determina la exposición financiera y riesgo de quiebra de los agentes comercializadores. | "Anomaly Detection and Market Power in Colombian Electricity Market" ([Documento de Trabajo, Banco de la República, 2022](https://www.banrep.gov.co/en/taxonomy/term/25/all?page=17&order=title&sort=desc)). | [Catálogo - Información Comercial](https://www.google.com/search?q=https://www.simem.co/datos/informacion-comercial) |
| Demanda Comercial del SIN | Consumo real de energía facturado por los comercializadores en distintas regiones del país.<br><br>Periodicidad: Horaria. | Exhibe marcada estacionalidad. La detección de outliers permite identificar tempranamente fallas en infraestructura de medida, incremento en pérdidas no técnicas (fraude) o choques macroeconómicos modelando covariables de calendario. | Distribuidores y Operadores de Red (balanceo de carga, control de pérdidas), XM (planeación operativa), Investigadores (pronóstico de demanda). | Es vital minimizar el error de pronóstico operativo y asegurar la precisión absoluta en la liquidación de cuentas y cargos del mercado por parte del ASIC. | Reportes de XM sobre desviaciones operativas vs. comerciales; múltiples tesis académicas en repositorios (ej. UNAL) sobre pronóstico y limpieza de demanda usando RNNs. | [Catálogo - Información Comercial](https://www.google.com/search?q=https://www.simem.co/datos/informacion-comercial) |
| Generación Real por Planta y Recurso | Energía inyectada físicamente al SIN por cada unidad generadora (hídrica, térmica, solar, eólica).<br><br>Periodicidad: Horaria. | Análisis multivariado cruzando la declaración de disponibilidad técnica vs. la generación efectiva permite identificar outages encubiertos, fallas de máquinas u omisiones en el despacho ideal. | XM (supervisión de seguridad), Operadores de planta (mantenimiento predictivo basado en datos), Auditores regulatorios. | Garantiza la confiabilidad estructural del sistema eléctrico al verificar el cumplimiento de las Obligaciones de Energía Firme (OEF) del Cargo por Confiabilidad. | "Evaluation of Anomaly Detection of an Autoencoder Based on Maintenance Information and Scada-Data" (Elsevier, modelo extrapolable a operación hidroeléctrica local). | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |
| Aportes Hídricos (Energía Equivalente) | Caudales naturales que ingresan a los embalses del sistema interconectado, convertidos en kWh.<br><br>Periodicidad: Diaria. | Variable de entrada fundamental. Detectar anomalías (sequías extremas, picos de vertimiento) con Deep Learning advierte de forma temprana fases críticas de estrés en el despacho. | XM (planeación energética de mediano/largo plazo), Generadores hidroeléctricos (curvas de vaciado y valoración de la prima de escasez del agua). | Al contar con una matriz eléctrica con ~68% de dependencia hídrica, anticipar variaciones anómalas es el eje principal para prevenir situaciones de racionamiento. | Estudios de variabilidad hidroclimatológica y series de tiempo de El Niño/La Niña emitidos periódicamente por XM e IDEAM. [Enlace](https://informeanual.xm.com.co/informe/pages/xm/22-condiciones-climaticas.html) | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |
| Generación de Seguridad y Restricciones Operativas | Energía que se despacha fuera de mérito económico para evitar fallas o aliviar congestiones, junto con su costo de remuneración.<br><br>Periodicidad: Horaria. | Anomalías en los sobrecostos de restricciones evidencian cuellos de botella emergentes, topologías de red críticas o abuso de posiciones dominantes zonales. Útil para algoritmos de clustering espacial. | Transmisores (justificación de planes de expansión), CREG y SSPD (mitigación de rentas de congestión). | Los costos por restricciones se trasladan directamente a la demanda. Picos anómalos incrementan drásticamente el Costo Unitario (CU) de prestación del servicio. | Implementaciones técnicas derivadas de la Resolución CREG 101-018 de 2023 sobre vigilancia de ofertas y evaluación del esquema de restricciones zonales. | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |

[PyDataSIMEM](https://github.com/XM-SA-ESP/GEDeN-SIMEM-Tools)

### Prioridad 1: Dinámica de Precios y Riesgo Sistémico (LSTM/Autoencoders)

Datasets a cruzar: Precio de Bolsa Nacional + Aportes Hídricos + Generación Real. Técnicas
recomendadas: Autoencoders Multivariados, Redes LSTMs (Long Short-Term Memory) o Transformers para
series de tiempo.

<!-- prettier-ignore -->
| Nombre del dataset | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace directo al portal |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Precio de Bolsa Nacional (Mercado Spot) | Precio horario al que se tranza la energía mayorista, determinado por la intersección de oferta y demanda.<br><br>Periodicidad: Horaria. | Altamente volátil ante choques climáticos. Requiere modelos avanzados (ej. Autoencoders, LSTMs) multivariados (cruzando con hidrología y disponibilidad térmica) para detectar spikes atípicos, cambios de régimen abruptos o manipulación de ofertas. | Traders (gestión de riesgo financiero), CREG y SIC (monitoreo de poder de mercado e Índice de Oferta Residual), Generadores (optimización de estrategias de oferta). | Impacta directamente la formación de tarifas para el usuario final y determina la exposición financiera y riesgo de quiebra de los agentes comercializadores. | "Anomaly Detection and Market Power in Colombian Electricity Market" ([Documento de Trabajo, Banco de la República, 2022](https://www.banrep.gov.co/en/taxonomy/term/25/all?page=17&order=title&sort=desc)). | [Catálogo - Información Comercial](https://www.google.com/search?q=https://www.simem.co/datos/informacion-comercial) |
| Generación Real por Planta y Recurso | Energía inyectada físicamente al SIN por cada unidad generadora (hídrica, térmica, solar, eólica).<br><br>Periodicidad: Horaria. | Análisis multivariado cruzando la declaración de disponibilidad técnica vs. la generación efectiva permite identificar outages encubiertos, fallas de máquinas u omisiones en el despacho ideal. | XM (supervisión de seguridad), Operadores de planta (mantenimiento predictivo basado en datos), Auditores regulatorios. | Garantiza la confiabilidad estructural del sistema eléctrico al verificar el cumplimiento de las Obligaciones de Energía Firme (OEF) del Cargo por Confiabilidad. | "Evaluation of Anomaly Detection of an Autoencoder Based on Maintenance Information and Scada-Data" (Elsevier, modelo extrapolable a operación hidroeléctrica local). | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |
| Aportes Hídricos (Energía Equivalente) | Caudales naturales que ingresan a los embalses del sistema interconectado, convertidos en kWh.<br><br>Periodicidad: Diaria. | Variable de entrada fundamental. Detectar anomalías (sequías extremas, picos de vertimiento) con Deep Learning advierte de forma temprana fases críticas de estrés en el despacho. | XM (planeación energética de mediano/largo plazo), Generadores hidroeléctricos (curvas de vaciado y valoración de la prima de escasez del agua). | Al contar con una matriz eléctrica con ~68% de dependencia hídrica, anticipar variaciones anómalas es el eje principal para prevenir situaciones de racionamiento. | Estudios de variabilidad hidroclimatológica y series de tiempo de El Niño/La Niña emitidos periódicamente por XM e IDEAM. [Enlace](https://informeanual.xm.com.co/informe/pages/xm/22-condiciones-climaticas.html) | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |

- **Por qué es la máxima prioridad:** El mercado eléctrico colombiano tiene un ~68% de dependencia
  hídrica. Un análisis univariado del Precio de Bolsa generará demasiados "falsos positivos" de
  anomalías durante los fenómenos de El Niño, ya que la volatilidad es la norma.

- **El enfoque avanzado:** Al construir un modelo multivariado que ingeste simultáneamente las
  series de tiempo de caudales (aportes hídricos), la disponibilidad térmica y el precio horario,
  la red neuronal aprende el "régimen normal" del mercado dadas unas condiciones climáticas
  específicas. Cualquier desviación en el espacio latente reconstruido por un Autoencoder indicará
  una verdadera anomalía: posible manipulación de precios, retención de energía o estrés
  estructural severo.

Este código extrae el Precio de Bolsa Nacional y los Aportes Hídricos, los fusiona y construye un
Autoencoder recurrente con TensorFlow/Keras para identificar anomalías multivariadas basadas en la
reconstrucción del espacio latente.

<!-- prettier-ignore -->
```python
import datetime as dt
import pandas as pd
import numpy as np
from pydataxm.pydataxm import ReadDB
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, RepeatVector, TimeDistributed, Dense

# 1. Extracción de datos usando pydataxm
api = ReadDB()
start, end = dt.date(2025, 1, 1), dt.date(2025, 12, 31)

# Descargar las 3 variables fundamentales a nivel Sistema
df_precio = api.request_data('PrecBolsNaci', 'Sistema', start, end)
df_aportes = api.request_data('AporEner', 'Sistema', start, end)
df_generacion = api.request_data('Gene', 'Sistema', start, end) # <- Inclusión de Generación Real

# 2. Preprocesamiento: Limpieza y Fusión
# (En pydataxm, si los datos no están aplanados por hora, se debe hacer un melt previo)
# Renombramos la columna objetivo de cada dataset para diferenciarlas en el cruce
df_precio = df_precio.rename(columns={'Value': 'Precio'})
df_aportes = df_aportes.rename(columns={'Value': 'Aportes'})
df_generacion = df_generacion.rename(columns={'Value': 'Generacion'})

# Fusión secuencial de los 3 conjuntos de datos alineados por fecha
df_merged = pd.merge(df_precio[['Date', 'Precio']], df_aportes[['Date', 'Aportes']], on='Date', how='inner')
df_merged = pd.merge(df_merged, df_generacion[['Date', 'Generacion']], on='Date', how='inner')

# Extraer solo las variables numéricas y escalar (la forma ahora es N x 3)
features = df_merged[['Precio', 'Aportes', 'Generacion']].fillna(method='ffill')
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(features)

# Convertir a secuencias 3D para la LSTM (muestras, pasos temporales, características)
def create_sequences(X, time_steps):
    return np.array([X[i : (i + time_steps)] for i in range(len(X) - time_steps)])

time_steps = 24 # Ventana de evaluación (ej. 24 periodos)
X_seq = create_sequences(data_scaled, time_steps)
# Nota: X_seq.shape ahora devolverá (n_muestras, 24, 3)

# 3. Arquitectura LSTM Autoencoder
model = Sequential([
    # La capa de entrada se adapta dinámicamente a las 3 características (X_seq.shape[2])
    LSTM(64, activation='relu', input_shape=(X_seq.shape[1], X_seq.shape[2]), return_sequences=False),
    RepeatVector(X_seq.shape[1]),
    LSTM(64, activation='relu', return_sequences=True),
    TimeDistributed(Dense(X_seq.shape[2])) # La capa de salida reconstruye las 3 señales
])

model.compile(optimizer='adam', loss='mse')

# Entrenamiento del modelo
model.fit(X_seq, X_seq, epochs=15, batch_size=32, validation_split=0.1)

# 4. Detección de Anomalías Multivariadas
X_pred = model.predict(X_seq)

# Calculamos el Error Absoluto Medio (MAE) promediando a través de las 3 variables y la ventana temporal
mae_loss = np.mean(np.abs(X_pred - X_seq), axis=(1, 2))

# Marcar como anomalía los registros cuyo error de reconstrucción supera el percentil 95
umbrales_anomalia = mae_loss > np.percentile(mae_loss, 95)
```

### Prioridad 2: Fallas Topológicas y Poder de Mercado Espacial (Clustering Espacial)

Datasets a cruzar: Generación de Seguridad y Restricciones Operativas + Generación Real por Planta.
Técnicas recomendadas: Graph Neural Networks (GNNs) o Autoencoders Espacio-Temporales, clustering
de densidades (HDBSCAN).

<!-- prettier-ignore -->
| Nombre del dataset | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace directo al portal |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Generación Real por Planta y Recurso | Energía inyectada físicamente al SIN por cada unidad generadora (hídrica, térmica, solar, eólica).<br><br>Periodicidad: Horaria. | Análisis multivariado cruzando la declaración de disponibilidad técnica vs. la generación efectiva permite identificar outages encubiertos, fallas de máquinas u omisiones en el despacho ideal. | XM (supervisión de seguridad), Operadores de planta (mantenimiento predictivo basado en datos), Auditores regulatorios. | Garantiza la confiabilidad estructural del sistema eléctrico al verificar el cumplimiento de las Obligaciones de Energía Firme (OEF) del Cargo por Confiabilidad. | "Evaluation of Anomaly Detection of an Autoencoder Based on Maintenance Information and Scada-Data" (Elsevier, modelo extrapolable a operación hidroeléctrica local). | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |
| Generación de Seguridad y Restricciones Operativas | Energía que se despacha fuera de mérito económico para evitar fallas o aliviar congestiones, junto con su costo de remuneración.<br><br>Periodicidad: Horaria. | Anomalías en los sobrecostos de restricciones evidencian cuellos de botella emergentes, topologías de red críticas o abuso de posiciones dominantes zonales. Útil para algoritmos de clustering espacial. | Transmisores (justificación de planes de expansión), CREG y SSPD (mitigación de rentas de congestión). | Los costos por restricciones se trasladan directamente a la demanda. Picos anómalos incrementan drásticamente el Costo Unitario (CU) de prestación del servicio. | Implementaciones técnicas derivadas de la Resolución CREG 101-018 de 2023 sobre vigilancia de ofertas y evaluación del esquema de restricciones zonales. | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |

- **Por qué es de alta prioridad:** Los sobrecostos por restricciones no ocurren en el vacío;
  dependen de la topología de la red de transmisión y de qué plantas están despachando energía en
  qué nodos del país.

- **El enfoque avanzado:** Modelar esto como un grafo, donde los nodos son las
  plantas/subestaciones y las aristas son las líneas de transmisión. Las GNNs pueden detectar
  anomalías espaciales complejas, por ejemplo, cuando el comportamiento atípico en la generación de
  una planta específica dispara injustificadamente los costos de restricción en toda un área
  operativa (comportamiento estratégico fuera de mérito).

Este enfoque extrae datos con granularidad de Agente o Recurso para las restricciones y la
generación, utilizando HDBSCAN para encontrar comportamientos atípicos de costos
(sobre-remuneración fuera de mérito) sin presuponer distribuciones tradicionales.

<!-- prettier-ignore -->
```python
import datetime as dt
import pandas as pd
from pydataxm.pydataxm import ReadDB
from sklearn.cluster import HDBSCAN

api = ReadDB()
start, end = dt.date(2025, 1, 1), dt.date(2025, 12, 31)

# Descargar Costos de Restricciones y Generación por Agente/Recurso
df_restricciones = api.request_data('CostRest', 'Agente', start, end)
df_generacion = api.request_data('Gene', 'Agente', start, end)

# Agrupación por agente para extraer patrones de comportamiento
df_agentes = pd.merge(df_restricciones, df_generacion, on=['Date', 'Agente'], suffixes=('_costo', '_gen'))
X_agentes = df_agentes[['Value_costo', 'Value_gen']].fillna(0)

# Aplicar clustering basado en densidad (tolera ruido y varianza compleja)
# Agrupaciones pequeñas indicarán comportamientos zonales/espaciales atípicos
clusterer = HDBSCAN(min_cluster_size=10, metric='euclidean')
df_agentes['cluster_label'] = clusterer.fit_predict(X_agentes)

# Extraer anomalías explícitas (ruido = -1 en HDBSCAN)
anomalias_topologicas = df_agentes[df_agentes['cluster_label'] == -1]
```

### Prioridad 3: Limpieza de Señal y Fraude Comercial (Isolation Forest con Variables Calendario)

Datasets a cruzar: Demanda Comercial del SIN + Variables Calendario/Climáticas. Técnicas
recomendadas: Isolation Forests multivariados, Redes Neuronales Recurrentes (RNNs) con variables
exógenas.

<!-- prettier-ignore -->
| Nombre del dataset | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace directo al portal |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demanda Comercial del SIN | Consumo real de energía facturado por los comercializadores en distintas regiones del país.<br><br>Periodicidad: Horaria.| Exhibe marcada estacionalidad. La detección de outliers permite identificar tempranamente fallas en infraestructura de medida, incremento en pérdidas no técnicas (fraude) o choques macroeconómicos modelando covariables de calendario. | Distribuidores y Operadores de Red (balanceo de carga, control de pérdidas), XM (planeación operativa), Investigadores (pronóstico de demanda). | Es vital minimizar el error de pronóstico operativo y asegurar la precisión absoluta en la liquidación de cuentas y cargos del mercado por parte del ASIC. | Reportes de XM sobre desviaciones operativas vs. comerciales; múltiples tesis académicas en repositorios (ej. UNAL) sobre pronóstico y limpieza de demanda usando RNNs. | [Catálogo - Información Comercial](https://www.google.com/search?q=https://www.simem.co/datos/informacion-comercial) |

- **Por qué es prioridad media-alta:** La demanda eléctrica es fuertemente estacional. El principal
  reto analítico aquí es separar el ruido (efectos de fines de semana, festivos, olas de calor) de
  las verdaderas anomalías.

- **El enfoque avanzado:** Para establecer un punto de partida sólido, las herramientas orientadas
  al ajuste de distribuciones y pruebas estadísticas clásicas de outliers (usando el ecosistema de
  scipy.stats, distfit, numpy y pandas) funcionan excelente como línea base univariada.
  Posteriormente, se puede escalar a un modelo profundo que incorpore la estacionalidad como
  tensores de entrada para identificar caídas abruptas en el consumo que representen pérdidas no
  técnicas (fraude o robo de energía a gran escala) o fallas sistémicas de medición.

<!-- prettier-ignore -->
```python
import datetime as dt
import pandas as pd
from pydataxm.pydataxm import ReadDB
from sklearn.ensemble import IsolationForest

api = ReadDB()
start, end = dt.date(2025, 1, 1), dt.date(2025, 1, 31) # Mes de prueba

# Descargar Demanda Comercial Nacional
df_demanda = api.request_data('DemaCome', 'Sistema', start, end)

# Preprocesamiento: Extraer características temporales
# La API entrega horas en columnas o de forma plana; aquí asumimos un dataframe aplanado 
df_demanda['Date'] = pd.to_datetime(df_demanda['Date'])
df_demanda['hour'] = df_demanda['Date'].dt.hour
df_demanda['day_of_week'] = df_demanda['Date'].dt.dayofweek

X_demanda = df_demanda[['Value', 'hour', 'day_of_week']].dropna()

# Entrenar Isolation Forest
# Contamination es el porcentaje esperado de fraudes, caídas de telemetría o errores de facturación
iso_forest = IsolationForest(contamination=0.01, random_state=42)
df_demanda['anomaly_score'] = iso_forest.fit_predict(X_demanda)

# Filtrar las lecturas problemáticas (-1 indica anomalía)
lecturas_atipicas = df_demanda[df_demanda['anomaly_score'] == -1]
```

## deepseek

<!-- prettier-ignore -->
| **Nombre del dataset** | **Descripción breve** | **Relevancia para análisis de anomalías** | **Casos de uso prácticos** | **Importancia estratégica** | **Antecedentes de análisis similar** | **Enlace directo al dataset** |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Precio de Bolsa Nacional (Precio de bolsa horario)** | Precio de la energía en el mercado mayorista, resolución horaria, agregación nacional. Incluye precio promedio ponderado diario y horario, con periodicidad de actualización diaria. | Es el principal indicador de volatilidad del mercado. Permite detectar picos anómalos, manipulación de precios, comportamientos atípicos en horas de alta demanda o baja oferta, y cambios estructurales en la formación de precios. | Traders, generadores, comercializadores y reguladores. Permite optimizar estrategias de compra/venta, identificar oportunidades de arbitraje, y activar alertas regulatorias por posibles abusos de posición dominante. | Detectar anomalías en el precio de bolsa es crítico para la transparencia y eficiencia del mercado. Un precio anómalo puede indicar fallas en la operación, ejercicios de poder de mercado o errores en la programación económica, afectando directamente los costos de todos los agentes. | No se encontraron estudios públicos específicos de detección de anomalías sobre este dataset exacto. Sin embargo, el análisis de precios spot en mercados eléctricos es un campo ampliamente estudiado a nivel internacional; en Colombia, los informes de la Superintendencia de Servicios Públicos monitorean comportamientos elevados del precio de bolsa. | `https://www.simem.co/backend-files/api/PublicData?datasetId=8d10e6` |
| **Demanda Real del SIN (Demanda horaria del Sistema Interconectado Nacional)** | Demanda real de energía del SIN, con resolución horaria y cobertura nacional. Incluye demanda regulada y no regulada, y se actualiza diariamente. | Serie temporal con estacionalidad diaria, semanal y anual. Anomalías pueden reflejar fraudes masivos, errores de medición, eventos climáticos extremos, fallas en la comunicación de datos o cambios inesperados en el consumo industrial. Es ideal para modelos multivariados (demanda por región + clima) y aprendizaje profundo (autoencoders, LSTM). | Distribuidoras, comercializadoras, reguladores (CREG, SSPD) e investigadores. Permite detectar pérdidas no técnicas, validar proyecciones de demanda, y activar planes de contingencia ante caídas o picos atípicos de consumo. | La demanda es la variable base para la planeación operativa y la expansión del sistema. Detectar anomalías a tiempo evita desbalances, sobrecostos por compra en bolsa y riesgos de racionamiento. Además, anomalías persistentes pueden indicar problemas estructurales de eficiencia energética. | Existe un estudio colombiano que utiliza datos de demanda horaria del SIN para detección de anomalías: **“PILOTO AMIs: detección de anomalías en series de tiempo de consumo de energía eléctrica de usuarios residenciales”**. También se ha trabajado en pronóstico de carga horaria con datos de SIMEM. | `https://www.simem.co/backend-files/api/PublicData?datasetId=e007fb` |
| **Generación Real por Planta** | Energía neta generada por cada central del sistema, con resolución horaria. Incluye generación por tipo de combustible y agente propietario, y se publica con desagregación por planta. | Permite detectar anomalías operativas: caídas súbitas de generación, desviaciones entre generación programada y real, comportamiento atípico de plantas térmicas o hidráulicas, y posibles fallas de equipos. Es un dataset multivariado natural (múltiples plantas × tiempo) y adecuado para deep learning (series multivariadas). | Generadores, Centro Nacional de Despacho (CND), reguladores e investigadores. Facilita mantenimiento predictivo, verificación de cumplimiento de despacho, y detección temprana de indisponibilidades no reportadas. | La generación real es el insumo directo para el balance oferta-demanda. Anomalías no detectadas pueden derivar en incumplimientos, sanciones, y riesgo para la estabilidad del sistema. Su monitoreo es clave para la confiabilidad del SIN. | No se encontraron papers públicos que utilicen específicamente este dataset para detección de anomalías. Sin embargo, la literatura sobre detección de fallas en plantas de generación es extensa, y los datos de generación real de SIMEM son la fuente primaria para dichos análisis en Colombia. | `https://www.simem.co/backend-files/api/PublicData?datasetId=E17D25` |
| **Aportes Hídricos a Embalses** | Caudal o energía aportada a los embalses del sistema, con resolución diaria o semanal. Es la variable hidrológica fundamental para la operación del sistema hidro-térmico colombiano. | Los aportes hídricos presentan alta variabilidad climática (eventos El Niño/La Niña). Anomalías pueden indicar sequías severas, errores de medición, o cambios en el régimen hidrológico. Su análisis univariado y multivariado (junto con nivel de embalses y generación hidráulica) es crucial para modelos de deep learning que capturen dependencias temporales largas. | Operadores del sistema (XM), generadores hidroeléctricos, reguladores (CREG, UPME), y analistas de riesgo. Permite anticipar riesgos de desabastecimiento, ajustar estrategias de generación, y activar mecanismos de cargo por confiabilidad. | Colombia depende mayoritariamente de la generación hidroeléctrica. Detectar anomalías en los aportes hídricos es estratégico para la seguridad energética, la planeación de largo plazo y la gestión de riesgos climáticos. | No se hallaron estudios públicos de detección de anomalías específicamente sobre este dataset en SIMEM. Sin embargo, los informes de XM y la UPME monitorean continuamente los aportes hídricos para alertar sobre condiciones críticas. | Disponible a través del catálogo de SIMEM (búsqueda por “aportes hídricos” o “hidrología”). |
| **Disponibilidad de Plantas de Generación (Indisponibilidad)** | Horas de indisponibilidad programada y no programada de cada unidad de generación del SIN, con resolución horaria o diaria. Incluye causa de la indisponibilidad (mantenimiento, falla, etc.). | Es un dataset ideal para detección de anomalías operativas: indisponibilidades no planificadas, patrones repetitivos de falla en ciertas plantas, correlación entre indisponibilidad y variables climáticas o de mercado. Su estructura multivariada (planta × tiempo × causa) lo hace apto para técnicas de deep learning como autoencoders o transformers. | Generadores, CND, reguladores, y aseguradoras del sector. Permite identificar equipos problemáticos, optimizar planes de mantenimiento, y evaluar el impacto de las indisponibilidades en la seguridad del sistema. | La disponibilidad del parque generador es determinante para la confiabilidad del suministro. Anomalías no gestionadas pueden provocar déficit de generación, precios altos y riesgos de racionamiento. Su análisis proactivo mejora la resiliencia del sistema. | No se encontraron estudios públicos de detección de anomalías aplicados a este dataset específico. Sin embargo, los informes de auditoría del MEM y los boletines de la SSPD analizan patrones de indisponibilidad. | Disponible a través del catálogo de SIMEM (búsqueda por “disponibilidad” o “indisponibilidad”). |

<!-- prettier-ignore -->
| Prioridad | Dataset | Estructura de datos | Complejidad temporal | Potencial de anomalías | Encaje con modelos avanzados | Justificación de prioridad |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Generación Real por Planta | Multivariado natural: N plantas × T horas × tipo de combustible (matriz de alta dimensión). Cada planta es una serie temporal con dinámica propia, y las correlaciones entre plantas capturan relaciones espaciales (congestión, despacho). | Alta: estacionalidad horaria, semanal y anual, más efectos de mantenimiento, hidrología y precio. Series no estacionarias con regímenes operativos cambiantes. | Muy alto: caídas súbitas de generación, desviaciones entre generación programada y real, fallas de equipos, indisponibilidades no reportadas. Anomalías que se propagan entre plantas por restricciones de red. | Excelente. LSTM multivariado, autoencoders (AE) sobre matrices planta×hora, transformers para capturar dependencias entre plantas, graph neural networks (GNN) para relaciones topológicas. La estructura N×T permite reconstrucción multivariada con error de reconstrucción como señal de anomalía. | Es el dataset con mayor dimensionalidad y riqueza estructural del SIMEM. Permite formular el problema como detección de anomalías en series multivariadas con dependencias cruzadas, que es exactamente el escenario donde los modelos profundos superan a los métodos univariados. Además, hay precedentes metodológicos directos en plantas hidroeléctricas colombianas. |
| 2 | Precio de Bolsa Nacional (horario) | Univariado en su forma básica, pero fácilmente multivariado al incorporar variables exógenas: demanda, generación, aportes hídricos, disponibilidad. La serie horaria tiene alta frecuencia y muchos valores atípicos. | Muy alta: resolución horaria, con picos extremos, cambios de régimen y efectos de mercado (ofertas, contratos). No estacionaria con clustering de volatilidad. | Muy alto: picos anómalos, manipulación de precios, comportamientos atípicos en horas de alta demanda/baja oferta, cambios estructurales en formación de precios. Es la variable más crítica para la transparencia del mercado. | Excelente. LSTM/GRU para capturar dependencias temporales largas, autoencoders variacionales (VAE) para detección de anomalías en precios, CNN-LSTM híbridos para extraer patrones espacio-temporales, isolation forests como baseline. | Aunque univariado en origen, su valor para deep learning explota al integrarlo con otros datasets (demanda, generación, aportes). El Banco de la República ya desarrolló una metodología de detección de anomalías en ofertas de agentes pivotales usando machine learning, lo que valida la aproximación y su relevancia regulatoria. |
| 3 | Demanda Real del SIN (horaria) | Multivariado al desagregar por región, tipo de usuario (regulado/no regulado) y al cruzar con clima. La serie horaria nacional es la agregación de múltiples series con dinámicas distintas. | Alta: estacionalidad diaria, semanal, anual y efectos climáticos. La demanda responde a temperatura, días festivos y eventos macroeconómicos. | Alto: fraudes masivos, errores de medición, caídas o picos atípicos de consumo industrial, cambios inesperados en patrones regionales. Las anomalías suelen ser persistentes y localizadas. | Muy bueno. Autoencoders para detección de desviaciones en perfiles horarios, LSTM multivariado para capturar dependencias entre regiones, modelos de reconstrucción con ventanas temporales. La literatura reporta AE+BiLSTM con F1 de 93.89% en datos de consumo eléctrico. | Es la variable base para planeación operativa. Los estudios colombianos ya han aplicado análisis de subestaciones con AMI, identificando ~4% de subestaciones como outliers. La granularidad horaria y la desagregación regional ofrecen suficiente complejidad para modelos profundos. |
| 4 | Aportes Hídricos a Embalses | Multivariado natural: N embalses × T días/semanas. Cada embalse tiene una cuenca con dinámica hidrológica propia, y las correlaciones entre embalses capturan patrones climáticos regionales (ENSO). | Media-alta: resolución diaria/semanal con estacionalidad anual y efectos de ENSO (El Niño/La Niña). Series con autocorrelación fuerte y cambios de régimen climático. | Alto: sequías severas, errores de medición, cambios en el régimen hidrológico, anomalías asociadas a ENSO. El Niño produce anomalías negativas significativas en caudales de embalses colombianos. | Muy bueno. LSTM multivariado para capturar dependencias entre embalses, autoencoders para reconstrucción de series hidrológicas, modelos con variables exógenas (índices ENSO). La estructura embalse×tiempo es ideal para deep learning. | Colombia depende mayoritariamente de generación hidroeléctrica. La literatura confirma que ENSO produce cambios estadísticamente significativos en la distribución de caudales diarios en 15 embalses colombianos. Detectar anomalías aquí es estratégico para la seguridad energética. |
| 5 | Disponibilidad de Plantas de Generación (Indisponibilidad) | Multivariado: planta × tiempo × causa de indisponibilidad (mantenimiento, falla, etc.). Es una matriz dispersa con eventos binarios o conteos de horas. | Media: resolución horaria o diaria, con patrones de mantenimiento programado y fallas no programadas. Los eventos son relativamente raros (desbalance de clases). | Alto: indisponibilidades no planificadas, patrones repetitivos de falla en ciertas plantas, correlación entre indisponibilidad y variables climáticas o de mercado. Anomalías que impactan directamente la seguridad del sistema. | Bueno. Autoencoders para detectar patrones inusuales de indisponibilidad, LSTM para predecir fallas, modelos de clasificación con técnicas de balanceo (SMOTE) para eventos raros. La estructura planta×causa×tiempo permite representaciones ricas. | Es un dataset con alta relevancia operativa pero menor volumen y mayor desbalance de clases que los anteriores. Su inclusión como quinta prioridad se justifica porque las anomalías en disponibilidad tienen impacto directo en la confiabilidad del SIN y complementan el análisis de generación real. La combinación de ambas permite distinguir entre anomalías de generación por mérito económico vs. fallas técnicas. |

### Configuración inicial

<!-- prettier-ignore -->
```python
# Instalación de dependencias
!pip install pydataxm pandas numpy scikit-learn matplotlib seaborn tensorflow

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pydataxm.pydatasimem import ReadSIMEM, CatalogSIMEM
import warnings
warnings.filterwarnings('ignore')

# Función auxiliar para extraer datos de SIMEM
def extraer_simem(dataset_id, fecha_inicio, fecha_final, filter=False):
    """
    Extrae datos de un dataset de SIMEM.
    """
    simem = ReadSIMEM(dataset_id=dataset_id, start_date=fecha_inicio, end_date=fecha_final)
    df = simem.main(filter=filter)
    return df
```

### PRIORIDAD 1: Generación Real por Planta

Dataset ID: `E17D25`

Descripción: Energía neta generada por cada central del SIN, resolución horaria, desagregada por
planta y tipo de combustible.

<!-- prettier-ignore -->
```python
# ============================================================
# PRIORIDAD 1: GENERACIÓN REAL POR PLANTA
# ============================================================

dataset_id = 'E17D25'
fecha_inicio = '2024-01-01'
fecha_final = '2024-12-31'

df_generacion = extraer_simem(dataset_id, fecha_inicio, fecha_final)

# Preprocesamiento: pivotear para obtener matriz planta × hora
df_pivot = df_generacion.pivot_table(
    index='FechaHora',
    columns='NombrePlanta',
    values='GeneracionReal',
    aggfunc='sum'
).fillna(0)

print(f"Matriz: {df_pivot.shape[0]} horas × {df_pivot.shape[1]} plantas")

# Normalización por planta (z-score)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_pivot)

# ============================================================
# DETECCIÓN DE ANOMALÍAS MULTIVARIADA CON AUTOENCODER
# ============================================================

from tensorflow.keras import layers, Model

# Definir autoencoder
input_dim = X_scaled.shape[1]
encoding_dim = max(8, input_dim // 4)

input_layer = layers.Input(shape=(input_dim,))
encoded = layers.Dense(encoding_dim * 2, activation='relu')(input_layer)
encoded = layers.Dense(encoding_dim, activation='relu')(encoded)
decoded = layers.Dense(encoding_dim * 2, activation='relu')(encoded)
decoded = layers.Dense(input_dim, activation='linear')(decoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Entrenar
history = autoencoder.fit(
    X_scaled, X_scaled,
    epochs=50,
    batch_size=256,
    validation_split=0.1,
    verbose=0
)

# Reconstrucción y error
X_pred = autoencoder.predict(X_scaled)
reconstruction_error = np.mean(np.square(X_scaled - X_pred), axis=1)

# Umbral basado en percentil 99
umbral = np.percentile(reconstruction_error, 99)
anomalias = reconstruction_error > umbral

print(f"Anomalías detectadas: {anomalias.sum()} de {len(anomalias)} horas ({anomalias.mean()*100:.2f}%)")

# Visualización
plt.figure(figsize=(14, 5))
plt.plot(df_pivot.index, reconstruction_error, label='Error de reconstrucción', alpha=0.7)
plt.axhline(umbral, color='r', linestyle='--', label=f'Umbral (P99) = {umbral:.4f}')
plt.scatter(df_pivot.index[anomalias], reconstruction_error[anomalias],
            color='red', s=20, label='Anomalías', zorder=5)
plt.title('Detección de Anomalías - Generación Real por Planta (Autoencoder)')
plt.xlabel('Fecha')
plt.ylabel('Error MSE')
plt.legend()
plt.tight_layout()
plt.show()

# Anomalías por planta
df_anomalias = pd.DataFrame({
    'FechaHora': df_pivot.index[anomalias],
    'Error_Reconstruccion': reconstruction_error[anomalias]
})
print(df_anomalias.head(10))
```

### PRIORIDAD 2: Precio de Bolsa Nacional

Dataset ID: `8d10e6`

Descripción: Precio horario de la energía en el mercado mayorista colombiano.

<!-- prettier-ignore -->
```python
# ============================================================
# PRIORIDAD 2: PRECIO DE BOLSA NACIONAL (HORARIO)
# ============================================================

dataset_id = '8d10e6'
fecha_inicio = '2024-01-01'
fecha_final = '2024-12-31'

df_precio = extraer_simem(dataset_id, fecha_inicio, fecha_final)

# Serie temporal univariada
serie_precio = df_precio.set_index('FechaHora')['PrecioBolsa'].sort_index()

print(f"Serie: {len(serie_precio)} observaciones horarias")
print(serie_precio.describe())

# ============================================================
# DETECCIÓN DE ANOMALÍAS CON LSTM (AUTOENCODER SECUENCIAL)
# ============================================================

# Crear ventanas temporales (por ejemplo, 24 horas)
def crear_ventanas(serie, window_size=24):
    X = []
    for i in range(len(serie) - window_size):
        X.append(serie[i:i + window_size])
    return np.array(X)

window_size = 24
X_seq = crear_ventanas(serie_precio.values, window_size)

# Normalizar
scaler_seq = StandardScaler()
X_seq_flat = X_seq.reshape(-1, 1)
X_seq_scaled = scaler_seq.fit_transform(X_seq_flat).reshape(X_seq.shape)

# LSTM Autoencoder
input_seq = layers.Input(shape=(window_size, 1))
encoded = layers.LSTM(32, activation='relu', return_sequences=True)(input_seq)
encoded = layers.LSTM(16, activation='relu', return_sequences=False)(encoded)
decoded = layers.RepeatVector(window_size)(encoded)
decoded = layers.LSTM(16, activation='relu', return_sequences=True)(decoded)
decoded = layers.LSTM(32, activation='relu', return_sequences=True)(decoded)
output_seq = layers.TimeDistributed(layers.Dense(1))(decoded)

lstm_ae = Model(input_seq, output_seq)
lstm_ae.compile(optimizer='adam', loss='mse')

# Entrenar
lstm_ae.fit(
    X_seq_scaled, X_seq_scaled,
    epochs=40,
    batch_size=64,
    validation_split=0.1,
    verbose=0
)

# Error de reconstrucción por ventana
X_seq_pred = lstm_ae.predict(X_seq_scaled)
error_seq = np.mean(np.square(X_seq_scaled - X_seq_pred), axis=(1, 2))

# Anomalías: ventanas con error > percentil 95
umbral_seq = np.percentile(error_seq, 95)
anomalias_seq = error_seq > umbral_seq

print(f"Ventanas anómalas: {anomalias_seq.sum()} de {len(anomalias_seq)}")

# Visualización
plt.figure(figsize=(14, 5))
plt.plot(error_seq, label='Error de reconstrucción LSTM', alpha=0.7)
plt.axhline(umbral_seq, color='r', linestyle='--', label=f'Umbral (P95) = {umbral_seq:.4f}')
plt.scatter(np.where(anomalias_seq)[0], error_seq[anomalias_seq],
            color='red', s=20, label='Anomalías', zorder=5)
plt.title('Detección de Anomalías en Precio de Bolsa - LSTM Autoencoder')
plt.xlabel('Índice de ventana temporal (24h)')
plt.ylabel('Error MSE')
plt.legend()
plt.tight_layout()
plt.show()
```

### PRIORIDAD 3: Demanda Real del SIN

Dataset ID: `e007fb`

Descripción: Demanda horaria del Sistema Interconectado Nacional.

<!-- prettier-ignore -->
```python
# ============================================================
# PRIORIDAD 3: DEMANDA REAL DEL SIN (HORARIA)
# ============================================================

dataset_id = 'e007fb'
fecha_inicio = '2024-01-01'
fecha_final = '2024-12-31'

df_demanda = extraer_simem(dataset_id, fecha_inicio, fecha_final)

# Serie temporal
serie_demanda = df_demanda.set_index('FechaHora')['DemandaReal'].sort_index()

print(f"Serie: {len(serie_demanda)} observaciones horarias")
print(serie_demanda.describe())

# ============================================================
# DETECCIÓN DE ANOMALÍAS CON AUTOENCODER + BILSTM
# ============================================================

from tensorflow.keras import backend as K

# Preparar datos secuenciales
window_size = 48  # 2 días de historial
X_dem = crear_ventanas(serie_demanda.values, window_size)

scaler_dem = StandardScaler()
X_dem_flat = X_dem.reshape(-1, 1)
X_dem_scaled = scaler_dem.fit_transform(X_dem_flat).reshape(X_dem.shape)

# Modelo Autoencoder con Bidirectional LSTM
input_dem = layers.Input(shape=(window_size, 1))
encoded_dem = layers.Bidirectional(layers.LSTM(32, activation='relu'))(input_dem)
encoded_dem = layers.Dense(16, activation='relu')(encoded_dem)
decoded_dem = layers.RepeatVector(window_size)(encoded_dem)
decoded_dem = layers.Bidirectional(layers.LSTM(32, activation='relu', return_sequences=True))(decoded_dem)
output_dem = layers.TimeDistributed(layers.Dense(1))(decoded_dem)

ae_demanda = Model(input_dem, output_dem)
ae_demanda.compile(optimizer='adam', loss='mse')

# Entrenar
ae_demanda.fit(
    X_dem_scaled, X_dem_scaled,
    epochs=40,
    batch_size=64,
    validation_split=0.1,
    verbose=0
)

# Error de reconstrucción
X_dem_pred = ae_demanda.predict(X_dem_scaled)
error_dem = np.mean(np.square(X_dem_scaled - X_dem_pred), axis=(1, 2))

umbral_dem = np.percentile(error_dem, 95)
anomalias_dem = error_dem > umbral_dem

print(f"Ventanas anómalas: {anomalias_dem.sum()} de {len(anomalias_dem)} ({anomalias_dem.mean()*100:.2f}%)")

# Visualización
plt.figure(figsize=(14, 5))
plt.plot(error_dem, label='Error de reconstrucción BiLSTM', alpha=0.7)
plt.axhline(umbral_dem, color='r', linestyle='--', label=f'Umbral (P95)')
plt.scatter(np.where(anomalias_dem)[0], error_dem[anomalias_dem],
            color='red', s=20, label='Anomalías', zorder=5)
plt.title('Detección de Anomalías en Demanda Real del SIN - BiLSTM Autoencoder')
plt.xlabel('Ventana temporal (48h)')
plt.ylabel('Error MSE')
plt.legend()
plt.tight_layout()
plt.show()
```

### PRIORIDAD 4: Aportes Hídricos a Embalses

Dataset ID: Se obtiene del catálogo de SIMEM

Descripción: Caudal o energía aportada a los embalses del sistema.

<!-- prettier-ignore -->
```python
# ============================================================
# PRIORIDAD 4: APORTES HÍDRICOS A EMBALSES
# ============================================================

# Primero, buscar el dataset ID en el catálogo
catalogo = CatalogSIMEM('Datasets')
df_catalogo = catalogo.get_data()

# Buscar datasets relacionados con aportes hídricos
datasets_hidricos = df_catalogo[
    df_catalogo['nombreConjuntoDatos'].str.contains('Aporte|Hídrico|Embalse', case=False, na=False)
]
print(datasets_hidricos[['idConjuntoDatos', 'nombreConjuntoDatos']].to_string())

# Una vez identificado el ID, extraer datos
dataset_id_hidrico = datasets_hidricos.iloc[0]['idConjuntoDatos']  # Ajustar según resultado
fecha_inicio = '2023-01-01'
fecha_final = '2024-12-31'

df_aportes = extraer_simem(dataset_id_hidrico, fecha_inicio, fecha_final)

# Pivotear: embalse × tiempo
df_aportes_pivot = df_aportes.pivot_table(
    index='Fecha',
    columns='NombreEmbalse',
    values='AporteHidrico',
    aggfunc='sum'
).fillna(method='ffill')

print(f"Matriz: {df_aportes_pivot.shape[0]} días × {df_aportes_pivot.shape[1]} embalses")

# ============================================================
# DETECCIÓN DE ANOMALÍAS CON AUTOENCODER MULTIVARIADO
# ============================================================

scaler_hid = StandardScaler()
X_hid = scaler_hid.fit_transform(df_aportes_pivot)

input_hid = layers.Input(shape=(X_hid.shape[1],))
encoded_hid = layers.Dense(32, activation='relu')(input_hid)
encoded_hid = layers.Dense(16, activation='relu')(encoded_hid)
decoded_hid = layers.Dense(32, activation='relu')(encoded_hid)
decoded_hid = layers.Dense(X_hid.shape[1], activation='linear')(decoded_hid)

ae_hidrico = Model(input_hid, decoded_hid)
ae_hidrico.compile(optimizer='adam', loss='mse')

ae_hidrico.fit(X_hid, X_hid, epochs=50, batch_size=32, validation_split=0.1, verbose=0)

X_hid_pred = ae_hidrico.predict(X_hid)
error_hid = np.mean(np.square(X_hid - X_hid_pred), axis=1)

umbral_hid = np.percentile(error_hid, 98)
anomalias_hid = error_hid > umbral_hid

print(f"Anomalías detectadas: {anomalias_hid.sum()} de {len(anomalias_hid)} días ({anomalias_hid.mean()*100:.2f}%)")

# Visualización
plt.figure(figsize=(14, 5))
plt.plot(df_aportes_pivot.index, error_hid, label='Error de reconstrucción', alpha=0.7)
plt.axhline(umbral_hid, color='r', linestyle='--', label=f'Umbral (P98)')
plt.scatter(df_aportes_pivot.index[anomalias_hid], error_hid[anomalias_hid],
            color='red', s=20, label='Anomalías', zorder=5)
plt.title('Detección de Anomalías - Aportes Hídricos a Embalses')
plt.xlabel('Fecha')
plt.ylabel('Error MSE')
plt.legend()
plt.tight_layout()
plt.show()
```

### PRIORIDAD 5: Disponibilidad de Plantas de Generación

Dataset ID: `Disponibilidad comercial por planta` (disponible en datos.gov.co)

Descripción: Horas de indisponibilidad programada y no programada de cada unidad de generación.

<!-- prettier-ignore -->
```python
# ============================================================
# PRIORIDAD 5: DISPONIBILIDAD DE PLANTAS DE GENERACIÓN
# ============================================================

# Buscar dataset de disponibilidad en el catálogo
datasets_disp = df_catalogo[
    df_catalogo['nombreConjuntoDatos'].str.contains('Disponibilidad', case=False, na=False)
]
print(datasets_disp[['idConjuntoDatos', 'nombreConjuntoDatos']].to_string())

# Extraer datos (ajustar ID según resultado)
dataset_id_disp = datasets_disp.iloc[0]['idConjuntoDatos']
fecha_inicio = '2024-01-01'
fecha_final = '2024-12-31'

df_disp = extraer_simem(dataset_id_disp, fecha_inicio, fecha_final)

# Pivotear: planta × tiempo
df_disp_pivot = df_disp.pivot_table(
    index='FechaHora',
    columns='NombrePlanta',
    values='DisponibilidadComercial',
    aggfunc='sum'
).fillna(0)

print(f"Matriz: {df_disp_pivot.shape[0]} horas × {df_disp_pivot.shape[1]} plantas")

# ============================================================
# DETECCIÓN DE ANOMALÍAS CON ISOLATION FOREST (BASELINE)
# ============================================================

from sklearn.ensemble import IsolationForest

# Isolation Forest es robusto para datos de alta dimensionalidad y desbalanceados
iso_forest = IsolationForest(
    contamination=0.05,  # 5% de anomalías esperadas
    random_state=42,
    n_estimators=200
)

# Entrenar sobre la matriz planta × hora
predicciones = iso_forest.fit_predict(df_disp_pivot)

# -1 indica anomalía, 1 indica normal
anomalias_disp = predicciones == -1

print(f"Anomalías detectadas: {anomalias_disp.sum()} de {len(anomalias_disp)} horas ({anomalias_disp.mean()*100:.2f}%)")

# Score de anomalía
scores = iso_forest.decision_function(df_disp_pivot)

# Visualización
plt.figure(figsize=(14, 5))
plt.plot(df_disp_pivot.index, scores, label='Score de anomalía (Isolation Forest)', alpha=0.7)
plt.axhline(0, color='r', linestyle='--', label='Umbral de decisión')
plt.scatter(df_disp_pivot.index[anomalias_disp], scores[anomalias_disp],
            color='red', s=20, label='Anomalías', zorder=5)
plt.title('Detección de Anomalías - Disponibilidad de Plantas (Isolation Forest)')
plt.xlabel('Fecha')
plt.ylabel('Score de anomalía')
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# DEEP LEARNING COMPLEMENTARIO: AUTOENCODER
# ============================================================

scaler_disp = StandardScaler()
X_disp = scaler_disp.fit_transform(df_disp_pivot)

input_disp = layers.Input(shape=(X_disp.shape[1],))
encoded_disp = layers.Dense(32, activation='relu')(input_disp)
encoded_disp = layers.Dense(16, activation='relu')(encoded_disp)
decoded_disp = layers.Dense(32, activation='relu')(encoded_disp)
decoded_disp = layers.Dense(X_disp.shape[1], activation='linear')(decoded_disp)

ae_disp = Model(input_disp, decoded_disp)
ae_disp.compile(optimizer='adam', loss='mse')

ae_disp.fit(X_disp, X_disp, epochs=50, batch_size=64, validation_split=0.1, verbose=0)

X_disp_pred = ae_disp.predict(X_disp)
error_disp = np.mean(np.square(X_disp - X_disp_pred), axis=1)

umbral_disp = np.percentile(error_disp, 95)
anomalias_ae_disp = error_disp > umbral_disp

print(f"Anomalías por Autoencoder: {anomalias_ae_disp.sum()} de {len(anomalias_ae_disp)}")
```

### Resumen de datasets y técnicas aplicadas

<!-- prettier-ignore -->
| Prioridad | Dataset | Dataset ID | Técnica principal | Tipo de anomalía detectada |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Generación Real por Planta | `E17D25` | Autoencoder multivariado | Caídas de generación, fallas de equipos |
| 2 | Precio de Bolsa Nacional | `8d10e6` | LSTM Autoencoder secuencial | Picos de volatilidad, manipulación |
| 3 | Demanda Real del SIN | `e007fb` | BiLSTM Autoencoder | Fraudes, errores de medición, picos atípicos |
| 4 | Aportes Hídricos a Embalses | Catálogo SIMEM | Autoencoder multivariado | Sequías, errores hidrológicos |
| 5 | Disponibilidad de Plantas | [datos.gov.co](https://datos.gov.co) | Isolation Forest + Autoencoder | Indisponibilidades no planificadas |

Notas de implementación

1. **Librería oficial:** Todos los ejemplos utilizan pydataxm, la librería oficial de XM para
   consumir la API de SIMEM.

2. **Dataset IDs:** Los IDs proporcionados (E17D25, 8d10e6, e007fb) son los identificadores
   oficiales de SIMEM para generación real, precio de bolsa y demanda, respectivamente.

3. **Restricciones de la API:** La API de SIMEM tiene límites de consulta por rango de fechas; para
   períodos extensos, la librería pydataxm maneja automáticamente la consolidación de datos.

4. **Ajuste de hiperparámetros:** Los valores de window_size, encoding_dim, contamination y
   percentiles de umbral deben calibrarse según el dataset específico y el nivel de sensibilidad
   deseado.

5. **Escalabilidad:** Para datasets de alta dimensionalidad (más de 100 plantas), se recomienda
   usar ventanas temporales más largas y arquitecturas más profundas, o migrar a modelos tipo
   Transformer.

## Copilot

<!-- prettier-ignore -->
| Dataset (SIMEM) | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace en SIMEM |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Precio de Bolsa Nacional de Energía | Serie temporal horaria del precio spot del Mercado de Energía Mayorista (MEM). Granularidad: hora. Cobertura histórica de varios años. Disponible dentro de los conjuntos de datos de información comercial del SIMEM. [simem.co](https://www.simem.co/), [simem.co](https://www.simem.co/backend-files/swagger/v1/swagger.json) | Ideal para detección de price spikes, eventos extremos, cambios de régimen, comportamientos especulativos, impactos climáticos y fallas operativas. Permite enfoques univariados (outliers de precio), multivariados (precio + demanda + generación + hidrología) y deep learning (LSTM, Autoencoders, Transformers). | Traders energéticos, generadores, comercializadores, XM, reguladores y analistas de riesgo. Permite mejorar coberturas, estrategias de despacho, señales de alerta temprana y gestión del portafolio. | El precio de bolsa es una señal central para el funcionamiento del mercado colombiano; anomalías sostenidas pueden anticipar estrés de abastecimiento o riesgos regulatorios. | Existen numerosos estudios sobre detección de anomalías y pronóstico de precios eléctricos en mercados spot, incluidos mercados hidrodominados comparables al colombiano. No se identificó evidencia pública de un paper dedicado específicamente al dataset SIMEM con ese nombre. | Portal SIMEM: https://www.simem.co → categoría Información comercial. [simem.co] |
| Demanda de Energía del SIN (Sistema Interconectado Nacional) | Demanda eléctrica agregada con resolución horaria y series históricas. Mide consumo total del SIN y, en algunas variantes, demanda por agente o mercado. Relacionado con operación y liquidación del mercado. [simem.co] | Permite detectar caídas abruptas de consumo, errores de medición, eventos climáticos, interrupciones regionales, cambios estructurales y comportamientos atípicos de carga. Excelente para modelos multivariados con clima, precios y generación. | Operadores de red, comercializadores, distribuidores, planeadores energéticos e investigadores. Mejora predicción de carga y monitoreo operacional. | La demanda es la variable fundamental para garantizar confiabilidad y suficiencia energética. Detectar anomalías ayuda a prevenir desequilibrios entre oferta y demanda. | Amplia literatura internacional sobre anomalías en curvas de carga mediante Isolation Forest, Autoencoders y LSTM. No se encontró referencia pública específica para este dataset SIMEM. | Portal SIMEM: https://www.simem.co → categorías de Operación del SIN e Información comercial. [simem.co] |
| Generación Real por Planta o Recurso de Generación | Producción de energía reportada por unidades generadoras del SIN. Resolución horaria; granularidad por planta, recurso o agente. Pertenece a los datos operativos usados para coordinación y operación del sistema. [simem.co] | Permite detectar fallas operativas, degradación de equipos, indisponibilidades no reportadas, desviaciones frente al programa de generación y comportamientos inusuales entre tecnologías. Muy adecuado para detección multivariada. | Generadores, XM, aseguradores, inversionistas y áreas de mantenimiento predictivo. | Las anomalías pueden indicar riesgos de confiabilidad, pérdidas económicas o incumplimientos operativos. | Existen numerosos estudios en generación hidroeléctrica y térmica usando Autoencoders, redes recurrentes y detección basada en series temporales. No se encontró evidencia pública específica para el conjunto de datos SIMEM. | Portal SIMEM: https://www.simem.co → Operación del Sistema Interconectado Nacional (SIN). [simem.co] |
| Aportes Hidrológicos / Variables Hidrológicas para Generación | Registra aportes hídricos y variables asociadas al recurso hidráulico utilizado por el parque hidroeléctrico colombiano. Generalmente con frecuencia diaria u horaria según la variable. Forma parte de la información operativa utilizada en la planeación del SIN. [simem.co] | Las anomalías pueden reflejar fenómenos climáticos, errores de sensado, impactos de El Niño o La Niña y condiciones extremas de disponibilidad hídrica. Presenta alta no linealidad, favorable para deep learning. | Generadores hidroeléctricos, XM, UPME, investigadores climáticos y gestores de riesgo energético. | Colombia posee una matriz fuertemente dependiente de recursos hídricos; anomalías hidrológicas tienen efectos directos sobre precios, confiabilidad y seguridad energética. | Existe abundante literatura sobre detección de anomalías hidrológicas y monitoreo hidroenergético, aunque no se identificó un estudio público específico sobre el dataset SIMEM. | Portal SIMEM: https://www.simem.co → Operación del SIN. [simem.co] |
| Histórico de Eventos en Activos de Transmisión del Sistema de Transmisión Nacional (STN) | Registro histórico de eventos, fallas e intervenciones en activos de transmisión. Dataset destacado dentro de Operación del SIN. [simem.co] | Permite identificar patrones atípicos de fallas, clusters de eventos, degradación de infraestructura y eventos raros de alta criticidad. Puede modelarse mediante secuencias temporales, grafos o detección de anomalías sobre redes. | Transportadores, XM, reguladores, operadores de red y equipos de mantenimiento. | Una anomalía en transmisión puede propagarse al sistema completo y afectar confiabilidad y calidad del servicio. | Existen estudios internacionales de detección temprana de fallas en redes eléctricas mediante machine learning y deep learning; no se encontró evidencia pública específica del dataset SIMEM. | Portal SIMEM: https://www.simem.co (dataset destacado: “Histórico de eventos en Activos de Transmisión del Sistema de Transmisión Nacional”). [simem.co] |
| Excedentes Negativos por Comercializador | Dataset comercial publicado por SIMEM que resume excedentes negativos asociados a comercializadores del MEM. Actualizado dentro de la categoría Información Comercial. [simem.co] | Útil para identificar comportamientos financieros o comerciales atípicos, errores de nominación, desviaciones frente a contratos y riesgos de mercado. | Comercializadores, reguladores, áreas de riesgo y auditoría, consultores del mercado eléctrico. | Permite monitorear desbalances y potenciales señales tempranas de deterioro financiero u operacional de agentes. | No se identificaron trabajos académicos públicos específicos sobre este dataset; representa una oportunidad de investigación aplicada para detección de anomalías financieras en mercados eléctricos. | Portal SIMEM: https://www.simem.co → Información comercial. [simem.co] |
| Energía Firme del Cargo por Confiabilidad verificada por el Centro Nacional de Despacho | Datos asociados a la verificación de Obligaciones de Energía Firme (OEF) dentro del esquema de Cargo por Confiabilidad. Dataset destacado por SIMEM. [simem.co] | Permite detectar desviaciones entre capacidad comprometida y capacidad efectiva, comportamientos inusuales de cumplimiento y riesgos sistémicos en periodos críticos. | Reguladores, XM, generadores, inversionistas y entidades de planeación. | Impacta directamente la confiabilidad del sistema colombiano durante eventos de escasez energética. | Existe literatura sobre monitoreo de confiabilidad y suficiencia energética; no se encontró un estudio público específico sobre la detección de anomalías en este dataset de SIMEM. | Portal SIMEM: https://www.simem.co → Cargo por Confiabilidad (CxC). [simem.co] |

Priorización para modelos avanzados (multivariados y deep learning)

Mayor potencial analítico:

- Precio de Bolsa Nacional
- Demanda del SIN
- Generación Real por Planta
- Aportes Hidrológicos
- Eventos en Activos de Transmisión

La combinación de estos cinco datasets permite construir un marco multivariado de alta complejidad
(precio-demanda-generación-hidrología-red), que es probablemente el ecosistema más rico de SIMEM
para aplicar Autoencoders, LSTM, Temporal Fusion Transformers, Isolation Forest, One-Class SVM y
Graph Neural Networks para detección de anomalías operativas y de mercado.

