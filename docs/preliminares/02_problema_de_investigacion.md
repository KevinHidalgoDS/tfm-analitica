# Problema de Investigación

## Planteamiento del problema

La literatura ha desarrollado y sistematizado diversos métodos para detectar observaciones
atípicas, con enfoques y supuestos distintos [@chandola2009anomaly; @pang2021deep]. Sin embargo,
llevar estos métodos a una solución utilizable también plantea retos de integración, mantenimiento
y despliegue, documentados en la literatura sobre sistemas de aprendizaje automático y MLOps
[@sculley2015hidden; @kreuzberger2023mlops]. En una solución aplicada, es necesario evaluar por
separado el desempeño de detección, la respuesta ante distintos volúmenes de datos y la consulta
de los resultados por parte de sus usuarios. Esta tesis aborda la integración de dichos
componentes y su evaluación en un contexto delimitado de análisis por lotes.

En términos concretos, el problema de investigación se formula mediante la siguiente pregunta
principal: ¿cómo diseñar e implementar una solución basada en microservicios que integre una API
para detectar observaciones atípicas en conjuntos de datos tabulares procesados por lotes y un
tablero de visualización para consultar sus resultados, y cómo evaluar el desempeño de detección,
el comportamiento operativo y la utilidad del tablero para los usuarios?

Esta pregunta se desglosa en tres preguntas específicas:

1. ¿Qué desempeño de detección alcanza la combinación de métodos estadísticos clásicos y técnicas
   de analítica y aprendizaje automático en comparación con cada método aplicado por separado sobre
   conjuntos de datos tabulares etiquetados?
2. ¿Cómo varían los tiempos de respuesta y el rendimiento de la solución ante distintos volúmenes
   de datos?
3. ¿Qué utilidad y facilidad de consulta perciben los usuarios al explorar los resultados mediante
   el tablero de visualización?

## Antecedentes y alcance de la contribución

La revisión de antecedentes, que se ampliará en el estado del arte, organiza el contexto de la
investigación. Para delimitar la contribución propuesta, se consideran tres dimensiones de trabajo:

- **Integración de métodos:** se comparará el desempeño de una combinación de métodos estadísticos
  y de aprendizaje automático mediante un esquema de ensamblado por votación o combinación de
  puntuaciones, y se contrastará con el desempeño de cada método individual en los conjuntos de
  datos tabulares etiquetados seleccionados para el estudio. La utilidad del ensamblado se evaluará
  empíricamente; no se presupone que los métodos estadísticos sean necesariamente más interpretables
  ni que los métodos de aprendizaje automático detecten siempre patrones más complejos. Estas
  propiedades dependen de la técnica concreta y de su aplicación. Los criterios de combinación y
  ponderación se especificarán en la metodología.
- **Implementación y operación:** se integrarán los métodos seleccionados en una API y se desplegará
  la solución mediante microservicios; su comportamiento se evaluará bajo los volúmenes de datos y
  las condiciones experimentales definidos en la metodología.
- **Presentación de resultados:** se implementará un tablero para consultar los resultados de
  detección. Analistas o científicos de datos representativos de los usuarios previstos realizarán
  tareas definidas previamente: cargar un conjunto tabular, ejecutar la detección, localizar
  observaciones señaladas e inspeccionar las variables asociadas a estas. Se registrarán la
  proporción de tareas completadas, el tiempo de ejecución y los errores, y se aplicará el
  cuestionario System Usability Scale (SUS) para medir la usabilidad percibida [@brooke1996sus].
  Estas medidas operacionalizan la efectividad, la eficiencia y la satisfacción de uso
  [@iso9241-11-2018]. La evaluación se refiere a la interfaz y a la presentación de resultados;
  no pretende medir la interpretabilidad intrínseca de los modelos. El diseño del tablero seguirá
  principios de comunicación visual de información [@few2006dashboard].

Esta tesis, en su modalidad de profundización, busca implementar y evaluar la solución integrada
para conjuntos de datos tabulares procesados por lotes. Su aporte se circunscribe a los métodos,
componentes de software, datos, cargas y participantes incluidos en la evaluación; no propone un
algoritmo novedoso ni pretende generalizar sus resultados más allá de esas condiciones.

## Justificación

La pertinencia de este trabajo de profundización radica en el diseño, la integración y la evaluación
contextualizada de una solución aplicada para detectar observaciones atípicas en datos tabulares
procesados por lotes. En la dimensión académica, se reportarán resultados comparativos de los
métodos seleccionados en los conjuntos de datos y bajo las condiciones experimentales definidas. En
la dimensión tecnológica, se implementará y documentará la API y su integración en una arquitectura
de microservicios. En la dimensión aplicada, se desarrollará un tablero para consultar los
resultados y se evaluará su utilidad con usuarios representativos. Las conclusiones se limitarán
a las técnicas, los conjuntos de datos, las cargas y los participantes incluidos; no se afirmará
una generalización a otros contextos sin evidencia adicional.
