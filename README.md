# 🚀 Repositorio de Prácticas de API REST

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-green)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![OpenAPI/Swagger](https://img.shields.io/badge/OpenAPI-6BAE23?logo=openapi-initiative&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)
![Udemy Course](https://img.shields.io/badge/Curso-Backend%20Developer%20(Udemy)-ec1c24?logo=udemy&logoColor=white)

---

## 📖 Descripción del Proyecto
Este repositorio reúne el conjunto de prácticas, conceptos y ejemplos de código desarrollados a lo largo de mi aprendizaje sobre **APIs REST** y el protocolo **HTTP**, enfocado en el ecosistema del desarrollo backend con **Python**. Abarca desde los fundamentos teóricos de la web y la arquitectura cliente-servidor hasta el diseño de APIs RESTful, manejo de métodos HTTP, negociación de contenidos, esquemas de autenticación y seguridad, serialización de datos (JSON/XML), documentación interactiva con **FastAPI (OpenAPI / Swagger)** y automatización de pruebas con **Pytest**.

Todo el contenido forma parte de mi especialización académica orientada al desarrollo backend:

1. **Curso de Backend Developer (Udemy):** Estudio teórico y práctico sobre la Web, arquitectura cliente-servidor, protocolo HTTP/HTTPS, métodos, cabeceras, códigos de respuesta, seguridad y principios de diseño RESTful.
2. **Prácticas y Ejercicios en Python (`be_api_rest`):** Implementación de scripts prácticos en Python para el consumo y construcción de servicios REST, manejo de autenticación (Basic Auth, API Key, Bearer Token), negociación de contenidos, documentación de APIs con Swagger UI y testing automatizado.

---

## 🎯 Objetivo
Consolidar el dominio técnico sobre el funcionamiento, diseño, consumo, documentación y pruebas de APIs RESTful siguiendo los estándares y buenas prácticas de la industria backend, logrando:

- Comprender la arquitectura **Cliente-Servidor**, el protocolo **HTTP/HTTPS** y los principios fundamentales de **REST**.
- Dominar los distintos **métodos HTTP** (GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD), identificando su idempotencia y comportamiento (*Safe Methods*).
- Gestionar **Headers**, **Query Parameters**, **Path Variables** y negociación de contenidos (`Content-Type` y `Accept`).
- Aplicar esquemas de **autenticación y seguridad** comunes en APIs REST (Basic Auth, API Keys, Bearer Tokens / JWT).
- Implementar **documentación interactiva y automatizada** mediante OpenAPI / Swagger con FastAPI.
- Validar y probar recursos mediante **pruebas unitarias y de integración** automatizadas utilizando `pytest` y `requests`.

---

## 🛠️ Requerimientos Técnicos / Temas Cubiertos
Este proyecto cumple con los estándares exigidos para el aprendizaje integral del desarrollo, consumo y pruebas de APIs RESTful:

### 1. Fundamentos de la Web y Protocolo HTTP
- ✅ **Arquitectura Cliente-Servidor:** Modelo de comunicación, peticiones (*Requests*) y respuestas (*Responses*).
- ✅ **Métodos HTTP e Idempotencia:** Uso práctico de GET, POST, PUT, PATCH, DELETE, HEAD y OPTIONS.
- ✅ **Códigos de Estado (Status Codes):** Manejo de respuestas 1xx, 2xx, 3xx, 4xx y 5xx.
- ✅ **Encabezados (Headers):** Configuración de `Content-Type`, `Accept` y headers personalizados.

### 2. Arquitectura REST y Diseño de APIs RESTful
- ✅ **Principios REST:** Cliente-servidor, Stateless (sin estado), Cacheable, Interfaz uniforme y sistema en capas.
- ✅ **Modelado de Recursos:** Naming conventions, URIs vs URLs, pluralización y estructura limpia de endpoints.
- ✅ **Formatos de Datos y Serialización:** Intercambio de información mediante JSON y XML, encoding UTF-8 y manejo de payloads.

### 3. Seguridad en APIs REST
- ✅ **Autenticación Básica (Basic Auth):** Validación de credenciales enviadas en los headers de solicitud.
- ✅ **API Keys:** Uso de llaves de acceso en Headers y Query Parameters.
- ✅ **Bearer Token:** Autenticación basada en tokens de acceso para recursos protegidos.

### 4. Documentación de APIs
- ✅ **OpenAPI & Swagger UI:** Generación de documentación interactiva de endpoints, esquemas de entrada/salida y modelos de error utilizando **FastAPI**.

### 5. Pruebas y Automatización de APIs
- ✅ **Consumo de HTTP en Python:** Integración con la librería `requests` para interactuar con servicios externos.
- ✅ **Pruebas Automáticas con Pytest:** Suite de tests automatizados en Python para verificar endpoints, códigos de estado y contratos de respuesta.

---

## 📂 Estructura del Repositorio

| Archivo / Directorio | Descripción |
| :--- | :--- |
| 📄 `temario.md` | Guía detallada del temario cubierto en el módulo de API REST. |
| 📄 `notas.md` | Apuntes teóricos sobre representaciones JSON/XML y comparación con SOAP. |
| 🐍 `api_documentada.py` | Ejemplo de API RESTful documentada con FastAPI, metadatos OpenAPI y manejo de excepciones. |
| 🐍 `accept-content-type.py` | Ejercicio sobre negociación de contenido (`Content-Type` / `Accept`). |
| 🐍 `basic_auth.py` | Implementación de cliente con autenticación **Basic Auth**. |
| 🐍 `bearer_token.py` | Implementación de cliente con autenticación por **Bearer Token**. |
| 🐍 `api_key.py` | Manejo de autenticación utilizando **API Key**. |
| 🐍 `primer_recurso.py` | Creación y consumo básico de un primer recurso REST. |
| 🐍 `post.py` / `put.py` / `patch.py` / `delete.py` / `head.py` / `options.py` | Scripts enfocados en el uso de cada método HTTP. |
| 🐍 `serialization.py` / `xml_example.py` | Ejemplos de serialización y deserialización de datos en formatos JSON y XML. |
| 🐍 `cliente_servidor.py` / `servidor.py` / `server.py` | Scripts demostrativos de comunicación cliente-servidor HTTP. |
| 📁 `api_test/` & `test_users.py` | Suite de pruebas unitarias y de integración automatizadas con `pytest`. |
| 📄 `requirements.txt` | Lista de dependencias de Python necesarias para ejecutar el proyecto. |

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Requisitos Previos
- Python 3.9 o superior.
- Git.

### 2. Clonar el Repositorio e Instalar Dependencias
```bash
# Clonar el repositorio
git clone https://github.com/jltamayocabello-droid/be_api_rest.git
cd be_api_rest

# Crear y activar entorno virtual (opcional pero recomendado)
python -m venv entorno_virtual

# En Windows (PowerShell):
.\entorno_virtual\Scripts\Activate.ps1
# En Linux/macOS:
source entorno_virtual/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Ejecutar los Scripts y Servidores de Ejemplo

#### Ejecutar la API Documentada (FastAPI + Uvicorn)
```bash
pip install fastapi uvicorn
uvicorn api_documentada:app --reload
```
> 💡 Accede a la documentación interactiva Swagger UI en: `http://127.0.0.1:8000/docs`

#### Ejecutar Pruebas Automatizadas con Pytest
```bash
pytest
```

---

## ✒️ Autor
**Jorge Tamayo Cabello**  
*Desarrollador Front-End*

## 📄 Licencia
Este repositorio es de carácter estrictamente académico y educativo. Todo el contenido es libre de ser consultado con fines de aprendizaje y referencia técnica.

## 🙏 Agradecimientos
- A **Udemy** por la excelente formación en desarrollo de backend mediante el curso de Backend Developer.
- A la **comunidad de desarrollo de software libre** por la creación y mantenimiento de herramientas de testing y depuración de primer nivel.