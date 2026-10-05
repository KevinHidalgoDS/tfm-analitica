# Escenario 1

## Datos

<!-- prettier-ignore -->
| Nombre del dataset | Descripción breve | Relevancia para análisis de anomalías | Casos de uso prácticos | Importancia estratégica | Antecedentes de análisis similar | Enlace directo al portal |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Precio de Bolsa Nacional (Mercado Spot) | Precio horario al que se tranza la energía mayorista, determinado por la intersección de oferta y demanda.<br><br>Periodicidad: Horaria. | Altamente volátil ante choques climáticos. Requiere modelos avanzados (ej. Autoencoders, LSTMs) multivariados (cruzando con hidrología y disponibilidad térmica) para detectar spikes atípicos, cambios de régimen abruptos o manipulación de ofertas. | Traders (gestión de riesgo financiero), CREG y SIC (monitoreo de poder de mercado e Índice de Oferta Residual), Generadores (optimización de estrategias de oferta). | Impacta directamente la formación de tarifas para el usuario final y determina la exposición financiera y riesgo de quiebra de los agentes comercializadores. | "Anomaly Detection and Market Power in Colombian Electricity Market" ([Documento de Trabajo, Banco de la República, 2022](https://www.banrep.gov.co/en/taxonomy/term/25/all?page=17&order=title&sort=desc)). | [Catálogo - Información Comercial](https://www.google.com/search?q=https://www.simem.co/datos/informacion-comercial) |
| Generación Real por Planta y Recurso | Energía inyectada físicamente al SIN por cada unidad generadora (hídrica, térmica, solar, eólica).<br><br>Periodicidad: Horaria. | Análisis multivariado cruzando la declaración de disponibilidad técnica vs. la generación efectiva permite identificar outages encubiertos, fallas de máquinas u omisiones en el despacho ideal. | XM (supervisión de seguridad), Operadores de planta (mantenimiento predictivo basado en datos), Auditores regulatorios. | Garantiza la confiabilidad estructural del sistema eléctrico al verificar el cumplimiento de las Obligaciones de Energía Firme (OEF) del Cargo por Confiabilidad. | "Evaluation of Anomaly Detection of an Autoencoder Based on Maintenance Information and Scada-Data" (Elsevier, modelo extrapolable a operación hidroeléctrica local). | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |
| Aportes Hídricos (Energía Equivalente) | Caudales naturales que ingresan a los embalses del sistema interconectado, convertidos en kWh.<br><br>Periodicidad: Diaria. | Variable de entrada fundamental. Detectar anomalías (sequías extremas, picos de vertimiento) con Deep Learning advierte de forma temprana fases críticas de estrés en el despacho. | XM (planeación energética de mediano/largo plazo), Generadores hidroeléctricos (curvas de vaciado y valoración de la prima de escasez del agua). | Al contar con una matriz eléctrica con ~68% de dependencia hídrica, anticipar variaciones anómalas es el eje principal para prevenir situaciones de racionamiento. | Estudios de variabilidad hidroclimatológica y series de tiempo de El Niño/La Niña emitidos periódicamente por XM e IDEAM. [Enlace](https://informeanual.xm.com.co/informe/pages/xm/22-condiciones-climaticas.html) | [Catálogo - Operación del SIN](https://www.google.com/search?q=https://www.simem.co/datos/operacion-del-sistema) |

Datasets a cruzar: Precio de Bolsa Nacional + Aportes Hídricos + Generación Real. Técnicas
posibles: Autoencoders Multivariados, Redes LSTMs (Long Short-Term Memory) o Transformers para
series de tiempo.

- **Por qué:** El mercado eléctrico colombiano tiene un ~68% de dependencia hídrica. Un análisis
  univariado del Precio de Bolsa generará demasiados "falsos positivos" de anomalías durante los
  fenómenos de El Niño, ya que la volatilidad es la norma.

- **El enfoque:** Al construir un modelo multivariado que ingeste simultáneamente las series de
  tiempo de caudales (aportes hídricos), la generación y el precio horario, la red neuronal aprende
  el "régimen normal" del mercado dadas unas condiciones climáticas específicas. Cualquier
  desviación en el espacio latente reconstruido indicará una verdadera anomalía: posible
  manipulación de precios, retención de energía o estrés estructural severo.

### 1. ¿Cuál es el problema?

- El problema principal radica en la necesidad de identificar observaciones atípicas que se desvían
  de manera significativa del comportamiento esperado dentro de un conjunto de datos.

- Estas anomalías pueden originarse por múltiples factores, como errores de medición, fraudes,
  fallas de sistemas, procesos generadores de datos heterogéneos o eventos excepcionales genuinos.

- Existe el desafío técnico de trasladar los diversos métodos algorítmicos a una solución de
  software utilizable, lo cual plantea retos de integración, mantenimiento y despliegue en
  producción.

- En el dominio específico del mercado eléctrico mayorista (SIMEM), este problema se traduce en la
  dificultad de detectar alteraciones estructurales complejas —como retención de energía, estrés
  del sistema o manipulación de ofertas— dentro de series de tiempo interdependientes y dinámicas.

### 2. ¿Por qué es importante?

- La validez de la analítica de datos y de la toma de decisiones depende directamente de la calidad
  de los datos utilizados, la cual se ve afectada por la presencia de estas observaciones atípicas.

- La correcta operación de los sistemas de aprendizaje automático requiere que el desempeño de
  detección, el comportamiento operativo ante distintos volúmenes de datos y la visualización de
  resultados sean viables y escalables de manera simultánea.

- A nivel estratégico en el sector eléctrico, identificar estas desviaciones es crítico porque
  impacta la formación de tarifas para el usuario final, determina la exposición financiera de los
  agentes comercializadores y garantiza la confiabilidad del sistema previniendo situaciones de
  racionamiento.

### 3. ¿Por qué no ha sido suficiente?

- Los métodos estadísticos univariados clásicos pueden resultar insuficientes porque no
  necesariamente logran detectar observaciones atípicas definidas por las relaciones entre
  múltiples variables.

- Las distintas familias de métodos (estadísticos, de aprendizaje automático y profundo) tienen
  diferentes supuestos, por lo que aplicarlos de manera aislada no garantiza capturar toda la
  diversidad de comportamientos inusuales.

- Abordar el análisis de forma teórica sin una arquitectura distribuida (como los microservicios)
  dificulta la separación de los componentes de ingesta, procesamiento y visualización, limitando
  la adaptabilidad de los recursos.

- En el mercado eléctrico, variables como el precio de bolsa son altamente volátiles y responden a
  choques climáticos; por tanto, los análisis aislados de caudales o capacidad instalada no bastan
  para detectar cambios de régimen que solo son visibles al cruzar simultáneamente la hidrología,
  la disponibilidad y el mercado.

### 4. ¿Cuál es la propuesta?

- Se propone diseñar e implementar un marco de trabajo híbrido que combine métodos estadísticos
  clásicos, algoritmos de aprendizaje automático y un autocodificador de aprendizaje profundo.

- La integración de las técnicas se realizará mediante una agregación ponderada de puntuaciones de
  atipicidad normalizadas para aprovechar los criterios complementarios de cada modelo.

- La solución será desplegada utilizando una arquitectura de microservicios en la nube para
  procesar eficientemente los conjuntos de datos tabulares por lotes.

- Se desarrollará un tablero interactivo de visualización que presentará las puntuaciones de
  atipicidad y las variables explicativas para facilitar la interpretación de usuarios no
  especializados.

- En el contexto del SIMEM, la propuesta se concreta en un modelo multivariado que ingeste de forma
  simultánea las series de tiempo de caudales, la generación y el precio horario, permitiendo que
  la red neuronal aprenda el "régimen normal" del mercado bajo condiciones climáticas específicas.

### 5. ¿Qué se espera encontrar?

- Se anticipa que el marco de trabajo híbrido alcance un desempeño de clasificación de anomalías
  superior al de los métodos individuales, optimizando el equilibrio entre precisión y
  exhaustividad (medida F1) y el área bajo la curva de precisión-exhaustividad (AUC-PR).

- Se espera que el esquema de ensamblado propuesto reduzca la tasa de falsos positivos frente a los
  métodos aislados, sin que esto aumente significativamente la tasa de falsos negativos.

- A nivel de infraestructura, se prevé que la arquitectura de microservicios mantenga la
  estabilidad en la latencia y en el caudal de procesamiento ante incrementos controlados en el
  volumen de datos.

- Se espera que el uso del tablero interactivo mejore significativamente la exactitud, el tiempo de
  respuesta y la comprensión de los resultados frente a la consulta de una lista plana de
  observaciones.

- Aplicado al mercado de energía, se espera encontrar que cualquier desviación reportada en este
  espacio multivariado indique verdaderas anomalías de alto impacto práctico, advirtiendo
  tempranamente sobre manipulación de precios, apagones encubiertos (_outages_) o fases críticas de
  estrés hidrológico.
