# FIRMS Wildfire Detections and Data Application

Este script utiliza la API de FIRMS (Fire Information for Resource Management System) de la NASA para obtener datos de incendios detectados por satélite en una zona específica y mostrarlos en un mapa interactivo.

## Funcionalidades

* **Consulta de datos de incendios:** Obtiene datos de incendios de la API de FIRMS utilizando una clave de API.
* **Visualización de datos:** Muestra los datos de incendios en un mapa interactivo utilizando la librería `folium`.
* **Personalización:** Permite seleccionar la tecnología de detección de incendios (sensor) y la zona geográfica.
* **Control de transacciones:** Monitoriza el número de transacciones realizadas con la API para evitar exceder el límite.

## Dependencias

* `pandas`: Para la manipulación y análisis de datos.
* `geopandas`: Para trabajar con datos geoespaciales.
* `matplotlib`: Para la visualización de datos.
* `folium`: Para crear mapas interactivos.

Sí, tienes razón. El formato Markdown para la indentación en listas y bloques de código requiere un espacio en blanco al inicio de cada línea. 

Aquí te dejo el texto con la indentación corregida:

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone [invalid URL removed]
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtén una clave de API de FIRMS:**
   * Visita el sitio web de FIRMS: [https://firms.modaps.eosdis.nasa.gov/active_fire/](https://firms.modaps.eosdis.nasa.gov/active_fire/)
   * Regístrate para obtener una clave de API.

4. **Configura la clave de API:**
   * Reemplaza `'a0f1afd59cc42db75820a429a7617f3a'` en el script con tu clave de API.

## Uso

1. **Selecciona la tecnología de detección de incendios:**
   * Modifica la variable `model` en el script para elegir el sensor deseado (ej. `'VIIRS_NOAA21_NRT'`).

2. **Selecciona la zona geográfica:**
   * Modifica la variable `zone` en el script para elegir la zona deseada (ej. `'ESP'` para España, `'world'` para todo el mundo).

3. **Ejecuta el script:**
   * El script descargará los datos de incendios de la API de FIRMS.
   * Se generará un mapa interactivo (`mapa_incendios_espana.html`) que muestra los incendios en la zona seleccionada.

## Datos

Los datos de incendios se obtienen de la API de FIRMS de la NASA. La API proporciona información sobre la ubicación, la fecha, la hora y la intensidad de los incendios detectados por satélite.

## Resultados

El script genera un mapa interactivo que muestra la ubicación de los incendios detectados por satélite en la zona seleccionada. Cada incendio se representa como un círculo en el mapa, con un color que indica la intensidad del fuego.

## Limitaciones

* El script está limitado por el número de transacciones permitidas por la API de FIRMS.
* La precisión de los datos depende de la tecnología de detección de incendios utilizada.
```

**Recuerda que la indentación es crucial en Markdown para que el formato se visualice correctamente.**
