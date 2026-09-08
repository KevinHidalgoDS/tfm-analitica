# Problema de Investigación

## Planteamiento del problema

A pesar de la extensa producción académica sobre algoritmos de detección de datos atípicos,
persiste una desconexión relevante entre el desarrollo metodológico de dichos algoritmos y su
implementación como sistemas operativos, escalables y accesibles para los equipos de analítica y
ciencia de datos. La mayoría de los estudios existentes evalúan el desempeño de los métodos de
detección de anomalías en entornos de laboratorio, sobre conjuntos de datos estáticos, sin
considerar las restricciones propias de un entorno productivo: variabilidad en el volumen de datos,
necesidad de reentrenamiento o recalibración periódica, heterogeneidad de las fuentes de datos,
requerimientos de disponibilidad y latencia, y la necesidad de comunicar los resultados de manera
comprensible a usuarios no especializados en estadística o en aprendizaje automático.

En términos concretos, el problema de investigación puede formularse mediante la siguiente
pregunta: ¿en qué medida un framework de detección de datos atípicos que combine métodos
estadísticos clásicos y técnicas de analítica/aprendizaje automático, desplegado sobre una
arquitectura de microservicios en la nube, permite mejorar la precisión, la escalabilidad y la
interpretabilidad de la detección de anomalías respecto de enfoques monolíticos o de un único
método, y cómo puede dicho framework traducirse en un dashboard que facilite la toma de decisiones
basada en datos?

## Vacío de conocimiento

La revisión preliminar de la literatura (desarrollada con mayor profundidad en el Estado del Arte)
evidencia tres vacíos específicos que esta investigación busca abordar:

- **Vacío metodológico:** la mayor parte de los estudios comparan algoritmos de detección de
  anomalías de forma aislada (estadísticos frente a machine learning, o machine learning frente a
  deep learning), pero existen pocas propuestas que evalúen sistemáticamente esquemas híbridos que
  combinen la interpretabilidad de los métodos estadísticos con la capacidad de captura de patrones
  complejos de los métodos de aprendizaje automático, aplicados de forma complementaria según las
  características de los datos.
- **Vacío arquitectónico y operativo:** la literatura sobre detección de anomalías rara vez discute
  su implementación como microservicios independientes, versionables y escalables en la nube, lo
  que limita la comprensión de cómo trasladar los hallazgos algorítmicos hacia soluciones de nivel
  productivo (MLOps) y las implicaciones de dicho tránsito sobre el desempeño, el costo
  computacional y la mantenibilidad.
- **Vacío en la interpretabilidad y comunicación de resultados:** existe escasa evidencia
  sistematizada sobre el diseño de tableros (dashboards) que traduzcan los resultados de los
  modelos de detección de anomalías —puntajes de anomalía, explicaciones de las variables
  contribuyentes, tendencias temporales— en insights comprensibles y accionables para usuarios de
  negocio, lo cual limita la adopción práctica de estas soluciones en las organizaciones.

Cerrar estos vacíos es relevante no solo desde una perspectiva académica, sino también práctica:
las organizaciones requieren cada vez más sistemas de monitoreo de calidad de datos y detección de
anomalías que sean simultáneamente rigurosos desde el punto de vista estadístico, escalables desde
el punto de vista de ingeniería, y comprensibles desde el punto de vista de negocio. Esta tesis, en
su modalidad de profundización, busca aportar una solución aplicada y evaluada empíricamente a este
problema, sin pretender un desarrollo puramente algorítmico novedoso, sino una integración
metodológica y tecnológica rigurosa, documentada y replicable.

## Justificación

La pertinencia de este trabajo se sustenta en tres dimensiones. En primer lugar, una dimensión
académica: contribuye a la literatura sobre integración de métodos estadísticos y de aprendizaje
automático para detección de anomalías, aportando evidencia empírica comparativa bajo condiciones
controladas. En segundo lugar, una dimensión tecnológica: propone y documenta un patrón de
arquitectura de microservicios para el despliegue de modelos de detección de anomalías,
contribuyendo a la práctica de MLOps aplicada a la calidad de datos. En tercer lugar, una dimensión
de aplicabilidad: el dashboard resultante constituye un artefacto tangible que puede ser adoptado o
adaptado por organizaciones interesadas en fortalecer sus procesos de gobierno y calidad de datos.
