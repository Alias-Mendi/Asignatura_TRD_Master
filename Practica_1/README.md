# Asistente de depuración de Python con OpenAI y Stack Overflow

Este script de Python te ayuda a depurar tu código proporcionándote soluciones de Stack Overflow y explicaciones generadas por la IA de OpenAI.

## Funcionalidades

* **Detección de errores:** Ejecuta tu código Python y detecta errores automáticamente.
* **Búsqueda en Stack Overflow:** Busca en Stack Overflow soluciones al error encontrado, extrayendo el comentario más votado.
* **Explicación con IA:** Utiliza la API de OpenAI para obtener una explicación detallada del error y una posible solución, con ejemplos de código.
* **Formato amigable:** Presenta la información de forma clara y concisa, incluyendo el traceback del error.

## Dependencias

* `openai`: Para interactuar con la API de OpenAI.
* `python-dotenv`: Para cargar variables de entorno desde un archivo `.env`.
* `requests`: Para realizar solicitudes HTTP a Google y Stack Overflow.
* `beautifulsoup4`: Para analizar el HTML de las páginas web.
* `pandas`: Para organizar y analizar los datos de Stack Overflow.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone [invalid URL removed]
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Crea un archivo .env:**
   ```
   OPENAI_KEY=tu_clave_de_api_de_openai
   ```
   Reemplaza `tu_clave_de_api_de_openai` con tu clave de API de OpenAI.

## Uso

1. **Importa las funciones:**
   ```python
   from tu_script import execute_code_with_help
   ```

2. **Ejecuta tu código con la función `execute_code_with_help`:**
   ```python
   codigo = """
   # Tu código Python aquí
   print(variable_no_definida)
   """
   execute_code_with_help(codigo)
   ```

## Ejemplo

```python
execute_code_with_help("print(variable_no_definida)")
```

**Salida:**

```
⚠️ Error encontrado: name 'variable_no_definida' is not defined
🔍 Buscando solución en StackOverflow...
🔍 Los mejores resultados de StackOverflow son:
👉 [invalid URL removed] 
💡 Posible solución encontrada en StackOverflow:
Asegúrate de que la variable esté definida antes de usarla.

🤖 Consultando a GPT-3.5 para obtener ayuda...

⚠️ **Error encontrado:** El error "name 'variable_no_definida' is not defined" ocurre cuando intentas usar una variable que no ha sido definida previamente en tu código. Python no puede encontrar la variable en su espacio de nombres.

💡 **Posible solución:** Define la variable 'variable_no_definida' antes de la línea `print(variable_no_definida)`. Puedes asignarle un valor o crearla como una variable vacía.

```python
variable_no_definida = "Hola"
print(variable_no_definida)  # Salida: Hola

variable_no_definida = 123
print(variable_no_definida)  # Salida: 123
```

## Limitaciones

* La precisión de las soluciones depende de la calidad de los datos en Stack Overflow y la capacidad de la IA para comprender el error.
* El script está diseñado para errores de Python. No funcionará con otros lenguajes de programación.

