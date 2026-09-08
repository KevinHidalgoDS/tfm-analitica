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