# 🚀 Framework Híbrido para la Detección de Datos Atípicos (Microservicios & MLOps)

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)
[![Cloud: Azure](https://img.shields.io/badge/cloud-Azure-0078D4.svg)](https://azure.microsoft.com/)
[![Architecture: Microservices](https://img.shields.io/badge/architecture-Microservices_|_K8s-326ce5.svg)](https://kubernetes.io/)
[![Linter: SonarQube](https://img.shields.io/badge/linter-SonarQube-brightgreen.svg)](https://www.sonarqube.org/)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=KevinHidalgoDS_tfm-analitica&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=KevinHidalgoDS_tfm-analitica)

## 📖 Descripción del Proyecto

Este repositorio contiene la implementación del trabajo de grado en modalidad de profundización
para la **Maestría en Ingeniería - Analítica** de la **Universidad Nacional de Colombia, Sede
Medellín**.

El proyecto propone un framework híbrido para la detección de datos atípicos (outliers), integrando
la interpretabilidad de los métodos estadísticos clásicos (z-score robusto, rango intercuartílico,
distancia de Mahalanobis) con la capacidad de captura de patrones complejos de algoritmos de
Machine Learning (Isolation Forest, Local Outlier Factor) y Deep Learning (Autoencoders).
Toda la solución está orquestada sobre una arquitectura de microservicios escalable en la nube,
facilitando el monitoreo continuo de la calidad de los datos en entornos organizacionales.

---

## 📂 Estructura de Directorios

La arquitectura de software desacopla los componentes de ingesta, procesamiento, modelado y
visualización en servicios independientes.

```text
├── .github/workflows/   # CI/CD pipelines (GitHub Actions).
├── data/                # DVC trackeado (raw, processed) - respaldado en Azure Blob Storage.
├── docs/                # Documentación del proyecto (MkDocs/Swagger).
├── infrastructure/      # Plantillas de IaC (Terraform) y manifiestos de Kubernetes (AKS).
├── services/            # Código fuente de cada microservicio independiente.
│   ├── ingestion/       # Validación de esquemas y encolamiento.
│   ├── preprocessing/   # Imputación, estandarización y partición.
│   ├── stat_detector/   # [Capa 1] Detección estadística (SciPy, statsmodels).
│   ├── ml_detector/     # [Capa 2] Detección ML/DL (scikit-learn, PyOD, TensorFlow/PyTorch).
│   ├── ensemble/        # Ensamblado de puntajes (promedio ponderado o metamodelo supervisado).
│   └── api_gateway/     # Exposición de resultados vía FastAPI.
├── dashboard/           # Interfaz de usuario (Streamlit / Plotly Dash).
├── tests/               # Pruebas unitarias, de integración y de carga (Locust/JMeter).
├── docker-compose.yml   # Orquestación local para desarrollo.
├── .gitignore
├── dvc.yaml             # Pipeline de versionado de datos.
└── README.md            # Este archivo.
```

---

## ⚙️ Requisitos y Dependencias

El framework requiere un ecosistema de herramientas distribuido:

| Componente | Tecnologías | Propósito |
| :--- | :--- | :--- |
| **Lenguaje y Analítica** | `Python 3.x`, `pandas`, `scikit-learn`, `PyOD`, `TensorFlow` / `PyTorch` | Implementación de algoritmos de detección estadística, ML y DL. |
| **Contenedores y Orquestación** | `Docker`, `Kubernetes` | Empaquetado y escalamiento horizontal e independiente de cada microservicio. |
| **Infraestructura Cloud** | `Azure` (AKS, Blob Storage, Azure Functions) | Cómputo escalable y almacenamiento. *(El diseño es portable a AWS o GCP).* |
| **Mensajería** | `Apache Kafka` | Comunicación asíncrona y procesamiento de flujos (streaming) entre servicios. |
| **Persistencia** | `PostgreSQL` | Almacenamiento de metadatos y resultados estructurados. |
| **Exposición y UI** | `FastAPI`, `Streamlit` / `Plotly Dash` | Endpoints REST y dashboard de explicabilidad. |

---

## 🚀 Instalación y Configuración

### Dependencias Python por plataforma

Los archivos `requirements.txt` y `requirements-dev.txt` se mantienen para Windows.
En Ubuntu/Linux se usan `requirements-linux.txt` y `requirements-dev-linux.txt`,
generados desde `pyproject.toml` con Python 3.14 y `pip-tools==7.6.1`.
No se deben generar los archivos de Linux desde Windows: las dependencias de
Jupyter incluyen paquetes distintos para cada sistema operativo.

Tras activar un entorno virtual con Python 3.14, instala las herramientas:

```bash
python -m pip install pip-tools==7.6.1 taskipy==1.14.1
```

En Windows, ejecuta `task pip-sync`. En Ubuntu/Linux, ejecuta `task pip-sync-linux`.
Para actualizar los archivos de Linux, ejecuta `task pip-compile-linux` y
`task pip-compile-dev-linux` en Ubuntu/Linux (o WSL) y versiona ambos archivos.
GitHub Actions instala estos archivos ya resueltos, sin regenerarlos en cada job.

#### Regenerar requisitos Linux desde un PC con solo Windows

El workflow **Regenerate Linux requirements** genera ambos archivos en Ubuntu
con Python 3.14, instala las dependencias y ejecuta las pruebas antes de publicar
un artefacto descargable. Los requisitos de desarrollo usan los de producción
como restricciones para mantener las versiones compartidas compatibles.

Se ejecuta automáticamente cuando un PR cambia `pyproject.toml`,
`requirements.txt` o `requirements-dev.txt`, y cuando esos cambios llegan a
`main` o `develop`. También puedes ejecutarlo desde **Actions → Regenerate Linux
requirements → Run workflow**, seleccionando la rama que contiene tus cambios.
Activa `upgrade` si quieres actualizar todas las versiones compatibles; sin esa
opción se conservan las versiones fijadas que sigan siendo compatibles.
Para ejecutarlo manualmente, el workflow debe existir en la rama predeterminada
del repositorio.

Desde Windows:

1. Modifica las dependencias y regenera los requisitos de Windows.
2. Publica los cambios en tu rama y abre o actualiza el PR, o ejecuta el workflow manualmente.
3. Descarga el artefacto `linux-requirements-<run_id>` de la ejecución correspondiente a tu commit.
4. Extrae `requirements-linux.txt` y `requirements-dev-linux.txt` en la raíz del repositorio.
5. Versiona ambos archivos en la misma rama antes de fusionar el PR.

La generación no instala los archivos de Windows en Ubuntu ni escribe cambios
automáticamente en el repositorio. El job de pruebas habitual sigue usando los
archivos Linux versionados: si quedaron desactualizados, puede fallar hasta que
subas los archivos del artefacto. Versionar solo los requisitos de Windows no
introduce `pywinpty` en Linux, pero tampoco actualiza sus dependencias.

```bash
cd /mnt/d/tfm-analitica

python3.14 -m venv ~/.venvs/tfm-analitica
source ~/.venvs/tfm-analitica/bin/activate

python -m pip install --upgrade pip
python -m pip install pip-tools==7.6.1 taskipy==1.14.1
task pip-sync-linux

python -m pytest
```

**1. Clonar el repositorio y configurar versionado de datos:**

```bash
git clone https://github.com/KevinHidalgo/tesis-outliers-framework.git
cd tesis-outliers-framework
dvc pull  # Descarga los datasets desde el Blob Storage
```

**2. Despliegue Local (Entorno de Desarrollo):** Para pruebas locales, levanta todos los
microservicios, bases de datos y el broker de Kafka utilizando Docker Compose:

```bash
docker-compose up --build -d
```

**3. Despliegue en la Nube (Producción en Kubernetes):** Aplica los manifiestos sobre tu clúster
(ej. Azure Kubernetes Service):

```bash
kubectl apply -f infrastructure/k8s/
```

---

## 💻 Uso y Ejecución

El flujo de trabajo se basa en eventos.

1. **Ingesta:** Envía un lote de datos o un stream JSON al endpoint del microservicio de ingesta:
   ```bash
   curl -X POST "http://localhost:8000/api/v1/ingest" -H "Content-Type: application/json" -d @data_payload.json
   ```
2. **Procesamiento y Detección:** Kafka orquesta el paso de los datos por los microservicios de
   preprocesamiento, `stat_detector` y `ml_detector` de forma asíncrona.
3. **Monitoreo y Explicabilidad (Dashboard):** Accede a `http://localhost:8501` para abrir el
   dashboard. Allí podrás visualizar el puntaje de anomalía por observación, métricas agregadas
   (AUC-ROC, AUC-PR) y la contribución de cada variable mediante SHAP o desviación estandarizada.


---

## 📏 Estándares de Código

Para garantizar la mantenibilidad y calidad en el despliegue de microservicios:

- **Estilo y Linting:** Uso estricto de **Black** y **Flake8**.
- **Análisis Estático (SonarQube):** Integrado en el pipeline local y CI/CD para detectar code
  smells, asegurar correcta parametrización de linters y optimizar funciones complejas de parseo o
  expresiones regulares (evitando _backtracking_).
- **Documentación Autónoma:** Todos los endpoints construidos con **FastAPI** están
  autodocumentados mediante **OpenAPI/Swagger**.
- **Documentación del Proyecto (MkDocs):** Al compilar el sitio estático (ej. `mkdocs serve`),
  asegúrate de resolver todos los _warnings_ en consola (como etiquetas HTML sin cerrar o
  referencias a enlaces duplicados) para mantener un _build_ limpio.

---

## 📦 Versionado de Datos y Modelos

- **Datasets y Artefactos:** Los modelos serializados y los conjuntos de datos masivos se gestionan
  exclusivamente con **DVC (Data Version Control)** y se almacenan remotamente (ej. Azure Blob
  Storage o Amazon S3). No realizar commits de archivos grandes a Git.
- **Trazabilidad:** Cada ejecución de análisis genera un identificador único (Run ID) para auditar
  el flujo desde la ingesta hasta el ensamblado.

---

## 🧪 Testing y Validación

La arquitectura requiere validación algorítmica y estructural:

1. **Pruebas de Modelos:** `pytest` para evaluar las métricas de precisión, exhaustividad y
   F1-score del framework híbrido contra datasets de referencia (ej. repositorio ODDS).
2. **Pruebas de Carga y Rendimiento:** Utiliza **Locust** o **Apache JMeter** para inyectar
   volúmenes crecientes de datos al API y medir la latencia y el _throughput_ del sistema. [cite:
   5]

```bash
# Ejecutar suite de pruebas de carga
locust -f tests/load/locustfile.py --host=http://localhost:8000
```

---

## 🤝 Contribuciones e Integración Continua

- Las contribuciones deben seguir el flujo de Git estándar.
- El repositorio incluye pipelines de **GitHub Actions** que ejecutan automáticamente la
  integración (pruebas de `pytest`) y el despliegue continuo (CI/CD) de los contenedores Docker
  hacia los registros de imágenes.

---

## 📄 Licencia y Atribuciones

**Autor:** Kevin Ferney Hidalgo Higuita **Institución:** Universidad Nacional de Colombia, Sede
Medellín. **Licencia:** MIT License

Este framework fue diseñado para facilitar el cierre de la brecha entre la investigación
estadística algorítmica y la ingeniería de sistemas de datos modernos en organizaciones
productivas.
