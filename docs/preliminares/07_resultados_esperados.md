# Resultados Esperados

## Resultados técnicos

- Un framework de detección de datos atípicos, documentado y con código disponible, que integre al
  menos un método estadístico clásico, dos algoritmos de aprendizaje automático (Isolation Forest y
  Local Outlier Factor) y un componente de aprendizaje profundo (autoencoder), combinados mediante
  un esquema de ensamblado configurable.
- Evidencia empírica comparativa del desempeño del esquema híbrido frente a los métodos
  individuales, sobre al menos tres conjuntos de datos de referencia con anomalías etiquetadas,
  reportada mediante precisión, exhaustividad, F1-score, AUC-ROC y AUC-PR, junto con las pruebas
  estadísticas de significancia correspondientes.
- Una arquitectura de microservicios funcional, contenerizada y desplegada en un entorno de nube,
  con documentación de su desempeño (latencia y throughput) bajo distintos volúmenes de datos, y
  con una guía de portabilidad hacia al menos dos proveedores de nube adicionales al utilizado en
  la implementación de referencia.
- Un prototipo funcional de dashboard interactivo que exponga los puntajes de anomalía, las
  explicaciones asociadas a cada detección y las métricas agregadas de desempeño del sistema,
  validado mediante una evaluación de utilidad percibida con usuarios representativos.
- Un repositorio de código documentado (incluyendo diagramas de arquitectura, especificación de
  APIs y guía de despliegue) que permita la replicabilidad del sistema desarrollado por parte de
  terceros interesados.

## Resultados académicos

- Una sistematización crítica del estado del arte en detección de datos atípicos, que articule los
  enfoques estadísticos clásicos, de aprendizaje automático y de aprendizaje profundo,
  identificando condiciones de aplicabilidad y complementariedad entre ellos, susceptible de ser
  publicada como artículo de revisión o presentada en un congreso del área.
- Evidencia empírica sobre las condiciones bajo las cuales los esquemas híbridos de detección de
  anomalías superan a los métodos individuales, contribuyendo a la discusión académica sobre la
  complementariedad (más que la sustitución) entre la estadística clásica y las técnicas modernas
  de analítica en el dominio de la calidad de datos.
- Un patrón de arquitectura de microservicios para el despliegue de soluciones de detección de
  anomalías, documentado de forma que pueda ser referenciado y adaptado en futuros trabajos de
  investigación aplicada o en proyectos de analítica dentro de organizaciones.
- Recomendaciones prácticas para el diseño de dashboards de detección de anomalías orientados a la
  interpretabilidad y a la adopción por parte de usuarios no especializados, contribuyendo a la
  literatura, aún incipiente, sobre la comunicación efectiva de resultados analíticos complejos.

## Aplicabilidad práctica

Más allá de su contribución académica, se espera que el sistema desarrollado constituya un
artefacto de referencia utilizable —con adaptaciones menores— por organizaciones interesadas en
fortalecer sus procesos de monitoreo de calidad de datos, detección temprana de fraude, control de
procesos industriales o vigilancia de indicadores operativos, en contextos donde la escalabilidad,
la interpretabilidad y la integración con arquitecturas de datos modernas resultan tan relevantes
como la precisión algorítmica en sí misma. Este resultado es consistente con el carácter de
profundización de la maestría, orientado a la aplicación rigurosa y evaluada del conocimiento
estadístico y analítico sobre problemas reales de las organizaciones.

## Limitaciones anticipadas

Se anticipa que la evaluación estará condicionada por la disponibilidad de conjuntos de datos con
anomalías etiquetadas de calidad suficiente, por las restricciones presupuestales propias de una
implementación académica en la nube (lo que podrá limitar la escala de las pruebas de carga
respecto de un entorno productivo real) y por el tamaño necesariamente reducido de la muestra de
usuarios para la validación del dashboard. Estas limitaciones serán explicitadas y discutidas en el
documento final de tesis, delimitando adecuadamente el alcance de las conclusiones.
