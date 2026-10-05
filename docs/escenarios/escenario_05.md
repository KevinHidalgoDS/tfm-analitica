# Escenario 5

## Datos

<!-- prettier-ignore -->
| Dataset | Estructura de datos | Complejidad temporal | Potencial de anomalías | Encaje con modelos avanzados | Justificación de prioridad |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Demanda Real del SIN (horaria) | Multivariado al desagregar por región, tipo de usuario (regulado/no regulado) y al cruzar con clima. La serie horaria nacional es la agregación de múltiples series con dinámicas distintas. | Alta: estacionalidad diaria, semanal, anual y efectos climáticos. La demanda responde a temperatura, días festivos y eventos macroeconómicos. | Alto: fraudes masivos, errores de medición, caídas o picos atípicos de consumo industrial, cambios inesperados en patrones regionales. Las anomalías suelen ser persistentes y localizadas. | Muy bueno. Autoencoders para detección de desviaciones en perfiles horarios, LSTM multivariado para capturar dependencias entre regiones, modelos de reconstrucción con ventanas temporales. La literatura reporta AE+BiLSTM con F1 de 93.89% en datos de consumo eléctrico. | Es la variable base para planeación operativa. Los estudios colombianos ya han aplicado análisis de subestaciones con AMI, identificando ~4% de subestaciones como outliers. La granularidad horaria y la desagregación regional ofrecen suficiente complejidad para modelos profundos. |

### 1. ¿Cuál es el problema?

El problema central radica en la identificación precisa y escalable de observaciones atípicas
dentro de series temporales de alta dimensionalidad y fuerte dependencia contextual,
específicamente en la **Demanda Real del SIN (horaria)**. La dificultad técnica y analítica obedece
a la **estructura de datos multivariada**: la serie nacional no es una señal simple, sino la
agregación de múltiples series con dinámicas distintas desagregadas por región, tipo de usuario
(regulado/no regulado) y variables climáticas. Esto genera una **alta complejidad temporal**
caracterizada por múltiples niveles de estacionalidad (diaria, semanal, anual) y respuestas a
factores exógenos como la temperatura, los días festivos y los eventos macroeconómicos, lo que hace
que la definición de "comportamiento normal" sea altamente dinámica.

### 2. ¿Por qué es importante?

Garantizar la calidad de estos datos es de prioridad crítica porque la demanda del SIN es la
variable base fundamental para la planeación operativa, el despacho de energía y la estabilidad del
sistema eléctrico nacional. Existe un **alto potencial de anomalías** con fuertes impactos técnicos
y económicos: desde fraudes masivos y errores de medición de la infraestructura, hasta caídas o
picos atípicos de consumo industrial y cambios inesperados en los patrones regionales. Estudios
aplicados al contexto colombiano revelan que cerca del 4% de las subestaciones con infraestructura
de medición avanzada (AMI) presentan comportamientos atípicos. Detectar de manera oportuna estas
anomalías (que suelen ser localizadas y persistentes) es indispensable para evitar sobrecostos,
mejorar las proyecciones energéticas y garantizar la seguridad del suministro.

### 3. ¿Por qué no ha sido suficiente?

Los enfoques tradicionales y las reglas estadísticas univariadas no han sido suficientes debido a
que fallan al capturar la **alta complejidad temporal** y las interrelaciones del sistema. Un valor
de demanda puede parecer estadísticamente normal en términos globales, pero constituir una anomalía
contextual grave si se cruza con las variables climáticas o si ocurre en un día festivo. Además,
desde una perspectiva de ingeniería de sistemas (MLOps), llevar modelos que sí capturen esta
complejidad a un entorno utilizable presenta grandes desafíos. A menudo, las soluciones se quedan
en algoritmos aislados en cuadernos de experimentación, careciendo de una arquitectura robusta
(capaz de manejar grandes volúmenes de datos por lotes) y de interfaces (tableros) que traduzcan la
detección de la anomalía en información digerible y causal para los operadores que planifican el
sistema, impidiendo así que el resultado técnico se traduzca en una decisión operativa.

### 4. ¿Cuál es la propuesta?

La propuesta consiste en implementar el marco de trabajo híbrido propuesto en la tesis (integrando
métodos estadísticos, técnicas de Machine Learning como Isolation Forest/LOF, y aprendizaje
profundo) desplegado sobre una arquitectura escalable en la nube (microservicios), y aplicarlo a la
Demanda Real del SIN. Este dominio tiene un **encaje muy bueno con modelos avanzados**. Dada la
granularidad horaria y la complejidad regional, se propone potenciar la detección mediante modelos
de aprendizaje profundo (como _Autoencoders_). Se implementarán modelos de reconstrucción con
ventanas temporales capaces de perfilar dinámicas horarias complejas y capturar dependencias entre
regiones, logrando así discriminar las variaciones estacionales legítimas de las verdaderas
anomalías. Todo este sistema analítico alimentará un tablero interactivo, permitiendo al usuario
cargar sus lotes de datos y visualizar rápidamente las puntuaciones de atipicidad junto con sus
variables explicativas (clima, región, festivos).

### 5. ¿Qué se espera encontrar?

En términos analíticos, se espera confirmar empíricamente el excelente encaje de estos datos con
los modelos de aprendizaje profundo en un esquema híbrido. La literatura especializada reporta
combinaciones de Autoencoders con redes recurrentes (AE+BiLSTM) que alcanzan un puntaje F1 de hasta
93.89% en datos de consumo eléctrico; se espera que nuestro marco híbrido se acerque a estos
niveles de rendimiento, reduciendo drásticamente la tasa de falsos positivos en comparación con los
métodos estadísticos aislados. Desde el punto de vista del sistema, se espera comprobar que la
arquitectura basada en microservicios pueda escalar eficientemente al procesar históricos robustos
de demanda horaria multivariada. Finalmente, se espera encontrar que el uso del tablero visual
interactivo reducirá el tiempo de interpretación y aumentará la comprensión del operador del SIN
frente a una lista de resultados estándar, permitiéndole identificar rápidamente si una anomalía
obedece a un factor exógeno genuino (ola de calor) o a un defecto que requiere intervención (error
de medición o anomalía industrial).
