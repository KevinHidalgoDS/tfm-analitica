# Introducción

La transformación digital de las organizaciones ha producido un incremento sostenido en el volumen,
la velocidad y la variedad de los datos generados en sectores tan diversos como las finanzas, la
salud, la industria manufacturera, las telecomunicaciones y el comercio electrónico. En este
contexto, la analítica de datos se ha consolidado como una disciplina central para transformar
grandes volúmenes de información en conocimiento accionable que soporte la toma de decisiones. Sin
embargo, la calidad de cualquier proceso analítico depende críticamente de la calidad de los datos
que lo alimentan, y uno de los principales factores que compromete dicha calidad es la presencia de
datos atípicos u outliers: observaciones que se desvían de manera significativa del comportamiento
esperado de un conjunto de datos y que pueden originarse por errores de medición, fraude, fallas de
sistemas, eventos excepcionales genuinos o procesos generadores de datos heterogéneos.

La detección de datos atípicos, entendida como el proceso de identificar patrones que no se ajustan
a la noción de comportamiento normal dentro de un conjunto de datos, constituye un campo de
investigación con más de seis décadas de desarrollo, cuyo origen se remonta a los trabajos pioneros
de la estadística clásica sobre pruebas de discordancia y detección de valores extremos. No
obstante, la irrupción del big data, el aumento de la dimensionalidad de los conjuntos de datos y
la necesidad de procesamiento en tiempo real han transformado radicalmente los requerimientos
técnicos y metodológicos que enfrenta esta tarea. Los métodos estadísticos clásicos —basados en
supuestos de distribución, medidas de dispersión como el rango intercuartílico, el z-score o
pruebas de Grubbs— continúan siendo ampliamente utilizados por su interpretabilidad y bajo costo
computacional, pero exhiben limitaciones sustanciales frente a datos de alta dimensionalidad,
relaciones no lineales entre variables y contextos donde la distribución subyacente es desconocida
o cambiante.

Paralelamente, el auge del aprendizaje automático (machine learning) y del aprendizaje profundo
(deep learning) ha dado lugar a una nueva generación de algoritmos de detección de anomalías —como
Isolation Forest, One-Class SVM, Local Outlier Factor, autoencoders y modelos basados en la función
de distribución empírica acumulada— capaces de capturar estructuras complejas y no lineales en los
datos sin necesidad de supuestos distribucionales estrictos. Estos enfoques, sin embargo, suelen
requerir mayor capacidad computacional, plantean retos de interpretabilidad y demandan
infraestructuras escalables para su despliegue en escenarios productivos.

En paralelo a esta evolución algorítmica, la computación en la nube y las arquitecturas de
microservicios han cambiado la forma en que se diseñan y operan los sistemas analíticos. La
posibilidad de desacoplar los componentes de ingesta, procesamiento, modelado y visualización en
servicios independientes, escalables y desplegables de forma autónoma, permite construir soluciones
de detección de anomalías más flexibles, mantenibles y capaces de integrarse con los ecosistemas de
datos empresariales existentes. No obstante, la literatura académica sobre detección de datos
atípicos se ha concentrado predominantemente en la comparación algorítmica sobre conjuntos de datos
estáticos, y ha prestado relativamente poca atención a la manera en que estos algoritmos deben
integrarse, operacionalizar y comunicarse dentro de arquitecturas modernas orientadas a servicios,
ni a cómo sus resultados deben traducirse en tableros de visualización que faciliten la
interpretación por parte de usuarios de negocio.

Este trabajo de tesis, desarrollado en la modalidad de profundización, se propone abordar
precisamente esta intersección: la construcción y evaluación de un framework de detección de datos
atípicos que integre métodos estadísticos clásicos y técnicas de analítica avanzada dentro de una
arquitectura de microservicios desplegada en la nube, complementada con un dashboard de
visualización orientado a la interpretación de resultados. La relevancia de este trabajo radica en
que no se limita a proponer o comparar algoritmos de detección, sino que aborda su viabilidad
operativa, su escalabilidad y su utilidad práctica para organizaciones que requieren monitorear la
calidad e integridad de sus datos de manera continua, aportando así un puente entre la
investigación estadística/analítica y la ingeniería de sistemas de datos modernos.
