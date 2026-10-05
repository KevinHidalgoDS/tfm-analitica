1. El archivo BibTeX (referencias.bib)
Primero, tendrías un archivo donde almacenas la información bibliográfica de los artículos, libros o papers que encontraste en bases de datos como Scopus o IEEE.

```text
@book{nielsen1993,
  title={Usability Engineering},
  author={Nielsen, Jakob},
  year={1993},
  publisher={Morgan Kaufmann}
}

@article{garcia2024,
  title={Evaluación de la carga cognitiva en interfaces de análisis de datos},
  author={García, L. y Pérez, J.},
  journal={Revista de Interacción Humano-Computador},
  volume={12},
  number={3},
  pages={45--60},
  year={2024}
}
```

2. El uso en tu documento Markdown (Entregable2.md)
Luego, dentro de la plantilla que generamos, llamas a las referencias usando la clave que definiste en el archivo .bib encerrada entre corchetes y con un arroba [@clave].

```text
## 1. Claridad del objetivo

* **Contexto general del proyecto:**
  * El sistema a evaluar es un panel interactivo diseñado para analistas financieros. Estudios recientes han demostrado que el exceso de información visual en este tipo de herramientas puede generar fatiga visual y abandono de la plataforma [@garcia2024].

---

## 3. Metodología utilizada

* **Justificación metodológica:**
  * Se eligió la técnica de observación contextual porque permite identificar comportamientos o frustraciones que los usuarios no suelen verbalizar en una entrevista tradicional, un principio fundamental en la evaluación de usabilidad [@nielsen1993]. Además, los descubrimientos derivados de esta técnica se cruzarán con los diarios de uso descritos en [@garcia2024].

---

## Referencias
<!-- MkDocs inyectará automáticamente la bibliografía aquí abajo -->
```

3. El resultado al compilar (Lo que verás en tu web/PDF)
Cuando compiles tu sitio con MkDocs, el plugin transformará automáticamente esos llamados en citas formales y generará la lista al final del documento con el formato de citación que hayas configurado (generalmente APA o IEEE por defecto):

(...) el exceso de información visual en este tipo de herramientas puede generar fatiga visual y abandono de la plataforma (García & Pérez, 2024).

(...) un principio fundamental en la evaluación de usabilidad (Nielsen, 1993).

Referencias

García, L., & Pérez, J. (2024). Evaluación de la carga cognitiva en interfaces de análisis de datos. Revista de Interacción Humano-Computador, 12(3), 45-60.

Nielsen, J. (1993). Usability Engineering. Morgan Kaufmann.

Nota de configuración extra:
Recuerda que para que la magia suceda, tu archivo mkdocs.yml debe tener habilitado el plugin indicando la ruta de tu archivo .bib:

```yaml
plugins:
  - bibtex:
      bib_file: "referencias_example.bib"
```

¿se puede usar referencias.bib fuera de mkdocs? es decir, se va a exportar el markdown a formato pdf sin hacer uso de mkdocs

Sí, absolutamente. De hecho, la sintaxis `[@clave]` no es exclusiva de MkDocs; es el estándar de facto para citar en Markdown académico.

Para exportar tu archivo Markdown a PDF usando tu archivo `referencias_example.bib` sin depender de MkDocs, la herramienta estándar y más potente es **Pandoc**.

Dado tu entorno de desarrollo y trabajo en ingeniería, usar Pandoc desde la terminal o integrarlo en tu flujo de trabajo te resultará muy natural. Funciona como un conversor universal de documentos y procesa las citas de forma nativa.

### 1. La solución por consola: Pandoc

Pandoc toma tu archivo Markdown, lee el archivo BibTeX y compila todo en un PDF (usualmente utilizando LaTeX o un motor de PDF por debajo).

El comando básico en la terminal sería:

```bash
pandoc entregable.md --citeproc --bibliography=referencias_example.bib -o entregable.pdf

```

**¿Qué hace este comando?**

