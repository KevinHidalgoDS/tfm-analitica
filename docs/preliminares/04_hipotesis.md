# Hipótesis

## Hipótesis general

**H1:** Un framework híbrido de detección de datos atípicos que combine métodos estadísticos
clásicos y técnicas de analítica/aprendizaje automático, desplegado sobre una arquitectura de
microservicios en la nube, presenta un desempeño de detección (medido en términos de precisión,
exhaustividad y F1-score, así como del área bajo la curva ROC y bajo la curva de
precisión-exhaustividad) superior al de la aplicación aislada de un único método estadístico o de
un único algoritmo de aprendizaje automático, sin comprometer significativamente los tiempos de
respuesta del sistema.

## Hipótesis específicas

- **H1a:** La combinación de métodos estadísticos y de aprendizaje automático mediante un esquema
  de ensamblado o de votación ponderada reduce la tasa de falsos positivos respecto de la
  aplicación individual de cada método, sin incrementar de manera proporcional la tasa de falsos
  negativos.
- **H1b:** El desempeño relativo de los distintos métodos de detección (estadísticos, de
  aprendizaje automático y de aprendizaje profundo) varía significativamente según el tipo de
  anomalía (puntual, contextual o colectiva) y según la dimensionalidad del conjunto de datos, por
  lo que ningún método individual domina de manera uniforme sobre todos los escenarios evaluados.
- **H1c:** El despliegue del framework de detección mediante una arquitectura de microservicios
  permite mantener tiempos de procesamiento y de respuesta compatibles con escenarios de monitoreo
  cuasi-continuo, en comparación con una implementación monolítica equivalente, a medida que
  aumenta el volumen de datos procesados.
- **H1d:** Un dashboard que presente los puntajes de anomalía junto con explicaciones sobre las
  variables que más contribuyen a cada anomalía detectada mejora la comprensión e interpretabilidad
  percibida de los resultados por parte de usuarios no especializados en estadística, en
  comparación con la presentación de los resultados sin dicho componente explicativo.

Estas hipótesis serán contrastadas empíricamente a partir de los experimentos descritos en la
sección de Metodología, mediante el diseño de escenarios controlados sobre conjuntos de datos con
anomalías etiquetadas (reales y/o sintéticas) y la aplicación de pruebas estadísticas de
comparación de desempeño entre métodos.
