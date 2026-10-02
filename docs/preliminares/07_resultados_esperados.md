# Resultados Esperados

## Resultados técnicos

- Un marco de trabajo para detectar observaciones atípicas, documentado y con código disponible, que integre al
  menos un método estadístico clásico, dos algoritmos de aprendizaje automático (Isolation Forest y
  Local Outlier Factor) y un componente de aprendizaje profundo (autocodificador), combinados mediante
  un esquema de ensamblado mediante agregación ponderada de puntuaciones normalizadas,
  configurable a partir de los datos de entrenamiento y validación.
- Evidencia empírica comparativa del desempeño del esquema híbrido frente a cada método individual
  y frente al mejor método individual seleccionado exclusivamente con el conjunto de validación,
  sobre al menos tres conjuntos de referencia con observaciones atípicas etiquetadas,
  reportada mediante precisión, exhaustividad, medida F1, área bajo la curva ROC (AUC-ROC) y área
  bajo la curva de precisión-exhaustividad (AUC-PR), junto con las pruebas
  estadísticas de significancia correspondientes.
- Evidencia sobre la interacción entre el método de detección, el tipo de observación atípica y la
  dimensionalidad, mediante un diseño factorial aplicado a los escenarios definidos.
- Una arquitectura de microservicios funcional, contenerizada y desplegada en un entorno de nube,
  con documentación de su desempeño (latencia media, mediana, p95, p99, caudal, uso de CPU y
  memoria) frente a una implementación monolítica equivalente, bajo distintos volúmenes y niveles
  de concurrencia, y
  con una guía de portabilidad hacia al menos dos proveedores de nube adicionales al utilizado en
  la implementación de referencia.
- Un prototipo funcional de tablero interactivo de visualización que presente las puntuaciones de
  atipicidad y las variables explicativas asociadas, validado mediante una comparación con una lista
  de resultados que mida respuestas correctas, tiempo de interpretación, comprensión percibida y
  utilidad con usuarios no especializados.
- Un repositorio de código documentado (incluyendo diagramas de arquitectura, especificación de
  APIs y guía de despliegue) que permita la replicabilidad del sistema desarrollado por parte de
  terceros interesados.

## Resultados académicos

- Una sistematización crítica del estado del arte sobre la detección de observaciones atípicas, que articule los
  enfoques estadísticos clásicos, de aprendizaje automático y de aprendizaje profundo,
  identificando condiciones de aplicabilidad y complementariedad entre ellos, susceptible de ser
  publicada como artículo de revisión o presentada en un congreso del área.
- Evidencia empírica sobre las condiciones bajo las cuales los esquemas combinados para detectar
  observaciones atípicas superan a los métodos individuales, contribuyendo a la discusión académica sobre la
  complementariedad (más que la sustitución) entre la estadística clásica y las técnicas modernas
  de analítica en el dominio de la calidad de datos.
- Un patrón de arquitectura de microservicios para desplegar soluciones de detección de
  observaciones atípicas, documentado de forma que pueda ser referenciado y adaptado en futuros trabajos de
  investigación aplicada o en proyectos de analítica dentro de organizaciones.
- Recomendaciones prácticas para el diseño de tableros de visualización de resultados de detección
  de observaciones atípicas, orientados a la
  interpretabilidad y a la adopción por parte de usuarios no especializados, contribuyendo a la
  literatura, aún incipiente, sobre la comunicación efectiva de resultados analíticos complejos.

## Aplicabilidad práctica

Más allá de su contribución académica, se espera que el sistema desarrollado constituya un
artefacto de referencia utilizable —con adaptaciones necesarias— por organizaciones interesadas en
fortalecer sus procesos de monitoreo de calidad de datos, detección temprana de fraude, control de
procesos industriales o vigilancia de indicadores operativos, en contextos donde la escalabilidad,
la comprensión de los resultados y la integración con arquitecturas de datos modernas resultan tan relevantes
como el desempeño algorítmico. Este resultado es consistente con el carácter de
profundización de la maestría, orientado a la aplicación rigurosa y evaluada del conocimiento
estadístico y analítico sobre problemas reales de las organizaciones.

## Limitaciones anticipadas

Se anticipa que la evaluación estará condicionada por la disponibilidad de conjuntos de datos con
observaciones atípicas etiquetadas de calidad suficiente, por las restricciones presupuestales propias de una
implementación académica en la nube (lo que podrá limitar la escala de las pruebas de carga
respecto de un entorno productivo real) y por el tamaño necesariamente reducido de la muestra de
usuarios para la validación del tablero de visualización. Estas limitaciones serán explicitadas y discutidas en el
documento final de tesis, delimitando adecuadamente el alcance de las conclusiones.
