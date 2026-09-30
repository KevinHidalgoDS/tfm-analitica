# Objetivos

## Objetivos generales

Diseñar, implementar y evaluar un marco de trabajo híbrido para detectar observaciones atípicas
que integre métodos estadísticos clásicos, métodos de aprendizaje automático y un autocodificador,
desplegado mediante una arquitectura de microservicios en la nube y complementado con un tablero
de visualización, para evaluar el desempeño de detección, la capacidad operativa y la utilidad de
los resultados en conjuntos de datos tabulares procesados por lotes.

## Objetivos específicos

1. Revisar y sistematizar de manera crítica los métodos estadísticos, de aprendizaje automático y
   de aprendizaje profundo existentes para detectar observaciones atípicas, identificando sus
   supuestos, fortalezas, limitaciones y condiciones de aplicabilidad, con el fin de fundamentar la
   selección de las técnicas que integrará el marco de trabajo propuesto.
2. Diseñar e implementar un marco de trabajo para detectar observaciones atípicas que combine,
   mediante un esquema de ensamblado o votación ponderada, métodos estadísticos clásicos, métodos
   de aprendizaje automático y un autocodificador, y evaluar su desempeño comparativo (precisión,
   exhaustividad, medida F1, área bajo la curva ROC (AUC-ROC) y área bajo la curva de
   precisión-exhaustividad (AUC-PR)) sobre conjuntos de referencia tabulares con observaciones
   atípicas etiquetadas.
3. Desarrollar una arquitectura de microservicios en la nube que permita la ingesta, el
   procesamiento, la ejecución del marco de trabajo de detección y la exposición de resultados mediante
   interfaces de programación de aplicaciones (API), evaluando su escalabilidad y sus tiempos de
   respuesta bajo distintos volúmenes y frecuencias de datos.
4. Construir un tablero interactivo de visualización que presente los resultados de detección en
   indicadores comprensibles para sus usuarios, y evaluar su utilidad percibida mediante una
   validación con usuarios representativos.
