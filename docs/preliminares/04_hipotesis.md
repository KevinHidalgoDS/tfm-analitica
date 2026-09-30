# Hipótesis

## Hipótesis general

**H1:** Un marco de trabajo híbrido para detectar observaciones atípicas, que combine métodos
estadísticos clásicos y técnicas de aprendizaje automático y se despliegue sobre una arquitectura
de microservicios en la nube, alcanzará un desempeño de detección superior al de los métodos
aplicados individualmente, medido mediante precisión, exhaustividad, medida F1, área bajo la curva
ROC (AUC-ROC) y área bajo la curva de precisión-exhaustividad (AUC-PR), sin comprometer
significativamente los tiempos de respuesta del sistema.

## Hipótesis específicas

- **H1a:** La combinación de métodos estadísticos y de aprendizaje automático mediante un esquema
  de ensamblado o de votación ponderada reduce la tasa de falsos positivos respecto de la
  aplicación individual de cada método, sin incrementar de manera proporcional la tasa de falsos
  negativos.
- **H1b:** El desempeño relativo de los distintos métodos de detección (estadísticos, de
  aprendizaje automático y de aprendizaje profundo) varía significativamente según el tipo de
observación atípica (puntual, contextual o colectiva) y según la dimensionalidad del conjunto de
datos, por lo que ningún método individual domina de manera uniforme sobre todos los escenarios evaluados.
- **H1c:** El despliegue del marco de trabajo de detección mediante una arquitectura de microservicios
  permite mantener tiempos de procesamiento y de respuesta compatibles con escenarios de monitoreo
  cuasi-continuo, en comparación con una implementación monolítica equivalente, a medida que
  aumenta el volumen de datos procesados.
- **H1d:** Un tablero de visualización que presente las puntuaciones de atipicidad junto con
  información sobre las variables asociadas a cada observación señalada mejora la comprensión
  percibida de los resultados por parte de usuarios no especializados en estadística, en comparación
  con la presentación de los resultados sin dicho componente explicativo.

Estas hipótesis serán contrastadas empíricamente a partir de los experimentos descritos en la
sección de Metodología, mediante el diseño de escenarios controlados sobre conjuntos de datos con
observaciones atípicas etiquetadas (reales o sintéticas) y la aplicación de pruebas estadísticas de
comparación de desempeño entre métodos.
