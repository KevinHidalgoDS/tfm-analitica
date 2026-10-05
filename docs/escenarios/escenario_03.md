# Escenario 3

## Datos

<!-- prettier-ignore -->
| Dataset | Estructura de datos | Complejidad temporal | Potencial de anomalías | Encaje con modelos avanzados | Justificación |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Generación Real por Planta | Multivariado natural: N plantas × T horas × tipo de combustible (matriz de alta dimensión). Cada planta es una serie temporal con dinámica propia, y las correlaciones entre plantas capturan relaciones espaciales (congestión, despacho). | Alta: estacionalidad horaria, semanal y anual, más efectos de mantenimiento, hidrología y precio. Series no estacionarias con regímenes operativos cambiantes. | Muy alto: caídas súbitas de generación, desviaciones entre generación programada y real, fallas de equipos, indisponibilidades no reportadas. Anomalías que se propagan entre plantas por restricciones de red. | Excelente. LSTM multivariado, autoencoders (AE) sobre matrices planta×hora, transformers para capturar dependencias entre plantas, graph neural networks (GNN) para relaciones topológicas. La estructura N×T permite reconstrucción multivariada con error de reconstrucción como señal de anomalía. | Es el dataset con mayor dimensionalidad y riqueza estructural del SIMEM. Permite formular el problema como detección de anomalías en series multivariadas con dependencias cruzadas, que es exactamente el escenario donde los modelos profundos superan a los métodos univariados. Además, hay precedentes metodológicos directos en plantas hidroeléctricas colombianas. |

### 1. ¿Cuál es el problema?

El problema general de investigación consiste en diseñar e implementar una solución basada en
microservicios para detectar observaciones atípicas (anomalías) en datos tabulares y exponer sus
resultados en un tablero para los usuarios, enfrentando además los retos de integración,
mantenimiento y despliegue documentados en las operaciones de sistemas de aprendizaje automático
(MLOps). Al integrar la idea del conjunto de datos del SIMEM ("Generación Real por Planta"), el
problema específico se traduce en detectar anomalías dentro de series temporales de alta dimensión
(N plantas × T horas × tipo de combustible) que presentan dinámicas propias y donde las
correlaciones entre plantas capturan relaciones espaciales complejas, como la congestión y el
despacho de energía.

### 2. ¿Por qué es importante?

La calidad de los datos es fundamental, pues de ella depende la validez de los análisis analíticos
que apoyan la toma de decisiones, pudiendo verse afectada por errores de medición, fallas de
sistemas o eventos excepcionales genuinos. En el contexto del dataset de "Generación Real por
Planta", abordar este problema es de suma importancia porque el potencial de anomalías es muy alto:
se presentan caídas súbitas de generación, desviaciones entre la generación programada y la real,
fallas de equipos e indisponibilidades no reportadas que terminan propagándose entre las distintas
plantas debido a las restricciones de la red eléctrica.

### 3. ¿Por qué no ha sido suficiente?

Metodológicamente, los métodos estadísticos univariados (como el rango intercuartílico o la
puntuación z robusta) identifican desviaciones variable por variable, pero no necesariamente logran
detectar las observaciones anómalas que se definen por relaciones conjuntas entre múltiples
variables. Esto resulta insuficiente para la "Generación Real por Planta", dado que su complejidad
temporal es alta (estacionalidad horaria, semanal, anual y cambios por mantenimiento, hidrología o
precio) y produce series no estacionarias con regímenes operativos cambiantes. Las dependencias
espaciales cruzadas hacen que un simple enfoque univariado o aislado ignore la riqueza estructural
del comportamiento del sistema interconectado.

### 4. ¿Cuál es la propuesta?

La propuesta investigativa es diseñar, implementar y evaluar un marco de trabajo híbrido para la
detección de anomalías que combine métodos estadísticos clásicos, métodos de aprendizaje automático
(como Isolation Forest y Local Outlier Factor) y un autocodificador (autoencoder) de aprendizaje
profundo, operado en una arquitectura de microservicios en la nube con un tablero interactivo.
Aplicando esto a la idea propuesta, el encaje de estos datos con los modelos avanzados de la
propuesta es excelente; la matriz multivariada permite emplear autoencoders (AE) sobre las matrices
de planta × hora, así como LSTMs multivariados, transformers o Graph Neural Networks (GNN),
permitiendo una reconstrucción donde el error de reconstrucción funja directamente como señal de
anomalía multivariada.

### 5. ¿Qué se espera encontrar?

Se espera que el esquema híbrido propuesto logre un desempeño de detección (medido en F1, precisión
y exhaustividad) superior al de los métodos individuales aislados, reduciendo la tasa de falsos
positivos sin incrementar significativamente los falsos negativos. Específicamente, al integrar la
idea del dataset del SIMEM, se espera corroborar empíricamente que, debido a la inmensa
dimensionalidad y las dependencias cruzadas de la matriz N×T, el componente de modelos profundos
supere con creces a los métodos univariados tradicionales. Así mismo, se espera que el tablero de
visualización mejore notablemente el tiempo de interpretación y la comprensión de estos resultados
complejos por parte de los usuarios no especialistas.
