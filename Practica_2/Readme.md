# Análisis de Variables en Documentos Académicos

Este proyecto analiza documentos académicos relacionados con nutrición y su impacto en la ganancia de masa muscular, pérdida de peso y mejora de la composición corporal. 

Utilizando una LLM (Large Language Model) descargada localmente desde Hugging Face, el proyecto extrae información relevante de los documentos PDF y la organiza en una tabla para su posterior análisis y visualización.

## Funcionalidades

* **Extracción de texto:** Extrae el texto de documentos PDF utilizando la librería `PyPDF2`.
* **Procesamiento de lenguaje natural (PNL):** 
    * Utiliza una LLM para resumir el contenido de los documentos.
    * Identifica y extrae variables clave de los textos.
* **Análisis de datos:** Crea una tabla con la información extraída, donde cada fila representa un documento y cada columna una variable de interés.
* **Visualización:** Genera un gráfico de barras que muestra la frecuencia de las variables en los documentos analizados.

## Dependencias

* `PyPDF2`: Para leer archivos PDF.
* `openai`: Para interactuar con la API de OpenAI (si se utiliza para resumir textos).
* `pandas`: Para la manipulación y análisis de datos.
* `seaborn` y `matplotlib`: Para la visualización de datos.
* Una LLM descargada desde Hugging Face (ej. `gpt-3.5-turbo`).

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone (en un futuro)
   ```
2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Descarga una LLM desde Hugging Face:** Sigue las instrucciones en [https://huggingface.co/models?other=LLM](https://huggingface.co/models?other=LLM) para descargar e instalar una LLM localmente.
4. **Configura la API de OpenAI (opcional):** Si utilizas la API de OpenAI para resumir los textos, crea un archivo `.env` y guarda tu clave de API:
   ```
   OPENAI_KEY=tu_clave_de_api_de_openai
   ```

## Uso

1. **Añade los documentos PDF a la carpeta `pdf/`**.
2. **Modifica la lista `pdf_files` en el script para que coincida con los nombres de tus archivos PDF.**
3. **Ejecuta el script de Python.**
4. **El script generará un gráfico de barras que muestra la frecuencia de las variables en los documentos.**

## Datos

El proyecto incluye una pequeña muestra de 5 documentos académicos en formato PDF.

## Resultados

El análisis identifica las variables más recurrentes en los documentos, proporcionando información valiosa sobre las áreas de interés en la investigación de nutrición y ejercicio.

## Limitaciones

* La precisión del análisis depende de la capacidad de la LLM para comprender y extraer la información relevante de los documentos.
* El proyecto está diseñado para analizar documentos académicos en inglés.
* La muestra de documentos incluida es pequeña.