* `entregable.md`: Tu documento fuente.
* `--citeproc`: Le dice a Pandoc que procese las citas que encuentre con el formato `[@...]`.
* `--bibliography=referencias.bib`: Le indica de dónde sacar los datos bibliográficos.
* `-o entregable.pdf`: Genera el archivo final en formato PDF.

### 2. Ajustar el estilo de citación (Ideal para la maestría)

Por defecto, Pandoc suele usar un formato similar a Chicago. Si para tus entregables de la universidad te exigen formato **APA** o **IEEE**, solo necesitas descargar un archivo de estilo `.csl` (Citation Style Language) desde repositorios oficiales como *Zotero Style Repository* y agregarlo al comando:

```bash
pandoc entregable.md --citeproc --bibliography=referencias_example.bib --csl=ieee.csl -o entregable.pdf

```

### 3. Alternativas visuales (Editores)

Si prefieres no usar la terminal y manejar todo desde tu entorno de edición de código:

* **VS Code:** Puedes instalar extensiones como **Markdown Preview Enhanced** o **Pandoc Citer**. Estas extensiones te permiten renderizar y exportar a PDF haciendo clic derecho, configurando en los ajustes de la extensión la ruta de tu archivo `.bib`.
* **Zettlr o Obsidian:** Son editores de Markdown pensados específicamente para escritura académica. Zettlr, por ejemplo, detecta automáticamente los archivos `.bib` en tu carpeta, autocompleta las citas mientras escribes `[@...` y tiene un botón nativo para exportar a PDF con las referencias ya procesadas.

El archivo Markdown que generamos previamente te servirá perfectamente sin tener que cambiarle ni una sola coma; la sintaxis seguirá funcionando en cualquiera de estos métodos.

Claves rápidas para su uso:
author: Los nombres se separan por and. Si el autor es una institución o empresa (como UPME o un equipo de desarrollo), se debe encerrar entre dobles llaves {{Nombre Institución}} para que el compilador no intente invertir el nombre como si fuera "Apellido, Nombre".

citekey: La primera palabra justo después de la llave de apertura (ej. perez2025_cognitivo) es el identificador único que usarás en tu archivo Markdown como [@perez2025_cognitivo]. Puedes nombrarlo como prefieras, pero la convención estándar es apellidoAño_palabraclave.

