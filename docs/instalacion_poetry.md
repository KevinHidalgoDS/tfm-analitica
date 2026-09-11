

1. **Instalar pipx:** 1 min.
Instala `pipx` a nivel de usuario utilizando el gestor de paquetes estándar de Python.

```powershell
python -m pip install --user pipx

```

Para verificar que se ejecutó correctamente, revisa que la salida final del comando indique "Successfully installed pipx".


2. **Configurar el PATH:** 1 min.
Agrega los directorios de `pipx` a tu variable PATH para que PowerShell pueda reconocer sus comandos.

```powershell
python -m pipx ensurepath

```

Si el comando es exitoso, la consola imprimirá un mensaje confirmando que los directorios han sido añadidos (o que ya estaban presentes) en tu PATH.


3. **Reiniciar la terminal:** Prerrequisito.
**Cierra completamente tu ventana actual de PowerShell** y abre una nueva. Esto es estrictamente necesario para que el sistema recargue las variables de entorno y detecte el nuevo comando.


4. **Instalar Poetry:** 1 min.
En la nueva terminal, retoma la instalación de Poetry.

```powershell
pipx install poetry

```

Para verificar que Poetry quedó correctamente instalado y funcional, ejecuta `poetry --version`. Si te devuelve el número de versión, el problema está resuelto.

### 1. Instalación Global de Poetry

Para un entorno de ingeniería de software robusto, la mejor práctica es aislar las herramientas CLI del entorno de desarrollo del proyecto.

* **Vía `pipx` (Recomendado):** Instala Poetry de forma global en el sistema.
```bash
# Permite gestionar herramientas CLI de Python en entornos aislados
pipx install poetry

```


* **Configuración del entorno virtual:** Es ideal que Poetry cree el entorno `.venv` directamente dentro de la ruta local `D:\tfm-analitica` para facilitar la integración transparente con entornos de desarrollo y pipelines.


```bash
# Obliga a Poetry a crear el entorno virtual en la raíz del proyecto
poetry config virtualenvs.in-project true

```



### 2. Transición del `pyproject.toml` Existente

Actualmente, el proyecto `tfm-analitica` delega la gestión de dependencias a `pip-tools`, evidenciado por la definición de dependencias en texto plano y los comandos `pip-compile`. Poetry soporta de forma nativa los bloques de metadatos estándar, por lo que podemos adoptar su motor sin perder las configuraciones existentes de validación estática (Black, Ruff, Mypy, Pydocstyle).

* **Inicialización:** Ejecuta este comando en la raíz del proyecto. Dado que ya tienes un archivo `pyproject.toml` con la versión de Python `>=3.14`, Poetry lo leerá y preparará su propio bloque de gestión.


```bash
# Inicializa el formato de Poetry. Puedes saltar la adición interactiva de dependencias
poetry init

```



### 3. Migración y Resolución de Dependencias

El ecosistema actual divide las dependencias en `requirements.txt`, `requirements-dev.txt` y `requirements-docs.txt`. Al migrar, centralizaremos la orquestación en el `pyproject.toml` y sellaremos las versiones exactas en un archivo `poetry.lock`.

* **Dependencias de Producción (Core Analítico):**
```bash
# Añade pandas al entorno principal (las sub-dependencias como numpy y tzdata se resuelven automáticamente)
poetry add pandas

```


* **Dependencias de Desarrollo y Documentación:** Traslada el bloque `[dependency-groups]` al grupo de desarrollo de Poetry.


```bash
# Instala el stack de CI/CD, linting y generación de documentación con MkDocs en un grupo aislado
poetry add --group dev black coverage flake8 mkdocs mkdocs-bibtex mkdocs-dracula-theme mkdocs-git-revision-date-localized-plugin mkdocs-glightbox mkdocs-jupyter mkdocs-material mkdocs-with-pdf mkdocstrings-python mypy pydocstyle pylint pyrefly pytest pytest-cov ruff taskipy unittest-xml-reporting

```


*Nota:* La herramienta `pip-tools` se excluye de esta lista ya que Poetry asume el control total sobre la resolución de dependencias.

### 4. Limpieza de Estructura y Refactorización de Tareas

Una vez que el archivo `poetry.lock` ha sido generado, la presencia de archivos `.txt` heredados introduce ambigüedad en la estructura del repositorio.

* **Eliminación de archivos obsoletos:**
```bash
# Limpia el directorio de archivos generados previamente por pip-compile
Remove-Item requirements.txt, requirements-dev.txt, requirements-docs.txt

```


* **Ajuste de `taskipy`:** Edita tu archivo `pyproject.toml` para eliminar los comandos acoplados a `pip-tools`. Los comandos analíticos, de formato y pruebas (`task format`, `task lint`, `task test-cov`) quedan intactos.


```toml
# Eliminar exclusivamente estas tres líneas del bloque [tool.taskipy.tasks]:
# pip-compile = "pip-compile pyproject.toml --output-file=requirements.txt"
# pip-compile-dev = "pip-compile pyproject.toml --group=dev --output-file=requirements-dev.txt"
# pip-sync = "pip-sync requirements.txt requirements-dev.txt"

```



### 5. Activación y Ejecución

Para asegurar que el motor de ejecución esté listo para los modelos y procesamiento de datos, levanta el nuevo entorno unificado.

* **Sincronización final:**
```bash
# Instala el estado exacto definido en el lockfile
poetry install

```


* **Activación del shell virtual:**
```bash
# Accede al entorno virtual para ejecutar scripts de Python o tareas de Taskipy
poetry shell

```



Con esta arquitectura, el control de dependencias queda centralizado y estandarizado para despliegues escalables. ¿Hay algún requerimiento específico de orquestación en la nube o integración de pipelines automatizados que debamos contemplar al empaquetar este entorno?