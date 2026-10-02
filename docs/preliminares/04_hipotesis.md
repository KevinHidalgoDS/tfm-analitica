# Hipótesis

## Hipótesis general

**HG:** Un marco de trabajo híbrido para la clasificación de anomalías, que combine métodos
estadísticos clásicos, técnicas de aprendizaje automático y un autocodificador de aprendizaje
profundo, alcanzará un desempeño de clasificación de anomalías superior al de cada método individual y al del mejor
método individual seleccionado exclusivamente, para cada conjunto de datos y escenario, a partir
del conjunto de validación.
Debido al posible desequilibrio entre observaciones habituales y atípicas, la superioridad se
evaluará mediante la medida F1 como métrica primaria, pues resume el equilibrio entre precisión y
exhaustividad. La precisión, la exhaustividad y el área bajo la curva de precisión-exhaustividad
(AUC-PR) se utilizarán como métricas secundarias, mientras que el área bajo la curva ROC (AUC-ROC)
se reportará con finalidad complementaria. No se utilizará la exactitud como criterio principal,
dado que puede resultar poco informativa cuando las observaciones atípicas son minoritarias. La
comparación se realizará sobre los conjuntos de datos y escenarios experimentales definidos, sin
seleccionar el método de referencia mediante los resultados del conjunto de prueba.

## Hipótesis específicas

- **HE1:** El esquema de ensamblado, implementado mediante la agregación ponderada de puntuaciones
  de atipicidad normalizadas, reduce la tasa de falsos positivos respecto de cada método individual
  y del mejor método individual seleccionado para cada conjunto de datos y escenario con los datos
  de validación, sin aumentar la tasa de falsos negativos en más de \(\delta = 0{,}05\), equivalente
  a cinco puntos porcentuales.
- **HE2:** Existe una interacción significativa entre el método de clasificación de anomalías, el
  tipo de anomalía y la dimensionalidad del conjunto de datos, de modo que el método con mejor
  desempeño depende del escenario experimental evaluado.
- **HE3:** Ante incrementos controlados del volumen de datos y manteniendo equivalentes los recursos
  computacionales, la arquitectura de microservicios presentará una degradación de la latencia y un
  aumento del caudal de procesamiento no mayores que los de una implementación monolítica
  equivalente.
- **HE4:** Los usuarios no especializados que consulten una interfaz de visualización con puntuaciones de atipicidad y
  variables explicativas obtendrán mejores resultados de comprensión e interpretación que los
  usuarios que consulten únicamente una lista de observaciones detectadas, considerando la
  proporción de respuestas correctas, el tiempo de respuesta y la comprensión percibida.

## Hipótesis nulas y reglas de decisión

- **H0-HG:** No existen diferencias estadísticamente significativas en la medida F1 entre el marco
  híbrido y los métodos individuales ni entre el marco híbrido y el mejor método individual
  seleccionado en validación.
- **H0-HE1:** El ensamblado no reduce la tasa de falsos positivos frente a las referencias ni
  mantiene la tasa de falsos negativos dentro del margen de no inferioridad \(\delta = 0{,}05\).
- **H0-HE2:** No existe una interacción estadísticamente significativa entre el método de
  clasificación de anomalías, el tipo de anomalía y la dimensionalidad sobre la medida F1.
- **H0-HE3:** Ante incrementos controlados del volumen de datos, no existen diferencias en la
  degradación de la latencia, el caudal de procesamiento ni el uso de recursos entre las
  arquitecturas de microservicios y monolítica.
- **H0-HE4:** No existen diferencias estadísticamente significativas entre las condiciones de
  interfaz en comprensión, exactitud o tiempo de respuesta.

Estas hipótesis serán contrastadas empíricamente a partir de los experimentos descritos en la
sección de Metodología, mediante el diseño de escenarios controlados sobre conjuntos de datos con
observaciones atípicas etiquetadas (reales o sintéticas) y la aplicación de pruebas estadísticas de
comparación de desempeño entre métodos. La comparación de HG incluirá cada método individual y el
mejor método individual para cada conjunto de datos y escenario, seleccionado exclusivamente
mediante la medida F1 obtenida en validación;
el conjunto de prueba se utilizará únicamente para la comparación final. Esta separación es
pertinente porque el desempeño de los métodos de clasificación de anomalías depende del tipo de anomalía, la
disponibilidad de etiquetas y el diseño de los datos de referencia [@chandola2009anomaly]. Para HG,
se considerará que existe una diferencia
estadísticamente significativa cuando el análisis inferencial alcance un nivel de significancia de
alfa = 0,05; además, se reportarán intervalos de confianza y tamaños de efecto para valorar la
relevancia práctica de las diferencias. Para HE1, la reducción de falsos positivos se contrastará
como una diferencia favorable respecto de cada referencia, y el aumento de falsos negativos se
evaluará mediante un criterio de no inferioridad con margen \(\delta = 0{,}05\). Este margen se
justifica como una tolerancia máxima de cinco puntos porcentuales para priorizar la reducción de
alertas falsas sin deteriorar sustancialmente la detección de anomalías. La selección de umbrales
de decisión, la normalización de puntuaciones, las ponderaciones y los demás parámetros del
experimento se realizará con los datos de entrenamiento y validación, y las etiquetas del
conjunto de prueba se reservarán para la evaluación final. En HE3, los umbrales de latencia y
caudal se fijarán antes de ejecutar las pruebas de carga y se mantendrán constantes al comparar
ambas arquitecturas.

La decisión estadística se expresará como rechazo o no rechazo de la hipótesis nula, con un nivel
de significancia de \(\alpha = 0{,}05\). No rechazar una hipótesis nula no se interpretará como
evidencia de equivalencia. Para las comparaciones de no inferioridad se utilizará el margen
\(\delta = 0{,}05\), fijado a priori, y se reportarán intervalos de confianza, tamaños de efecto y
la dirección de las diferencias.

## Operacionalización de las hipótesis

| Hipótesis | Variable independiente | Variables dependientes | Comparación | Diseño y análisis |
|:--|:--|:--|:--|:--|
| HG | Tipo de método | F1, precisión, exhaustividad y AUC-PR | Marco híbrido frente a cada método y al mejor método individual | Comparación pareada, pruebas no paramétricas y tamaño de efecto |
| HE1 | Estrategia de combinación | Tasa de falsos positivos y tasa de falsos negativos | Ensamblado frente a cada referencia y al mejor método | Prueba de diferencia y no inferioridad con \(\delta = 0{,}05\) |
| HE2 | Método, tipo de anomalía y dimensionalidad | F1, precisión, exhaustividad y AUC-PR | Métodos entre escenarios factoriales | Análisis de efectos principales e interacción |
| HE3 | Arquitectura y volumen de carga | Latencia, caudal, CPU y memoria | Microservicios frente a monolito | Prueba de carga con varios niveles y análisis de escalabilidad |
| HE4 | Tipo de interfaz | Comprensión, respuestas correctas, tiempo y confianza | Interfaz explicativa frente a lista de resultados | Experimento con usuarios y comparación entre condiciones |