| Fenómeno / Regla | Definición | Efecto Práctico | Algoritmos Vulnerables en Python | Librerías y Algoritmos para Mitigarlo | Contexto Práctico |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Enmascaramiento (Masking) | Un grupo de datos atípicos distorsiona tanto los estadísticos globales (media, varianza) que se camuflan a sí mismos o a otros atípicos. | Falsos Negativos. Los atípicos no son detectados y pasan como datos normales. | scipy.stats.zscore, sklearn.covariance.EmpiricalCovariance, K-Means (sklearn.cluster.KMeans). | PyOD: pyod.models.iforest (Isolation Forest), pyod.models.mcd (Minimum Covariance Determinant). | Crítico en el entrenamiento de modelos donde la data base ya viene sucia. MCD crea una envolvente elíptica robusta ignorando la zona contaminada. |
| Inundamiento (Swamping) | Los verdaderos datos atípicos sesgan tanto el modelo que las fronteras de normalidad se desplazan, haciendo que los datos normales queden fuera. | Falsos Positivos. Datos legítimos son marcados erróneamente como anomalías. | PCA estándar (sklearn.decomposition.PCA), algoritmos de distancia global. | SciPy / Statsmodels: Uso de MAD (Median Absolute Deviation) con scipy.stats.median_abs_deviation. PyOD: pyod.models.lof (Local Outlier Factor). | Común cuando se intenta ajustar un umbral estricto sobre datos con alta varianza natural; LOF evalúa la densidad local para evitarlo. |
| Apalancamiento (Leverage) | Valores extremos en el espacio de las variables predictoras (X) que "jalan" la función de ajuste hacia ellos, reduciendo artificialmente su propio error residual. | El modelo parece ajustar bien el punto atípico (error bajo), arruinando el ajuste del resto de los datos normales. | Regresión OLS (statsmodels.api.OLS), modelos autorregresivos estándar. | Statsmodels: statsmodels.stats.outliers_influence.OLSInfluence (Distancia de Cook). Scikit-Learn: RANSACRegressor, HuberRegressor. | Usar la regresión robusta (Huber) penaliza linealmente los errores grandes en lugar de cuadráticamente, mitigando el apalancamiento. |
| Maldición de la Dimensionalidad | En espacios de muchas variables (columnas), la diferencia entre la distancia al punto más cercano y al más lejano tiende a cero. | Los algoritmos basados en distancias pierden capacidad de discriminación; todo parece estar a la misma distancia. | KNN (sklearn.neighbors.KNeighborsClassifier), LOF clásico, DBSCAN básico. | PyOD: pyod.models.abod (Angle-Based Outlier Degree, mide varianza de ángulos en lugar de distancias), pyod.models.hbos (Histogram-based Outlier Score). | Al extraer muchas características (features) para modelos predictivos, reducir dimensionalidad con PCA previo o usar ABOD evita que el modelo colapse matemáticamente. |
| Atípicos Contextuales | Un valor que es completamente normal en el contexto global, pero anómalo en un periodo de tiempo, región o estado del sistema específico. | Si no se aísla la variable de contexto (como la estacionalidad temporal), la anomalía es invisible. | Algoritmos de punto global (Isolation Forest estándar, Boxplots clásicos). | Statsmodels: statsmodels.tsa.seasonal.STL (para extraer tendencia y estacionalidad). Sktime / Prophet: Modelado de expectativas temporales. | El mayor reto en el monitoreo de series de tiempo. Lo que es normal al mediodía es un atípico severo a las 3 AM. |
| Anomalías Colectivas | Una secuencia entera de datos o un patrón estructural es anómalo, aunque ningún punto individual dentro de la secuencia rompa los umbrales. | Ceguera total en la evaluación punto por punto (Point-wise detection). | Casi cualquier algoritmo estándar de PyOD evaluado fila por fila. | Stumpy: Cálculo de Matrix Profile (stumpy.stump). Tslearn / Keras: Modelos secuenciales como LSTMs o Hidden Markov Models. | Ocurre frecuentemente en infraestructura cuando un sensor se queda "congelado" reportando el mismo valor válido sin la varianza natural esperada. |
| Efecto de Borde (Edge Effect) | Los puntos situados en la periferia de un clúster denso tienen una densidad local intrínsecamente menor, simplemente por no tener vecinos en una dirección. | Micro-inundamiento: el algoritmo los clasifica como atípicos debido a la caída brusca de densidad. | LOF (sklearn.neighbors.LocalOutlierFactor). | HDBSCAN: hdbscan.HDBSCAN (algoritmo de clúster jerárquico basado en densidad), pyod.models.lscp (Ensembles de selección local). | Se puede comprobar mediante simulaciones de Monte Carlo generando clústers sintéticos con ruido y evaluando cómo se comportan los algoritmos en las fronteras. |
| Asimetría (Skewness) | El modelo asume una dispersión simétrica de los datos, cuando en realidad el proceso físico o de negocio tiene un sesgo natural hacia uno de los extremos (cola larga). | Doble error: Inundamiento en la cola larga (falsos positivos) y enmascaramiento en la cola corta (falsos negativos). | Z-score (scipy.stats.zscore), Boxplot de Tukey estándar ($Q3 + 1.5 \times IQR$). | Distfit: Ajuste exhaustivo de distribuciones empíricas. Scikit-Learn: PowerTransformer (Box-Cox, Yeo-Johnson) para simetrizar la varianza. | Fundamental en sistemas con límites inferiores estrictos en cero (como demandas del mercado energético). Forzar la normalidad genera alarmas falsas constantes; ajustar a distribuciones como Gamma o Weibull es mandatorio. |

[PyOd API CheatSheet](https://pyod.readthedocs.io/en/latest/api_cc.html)
