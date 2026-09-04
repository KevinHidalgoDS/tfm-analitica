# 🚀 Framework Híbrido para la Detección de Datos Atípicos (Microservicios & MLOps)

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)
[![Cloud: Azure](https://img.shields.io/badge/cloud-Azure-0078D4.svg)](https://azure.microsoft.com/)
[![Architecture: Microservices](https://img.shields.io/badge/architecture-Microservices_|_K8s-326ce5.svg)](https://kubernetes.io/)
[![Linter: SonarQube](https://img.shields.io/badge/linter-SonarQube-brightgreen.svg)](https://www.sonarqube.org/)

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
